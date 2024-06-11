import os

def update_user(root_folder):
    print(f"遍历所有扇区文件: {root_folder}")
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            # 检查GRpluginSettings.txt文件
            if filename == "GRpluginSettings.txt":
                file_path = os.path.join(dirpath, filename)
                print(f"找到文件: {file_path}")
                
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # 检查字体大小为15的设置
                if "GroundLabel_FontSize=15" in content:
                    # 替换字体大小为13
                    updated_content = content.replace("GroundLabel_FontSize=15", "GroundLabel_FontSize=13")
                    
                    # 将更新后的内容写回文件
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(updated_content)
                    print(f"写回: {file_path}")
                else:
                    print(f"没有找到匹配的字体大小条目: {file_path}")

            # 检查VATPRC Alias.txt
            elif filename == "VATPRC Alias.txt":
                file_path = os.path.join(dirpath, filename)
                print(f"找到Alias文件: {file_path}")

                # 读取E:\ATC\ES PLUGIN\Alias\Alias.txt文件的内容
                with open(r"E:\ATC\ES PLUGIN\Alias\Alias.txt", 'r', encoding='utf-8') as alias_file:
                    alias_content = alias_file.read()

                # 将Alias文件的内容写回到VATPRC Alias.txt文件
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(alias_content)
                print(f"更新内容为个人Alias到: {file_path}")

# 获取当前工作目录
root_folder = os.getcwd()
update_user(root_folder)
