import torch

def arange(i: int):
    "Think for-loop"
    return torch.tensor(range(i))

def where(q, a, b):
    "Think if-statement"
    return (q * a) + (~q) * b


def ones_spec(out):
    pass


