import torch
from torch.nn import Linear
from torch.autograd import Variable


inp = Variable(torch.randn(1,10))

myLayer = Linear(in_features=10, out_features=5, bias=True)
myLayer(inp)

print(myLayer.weight)
print(myLayer.bias)

# print(torch.randn(1,10))