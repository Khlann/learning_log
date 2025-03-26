import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from model.diffusion_model import SimpleModel, forward_diffusion

# 数据预处理
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,)),
    transforms.Lambda(lambda x: x.view(-1))  # 展平图像
])

# 加载 MNIST 数据集
train_dataset = datasets.MNIST(root='learn_diffusion/diffusion_project/data', train=True,
                               download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True)

# 初始化模型
input_dim = 784
num_timesteps = 100
num_epochs = 1000
learning_rate = 0.001

model = SimpleModel(input_dim)
betas = torch.linspace(0.0001, 0.02, num_timesteps)
optimizer = optim.Adam(model.parameters(), lr=learning_rate)
criterion = nn.MSELoss()

# 训练模型
for epoch in range(num_epochs):
    for batch_idx, (data, _) in enumerate(train_loader):
        if batch_idx >= 100:
            break
        t = torch.randint(0, num_timesteps, (data.shape[0],))
        x_t, noise = forward_diffusion(data, t, betas)

        # 预测噪声
        predicted_noise = model(x_t)
        # 计算损失
        loss = criterion(predicted_noise, noise)
        # 反向传播和优化
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

# 保存模型
torch.save(model.state_dict(), 'models/trained_model.pth')