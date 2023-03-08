from torch.nn import ReLU
import torch

sample_data = torch.Tensor([[1,2,-1,-1]])
myRelu = ReLU()
print(myRelu(sample_data))

