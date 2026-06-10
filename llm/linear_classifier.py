import torch
import torch.nn.functional as F

class LinearClassifier:
    def __init__(self, input_dim, num_classes):
        self.W = torch.randn(input_dim, num_classes) * 0.01
        self.b = torch.zeros(num_classes)

    def forward(self, X):
        return X @ self.W + self.b

    def predict(self, X):
        scores = self.forward(X)
        return torch.argmax(scores, dim=-1)

    def compute_loss(self, X, y):
        scores = self.forward(X)
        loss = F.cross_entropy(scores, y)
        return loss

    def update_parameters(self, dW, db, learning_rate):
        self.W -= learning_rate * dW
        self.b -= learning_rate * db