import torch
import torch.nn as nn
from torchvision import datasets, transforms
from models.cnn_model import CatDogCNN

# 数据预处理
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# 加载测试数据
test_data = datasets.ImageFolder(root='/home/arlen/arlen/learning_log/learn_dl/data/test1', transform=transform)
test_loader = torch.utils.data.DataLoader(test_data, batch_size=32, shuffle=False)

# 初始化模型并加载好训练好的参数
model = CatDogCNN()
model.load_state_dict(torch.load('cat_dog_cnn.pth'))
model.eval()

corret = 0
total = 0
with torch.no_grad():
    for data in test_loader:
        images, labels = data
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
print(f'Accuracy of the network on the test images: {100 * correct / total}%')
