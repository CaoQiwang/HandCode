import numpy as np


def softmax(x):
    x_exp = np.exp(x-np.max(x, axis=-1, keepdims=True))
    return x_exp / np.sum(x_exp, axis=-1, keepdims=True)

def cross_entropy(y_true, y_pred_logits):
    prob = softmax(y_pred_logits)

    num_samples = y_true.shape[0]
    selected_prob = prob[np.arange(num_samples), y_true]

    loss = -np.mean(np.log(selected_prob + 1e-6))
    return loss