import torch
import torch.nn as nn
import math
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, hidden_dim, num_head):
        super().__init__()

        assert hidden_dim % num_head == 0
        self.hidden_dim = hidden_dim
        self.num_head = num_head
        self.head_dim = hidden_dim // num_head

        self.q_proj = nn.Linear(hidden_dim, hidden_dim, bias=False)
        self.k_proj = nn.Linear(hidden_dim, hidden_dim, bias=False)
        self.v_proj = nn.Linear(hidden_dim, hidden_dim, bias=False)
        self.out_proj = nn.Linear(hidden_dim, hidden_dim)
    
    def forward(self, x, mask=None):
        # (bz, len, hidden_dim)
        batch_size, seq_len, hidden_dim = x.size()
        q = self.q_proj(x)
        k = self.k_proj(x)
        v = self.v_proj(x)

        q = q.view(batch_size, seq_len, self.num_head, self.head_dim).transpose(1, 2)
        k = k.view(batch_size, seq_len, self.num_head, self.head_dim).transpose(1, 2)
        v = v.view(batch_size, seq_len, self.num_head, self.head_dim).transpose(1, 2)
        # (bz, num_head, seq_len, head_dim)

        scores = torch.matmul(q, k.transpose(-1, -2))
        scores = scores / math.sqrt(self.head_dim)
        # (bz, num_head, seq_len, seq_len)

        if mask is not None:
            scores = scores.masked_fill(mask == 0, float('-inf'))
        
        attn = F.softmax(scores, dim=-1)

        out = torch.matmul(attn, v)
        # (bz, num_head, seq_len, head_dim)
        out = out.transpose(1, 2).contiguous().view(batch_size, seq_len, self.hidden_dim)
        # (bz, seq_len, hidden_dim)
        out = self.out_proj(out)
        return out








