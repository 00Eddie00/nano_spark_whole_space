import os
import re


def del_file(folder_path):
    filenames = os.listdir(folder_path)
    end = len(filenames)
    for i in range(end):
        last_filename = filenames[i]
        matches = re.findall(r'[0-9]', last_filename)
        # 将匹配的数字转换为整数或字符串
        current_step = int(''.join(matches))  # 如果需要提取的数字作为整数
        if current_step % 100 != 0:
            file_to_delete_path = os.path.join(folder_path, last_filename)
            os.remove(file_to_delete_path)
            print(f"删除文件: {folder_path}\\{last_filename}")


def del_basic_file():
    nano_species = ["Ca", "CaB", "CaF", "CaG"]
    open_species = ["Ca", "CaB", "CaF"]
    NANO = "NANO"
    OPEN = "OPEN"
    BASIC = "basic"
    dir_path = 'D:\\Projects\\SuYuTong\\DATA\\result'
    nano_basic_path = f'{dir_path}\\{NANO}_{BASIC}_parameter'
    open_basic_path = f'{dir_path}\\{OPEN}_{BASIC}_parameters'
    for species in nano_species:
        del_file(f"{nano_basic_path}\\{species}")
    for species in open_species:
        del_file(f"{open_basic_path}\\{species}")


def del_v1_file():
    nano_species = ["Ca", "CaB", "CaF", "CaG"]
    open_species = ["Ca", "CaB", "CaF"]
    NANO = "NANO"
    OPEN = "OPEN"
    V1 = "v1"
    dir_path = 'D:\\Projects\\SuYuTong\\DATA\\result'
    nano_v1_path = f'{dir_path}\\{NANO}_{V1}_parameter'
    open_v1_path = f'{dir_path}\\{OPEN}_{V1}_parameters'
    for species in nano_species:
        del_file(f"{nano_v1_path}\\{species}")
    for species in open_species:
        del_file(f"{open_v1_path}\\{species}")

def del_version_file(version):
    nano_species = ["Ca", "CaB", "CaF", "CaG"]
    open_species = ["Ca", "CaB", "CaF"]
    NANO = "NANO"
    OPEN = "OPEN"
    dir_path = 'D:\\Projects\\SuYuTong\\DATA\\result'
    nano_v2_path = f'{dir_path}\\{NANO}_{version}_parameter'
    open_v2_path = f'{dir_path}\\{OPEN}_{version}_parameters'
    for species in nano_species:
        del_file(f"{nano_v2_path}\\{species}")
    for species in open_species:
        del_file(f"{open_v2_path}\\{species}")


def main():
    del_basic_file()
    del_v1_file()


if __name__ == "__main__":
    main()
