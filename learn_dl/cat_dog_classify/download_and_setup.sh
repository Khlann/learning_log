#!/bin/bash

# 下载数据集
kaggle competitions download -c dogs-vs-cats

# 检查数据集是否下载成功
if [ ! -f dogs-vs-cats.zip ]; then
    echo "数据集下载失败，请检查网络连接或 Kaggle API 凭证。"
    exit 1
fi

# 解压缩数据集
unzip dogs-vs-cats.zip -d data
cd data
unzip train.zip
unzip test1.zip

# 修改 .gitignore 文件
echo "data/" >> .gitignore

echo "数据集下载、解压缩完成，.gitignore 文件已更新。"