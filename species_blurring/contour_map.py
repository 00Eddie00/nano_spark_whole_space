import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import os
from optical_blurring.concentration_matrix_generator_whole import cal_nano_concentration
from tool.cal_bcnl import cal_elements
from tool.tool_mkdir import *


def gen_contour(x_coords, y_coords, values, t, d, dirname):
    # 定义绘图范围
    xmin, xmax = min(x_coords), max(x_coords)
    ymin, ymax = min(y_coords), max(y_coords)
    # 创建一个新的坐标网格
    grid_x, grid_y = np.mgrid[xmin:xmax:1000j, ymin:ymax:1000j]
    # 使用原始数据进行插值
    grid_z = griddata((x_coords, y_coords), values, (grid_x, grid_y), method='cubic')
    # 绘制等高线图
    plt.figure(figsize=(8, 6))
    contour = plt.contourf(grid_x, grid_y, grid_z, cmap='viridis')
    plt.colorbar(contour, label='Concentration')
    plt.scatter(x_coords, y_coords, c=values, cmap='viridis', edgecolors='k')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Concentration Contour Map')
    plt.grid(True)
    plt.savefig(f"{dirname}/{d}_{t}ms.png")


def gen_line(values, relations, a_arr, b_arr, c_arr, nods, t, d, dirname):
    concentration = np.full(301)
    for i in range(301):
        concentration[i] = cal_nano_concentration(i, 0, values, relations, a_arr, b_arr, c_arr, nods)
    # 使用matplotlib绘制折线图
    plt.plot(concentration)
    # 添加标题和标签
    plt.title('Concentration Line Chart')
    plt.xlabel('X Coordinate')
    plt.ylabel('Concentration')
    plt.grid(True)
    plt.savefig(f"{dirname}/{d}_{t}ms.png")


def main():
    folder = "../result/nano_concentration_graph"
    name1 = f"{folder}/contour_map"
    name2 = f"{folder}/line_chart"
    mkdir(f"{name1}")
    mkdir(f"{name2}")
    time_interval = 2 * 10 ** -6 * 100 * 1000
    version = "basic"
    grid = np.loadtxt("../config/nano/4RYRgridt.dat")
    nods = np.loadtxt("../config/nano/4RYRnod.dat", dtype=int) - 1
    relations = np.load("../optical_blurring/relation/refined_relations.npy")
    single_area, control_area, near_triangle, index_in_triangle, nix_multiply_l, niy_multiply_l, a_arr, b_arr, c_arr, nmax, total_area = cal_elements(
        "../config/nano/4RYRgridt.dat", "../config/nano/4RYRnod.dat")
    dirnames = ["Ca", "CaF", "CaG"]
    time_list = [0, 10, 20, 30, 40, 50, 80]
    x_coords = grid[:, 0]
    y_coords = grid[:, 1]
    for d in dirnames:
        nano_path = f"D:\\Projects\\SuYuTong\\DATA\\result\\NANO_{version}_parameters"
        # 初始化各点Ca浓度
        nano_filenames = os.listdir(f"{nano_path}\\{d}")  # 纳米空间目前所有步数的浓度文件
        for t in time_list:
            step = int(t / time_interval)
            values = nano_filenames[step]
            gen_contour(x_coords, y_coords, values, t, d, name1)
            gen_line(values, relations, a_arr, b_arr, c_arr, nods, t, d, name2)


if __name__ == "__main__":
    # matplotlib.use('TkAgg')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    main()
