import torch 
import math
import torch.nn.functional as F
import torch.nn as nn


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

    
    def forward(self, x):
        
        bsz, seq_len, _ = x.size()
        q = self.q_proj(x)
        k = self.k_proj(x)
        v = self.v_proj(x)

        q = q.view(bsz, seq_len, self.num_head, self.head_dim).transpose(1, 2)
        k = k.view(bsz, seq_len, self.num_head, self.head_dim).transpose(1, 2)
        v = v.view(bsz, seq_len, self.num_head, self.head_dim).transpose(1, 2)

        scores = torch.matmul(q, k.transpose(-1, -2))
        scores = scores / math.sqrt(self.head_dim)

        attn = F.softmax(scores, dim=-1)
        out = torch.matmul(attn, v)

        out = out.transpose(1, 2).contiguous().view(bsz, seq_len, self.hidden_dim)
        
        return self.out_proj(out)



