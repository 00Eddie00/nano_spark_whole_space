from tool.tool_mkdir import *
import shutil


def main():
    version1 = "basic_(GCaMP6f_T=1)"
    version001 = "basic"
    nano_path1 = f"D:\\Projects\\SuYuTong\\DATA\\result\\NANO_{version1}_parameters"
    open_path1 = f"D:\\Projects\\SuYuTong\\DATA\\result\\OPEN_{version1}_parameters"
    nano_path001 = f"D:\\Projects\\SuYuTong\\DATA\\result\\NANO_{version001}_parameters"
    open_path001 = f"D:\\Projects\\SuYuTong\\DATA\\result\\OPEN_{version001}_parameters"
    temp = "D:\\Projects\\SuYuTong\\DATA\\result\\TEMP"

    dirnames = ["CaF"]
    time_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    # time_list = [0]
    for d in dirnames:
        # 初始化各点Ca浓度
        nano_filenames1 = os.listdir(f"{nano_path1}\\{d}")  # 纳米空间目前所有步数的浓度文件
        open_filenames1 = os.listdir(f"{open_path1}\\{d}")  # 开放空间目前所有步数的浓度文件
        nano_filenames001 = os.listdir(f"{nano_path001}\\{d}")  # 纳米空间目前所有步数的浓度文件
        open_filenames001 = os.listdir(f"{open_path001}\\{d}")  # 开放空间目前所有步数的浓度文件
        mkdir(f"{temp}\\{version1}\\NANO\\{d}")
        mkdir(f"{temp}\\{version001}\\NANO\\{d}")
        mkdir(f"{temp}\\{version1}\\OPEN\\{d}")
        mkdir(f"{temp}\\{version001}\\OPEN\\{d}")
        for t in time_list:
            print(f"{d}_{t}ms开始")
            step = int(t) * 5
            nano_file1 = nano_filenames1[step]
            open_file1 = open_filenames1[step]

            nano_file001 = nano_filenames001[step]
            open_file001 = open_filenames001[step]

            nano_original_concentration1 = f"{nano_path1}\\{d}\\{nano_file1}"  # 替换为你的源文件路径
            open_original_concentration1 = f"{open_path1}\\{d}\\{open_file1}"
            nano_original_concentration001 = f"{nano_path001}\\{d}\\{nano_file001}"
            open_original_concentration001 = f"{open_path001}\\{d}\\{open_file001}"

            # 将文件复制到指定位置
            shutil.copy(nano_original_concentration1, f"{temp}\\{version1}\\NANO\\{d}")
            shutil.copy(open_original_concentration1, f"{temp}\\{version1}\\OPEN\\{d}")
            shutil.copy(nano_original_concentration001, f"{temp}\\{version001}\\NANO\\{d}")
            shutil.copy(open_original_concentration001, f"{temp}\\{version001}\\OPEN\\{d}")


if __name__ == "__main__":
    main()
