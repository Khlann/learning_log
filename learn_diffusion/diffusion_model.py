import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt


# 定义简单的神经网络模型
class SimpleModel(nn.Module):
    def __init__(self, input_dim):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, input_dim)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x


# 定义扩散过程
def forward_diffusion(x_0, t, betas):
    alpha_bars = torch.cumprod(1 - betas, dim=0)
    sqrt_alpha_bars_t = torch.sqrt(alpha_bars[t])
    # 调整形状以匹配 x_0
    sqrt_alpha_bars_t = sqrt_alpha_bars_t.unsqueeze(-1)
    sqrt_one_minus_alpha_bars_t = torch.sqrt(1 - alpha_bars[t])
    # 调整形状以匹配 x_0
    sqrt_one_minus_alpha_bars_t = sqrt_one_minus_alpha_bars_t.unsqueeze(-1)
    noise = torch.randn_like(x_0)
    x_t = sqrt_alpha_bars_t * x_0 + sqrt_one_minus_alpha_bars_t * noise
    return x_t, noise

# 训练模型
def train_model(model, num_timesteps, num_epochs, learning_rate):
    betas = torch.linspace(0.0001, 0.02, num_timesteps)
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    criterion = nn.MSELoss()

    for epoch in range(num_epochs):
        # 生成一些简单的数据用于训练
        x_0 = torch.randn(32, 10)
        t = torch.randint(0, num_timesteps, (x_0.shape[0],))
        x_t, noise = forward_diffusion(x_0, t, betas)

        # 预测噪声
        predicted_noise = model(x_t)

        # 计算损失
        loss = criterion(predicted_noise, noise)

        # 反向传播和优化
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 100 == 0:
            print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')


# 生成样本
def generate_samples(model, num_timesteps):
    betas = torch.linspace(0.0001, 0.02, num_timesteps)
    alpha_bars = torch.cumprod(1 - betas, dim=0)
    x_T = torch.randn(1, 10)
    x = x_T
    for t in reversed(range(num_timesteps)):
        alpha_t = 1 - betas[t]
        alpha_bar_t = alpha_bars[t]
        z = torch.randn_like(x) if t > 0 else torch.zeros_like(x)
        predicted_noise = model(x)
        x = (1 / torch.sqrt(alpha_t)) * (
                x - ((1 - alpha_t) / torch.sqrt(1 - alpha_bar_t)) * predicted_noise) + torch.sqrt(betas[t]) * z
    return x


if __name__ == "__main__":
    input_dim = 10
    num_timesteps = 100
    num_epochs = 1000
    learning_rate = 0.001

    model = SimpleModel(input_dim)
    train_model(model, num_timesteps, num_epochs, learning_rate)
    sample = generate_samples(model, num_timesteps)
    print("Generated sample:", sample)
    