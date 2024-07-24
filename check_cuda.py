import  torch

# CUDA
# Check if CUDA is availabe | To verify if the correct version of the PyTorch has been installed

print(torch.cuda.is_available())

x = torch.rand(5, 3)
print(x)
