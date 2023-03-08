import torch

class MyFirstNetwork(torch.nn.Module):
    def __init__ (self, imput_size, hidden_size, output_size):
        super(MyFirstNetwork, self).__init__()
