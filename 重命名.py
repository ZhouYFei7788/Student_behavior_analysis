import os

# 文件夹路径
folder_path = r"D:\py_xiangmu\学生行为检测\1\2"

# 获取文件夹中的所有文件
files = os.listdir(folder_path)

# 过滤出所有jpg文件
jpg_files = [f for f in files if f.endswith(".txt")]

# 遍历所有jpg文件，进行重命名
for index, file in enumerate(jpg_files, start=1):
    # 构造新的文件名
    new_name = f"rt_{index:04d}.txt"  # 例如 rt_0001.jpg
    # 获取旧文件的完整路径
    old_file = os.path.join(folder_path, file)
    # 获取新文件的完整路径
    new_file = os.path.join(folder_path, new_name)
    # 重命名文件
    os.rename(old_file, new_file)

print("批量重命名完成！")
