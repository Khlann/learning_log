import torch 
import torch.nn as nn
from torchinfo import summary

class CatDogCNN(nn.Module):
    def __init__(self):
        super(CatDogCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(2)
        self.fc1 = nn.Linear(32*56*56, 128)
        self.relu3 = nn.ReLU()
        self.fc2 = nn.Linear(128, 2)

    def forward(self, x):
        x = self.pool1(self.relu1(self.conv1(x)))
        x = self.pool2(self.relu2(self.conv2(x)))
        x = x.view(-1, 32*56*56)
        x = self.relu3(self.fc1(x))
        x = self.fc2(x)
        return x

if __name__ == "__main__":
    # 创建模型实例
    model = CatDogCNN()

    # 模拟输入数据
    batch_size = 16
    channels = 3
    height = 224
    width = 224
    summary = summary(model, (batch_size, channels, height, width))
    input_tensor = torch.randn(batch_size, channels, height, width)

    # 前向传播
    output = model(input_tensor)

    # 输出形状
    print(f"Input shape: {input_tensor.shape}")
    print(f"Output shape: {output.shape}")   

    

