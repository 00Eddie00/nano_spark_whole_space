import numpy as np
from tool.tool_mkdir import *
import re


def gen_cag(version):
    dir_name = "D:\\Projects\\SuYuTong\\DATA\\result"
    mkdir(f"{dir_name}/OPEN_{version}_parameters/CaG")
    dir_nano = f"NANO_{version}_parameters\\"
    # 初始化各点Ca浓度
    filenames = os.listdir(f"{dir_name}\\{dir_nano}CaG\\")  # 目前所有步数的浓度文件

    open_grid_coordinates = np.loadtxt("../config/open/open_grid_coordinates.csv", delimiter=",")  # 点坐标
    # 点个数
    point_count = len(open_grid_coordinates)
    # 开放空间中无该染料，但设置为0
    open_cag = np.full(point_count, 0.0)

    for i in range(len(filenames)):
        open_cag_filename = filenames[i]
        filename = f"{dir_name}\\{dir_nano}CaG\\{open_cag_filename}"
        np.savetxt(filename, open_cag)

    last_filename = filenames[-1]
    matches = re.findall(r'[0-9]', last_filename)
    # 将匹配的数字转换为整数或字符串
    length = int(''.join(matches))  # 如果需要提取的数字作为整数

    print(len(filenames))


def main():
    version = "basic"
    gen_cag(version)


if __name__ == '__main__':
    main()
