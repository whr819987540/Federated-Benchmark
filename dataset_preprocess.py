import random
import os
from os.path import join
import shutil
import random
import time

dataset_path = "./VOC2005_1"
label_dir = join(dataset_path, "Annotations")
image_dir = join(dataset_path, "PNGImages")

# 遍历image_dir
# 以image_dir一级子目录名作为label
labels = os.listdir(image_dir)

# 以一级子目录名.文件名来合并所有图片到data目录
data_path = join(dataset_path, "data")
if os.path.exists(data_path):
    print("already split")
    exit()
else:
    print(f"make {data_path}")
    os.makedirs(data_path)
    os.makedirs(join(data_path, "raw"))
    os.makedirs(join(data_path, "train"))
    os.makedirs(join(data_path, "test"))


for label in labels:
    path = join(image_dir, label)
    for file_name in os.listdir(path):
        new_file_name = f"{label}.{file_name}"
        print(new_file_name)
        # 移动到data/raw
        new_path = join(data_path, "raw", new_file_name)
        old_path = join(path, file_name)
        shutil.copy(old_path, new_path)

# split data/raw to data/train data/test
file_names = os.listdir(join(data_path, "raw"))
random.seed(time.time())
random.shuffle(file_names)
ratio = 0.8
num = int(len(file_names)*ratio)
train_file_names = file_names[:num]
test_file_names = file_names[num:]

for train_file_name in train_file_names:
    src = join(data_path, "raw", train_file_name)
    dst = join(data_path, "train")
    shutil.copy(src, dst)

for test_file_name in test_file_names:
    src = join(data_path, "raw", test_file_name)
    dst = join(data_path, "test")
    shutil.copy(src, dst)
