import torch
import torch.nn as nn
import torch.nn.functional as F


class MultiHeadAttentionKVCache(nn.Module):
    def __init__(self, hidden_dim, num_head, use_kv=True):
        super().__init__()
        assert hidden_dim % num_head == 0
        self.num_head = num_head
        self.hidden_dim = hidden_dim
        self.head_dim = hidden_dim // num_head
        self.use_kv = use_kv

        self.q_proj = nn.Linear(hidden_dim, hidden_dim, bias=False)
        self.k_proj = nn.Linear(hidden_dim, hidden_dim, bias=False)
        self.v_proj = nn.Linear(hidden_dim, hidden_dim, bias=False)
        self.out_proj = nn.Linear(hidden_dim, hidden_dim)

        # 存储历史token
        self.history_seq = []

    def forward(self, q, k, v, past_key=None, past_value=None, mask=None):
        # Prefil阶段： seq_len > 1
        # Decoding阶段: seq_len = 1
        batch_size, seq_len, _ = q.shape

        if not self.use_kv:
            self.history_seq.append(q)

        # Q,K,V映射
        q = self.q_proj(q)
        if self.use_kv:
            k = self.k_proj(k)
            v = self.v_proj(v)

        # 切分多头[batch_size, seq_len, hidden_dim]->[batch_size, num_head, seq_len, head_dim]
        q = q.view(batch_size, seq_len, self.num_head, self.head_dim).transpose(1, 2)
        if self.use_kv:
            k = k.view(batch_size, seq_len, self.num_head, self.head_dim).transpose(1, 2)
            v = v.view(batch_size, seq_len, self.num_head, self.head_dim).transpose(1, 2)

        if self.use_kv:
            # KV Cache在seq_len维度去拼接
            # 拼接后[batch_size, num_head, seq_len+1, head_dim]
            if past_key is not None:
                k = torch.cat([past_key, k], dim=2)
            if past_value is not None:
                v = torch.cat([past_value, v], dim=2)
        else:
            # 标准多头
            history_seq = torch.cat(self.history_seq, dim=1)
            k = self.k_proj(history_seq)
            v = self.v_proj(history_seq)
            k = k.view(batch_size, -1, self.num_head, self.head_dim).transpose(1, 2)
            v = v.view(batch_size, -1, self.num_head, self.head_dim).transpose(1, 2)
        
        # 保存K,V用于下一次预测
        past_key_values = (k, v)

        # 多头注意力得分计算j]
        attn_scores = torch.matmul(q, k.transpose(-2, -1)) / (self.head_dim ** 0.5)

        if mask is not None:
            attn_scores = attn_scores.masked_fill(mask == 0, float('-inf'))
        
        attn_weights = F.softmax(attn_scores)
        attn_output = torch.matmul(attn_weights, v)

        # 拼接多头
        attn_output = attn_output.transpose(1, 2).contiguous()
        attn_output = attn_output.view(batch_size, seq_len, self.hidden_dim)

        # 输出映射
        output = self.out_proj(attn_output)

        return output, past_key_values


batch_size = 64
seq_len = 10
hidden_dim = 4096
num_head = 8
use_kv = False

# 模拟输入
x = torch.randn(batch_size, seq_len, hidden_dim)
mask = torch.full((1, 1, seq_len, seq_len), True)
mask = torch.triu(mask, diagonal=1)

mha_cache = MultiHeadAttentionKVCache(hidden_dim, num_head, use_kv=use_kv)

output, (past_k, past_v) = mha_cache(x, x, x, mask=mask)


# Prefill阶段
print("mask:", mask)
print("output:", output.shape, "past KV:", past_k.shape)

# Decoding阶段
N = 10
x = output
for _ in range(N):
    new_x = output[:, [-1], :]
    output, (past_k, past_v) = mha_cache(new_x, new_x, new_x, past_key=past_k, past_value=past_v)
    print("output:", output.shape, "past KV:", past_k.shape)

        

