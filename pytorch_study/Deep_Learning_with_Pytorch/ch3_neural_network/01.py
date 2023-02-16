from torch.nn import Linear
import torch

inp = torch.Variable(torch.randn(1,10))

myLayer = Linear(in_features=10, out_features=5, bias=True)
myLayer(inp)

print(myLayer.weight)

# print(torch.randn(1,10))