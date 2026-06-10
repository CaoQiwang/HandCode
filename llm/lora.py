import torch
import torch.nn as nn



class LoRALayer(nn.Module):
    def __init__(self, in_dim, out_dim, rank, alpha):
        super().__init__()

        std_dev = 1 / torch.sqrt(torch.tensor(rank).float())
        self.A = torch.nn.Parameter(torch.randn(rank, in_dim) * std_dev)
        self.B = torch.nn.Parameter(torch.zeros(out_dim, rank))
        self.scaling = alpha / rank

    def forward(self, x):
        return self.scaling * (x @ self.A.T @ self.B.T)
    

class LinearWithLoRA(nn.Module):
    def __init__(self, linear, rank, alpha):
        super().__init__()
        self.linear = linear
        self.lora = LoRALayer(
            linear.infeatures,
            linear.outfeatures,
            rank,
            alpha
        )
    
    def forward(self, x):
        return self.linear(x) + self.lora(x)

