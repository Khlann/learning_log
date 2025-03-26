import torch
from model.diffusion_model import SimpleModel, generate_samples

# 加载模型
input_dim = 784
num_timesteps = 100
model = SimpleModel(input_dim)
model.load_state_dict(torch.load('models/trained_model.pth'))
model.eval()

# 生成样本
sample = generate_samples(model, num_timesteps)
print("Generated sample:", sample)