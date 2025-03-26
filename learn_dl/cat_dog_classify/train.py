# 导入 PyTorch 库
import torch
# 导入 PyTorch 神经网络模块
import torch.nn as nn
# 导入 PyTorch 优化器模块
import torch.optim as optim
# 从 torchvision 库导入数据集和图像变换模块
from torchvision import datasets, transforms
# 从自定义模块中导入猫狗分类的 CNN 模型
from models.cnn_model import CatDogCNN

# 数据预处理部分
# 使用 transforms.Compose 组合多个图像变换操作
transform = transforms.Compose([
    # 将图像调整为 224x224 大小
    transforms.Resize((224, 224)),
    # 将图像转换为 PyTorch 张量
    transforms.ToTensor(),
    # 对图像进行归一化处理，均值和标准差都设为 0.5
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# 加载预训练数据
# 使用 ImageFolder 加载指定目录下的图像数据集
train_data = datasets.ImageFolder(root='/home/arlen/arlen/learning_log/learn_dl/data/train', transform=transform)
# 创建数据加载器，设置批量大小为 32，并开启数据打乱功能
train_loader = torch.utils.data.DataLoader(train_data, batch_size=32, shuffle=True)

# 定义模型、损失函数和优化器
# 初始化猫狗分类的 CNN 模型
model = CatDogCNN()
# 定义交叉熵损失函数，用于多分类问题
criterion = nn.CrossEntropyLoss()
# 定义 Adam 优化器，设置学习率为 0.001
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 训练模型
# 设置训练的总轮数
num_epochs = 10
# 开始训练循环
for epoch in range(num_epochs):
    # 初始化每一轮的累计损失
    running_loss = 0.0
    # 遍历训练数据加载器中的每个批次
    for i, data in enumerate(train_loader, 0):
        # 解包数据，获取输入图像和对应的标签
        inputs, labels = data
        # 清空优化器中的梯度信息
        optimizer.zero_grad()
        # 前向传播，将输入图像传入模型得到输出
        outputs = model(inputs)
        # 计算损失值，使用定义好的损失函数
        loss = criterion(outputs, labels)
        # 反向传播，计算梯度
        loss.backward()
        # 更新模型参数
        optimizer.step()
        # 累加当前批次的损失值
        running_loss += loss.item()
    # 打印每一轮的训练信息，包括轮数和平均损失
    print(f"Epoch {epoch + 1}, Loss: {running_loss / len(train_loader)}")

# 打印训练完成信息
print("Training Finished!")
torch.save(model.state_dict(), 'cat_dog_cnn.pth')