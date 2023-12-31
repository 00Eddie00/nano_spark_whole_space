import numpy as np

# 时间相关，单位：秒
DT = 2 * 10 ** -6  # DT 时间间隔
RELEASE_TIME = 0.02  # 释放时间，即到此刻RYR通道关闭
STOP_TIME = 0.1  # 结束时间

# 出入流点属性值
B_INNER = 0  # 内部
B_INFLOW = 2  # 入流
B_OUTFLOW = 4  # 出流

# 出入流参数
INITIAL_C_CA = 0.0001  # 肌质中钙离子初始浓度 mM
D_CA = 3.5 * 10 ** 8  # 自由钙离子的扩散系数
D_F = 2 * 10 ** 7  # 染料的扩散系数
S = 2 * np.pi * 0.5 * 15  # ryr通道表面积
K_RYR = 1.24368 * 10 ** 10 / S  # ryr通道处钙离子释放的扩散系数
Delta_r = 5.0

# C_CA_OUT = 0.0001
C_CA_OUT = 1.0
C_CAF_OUT = 1 / 245
CA_JSR = 1.0  # jSR中的钙离子浓度

#  Fluo-3
K_F3_PLUS = 80000
# K_F3_MINUS = 90
K_F3_MINUS = 57.6
F3_T = 0.05
D_CAF = 2 * 10 ** 7   # 染料的扩散系数

# GCaMP6f
K_GCaMP6f_PLUS = 27000
K_GCaMP6f_MINUS = 17
GCaMP6f_T = 0.01

# # 缓冲物（基本情况）basic小空间大空间都有
# # Calmodulin
# K_Calmodulin_PLUS = 100000
# K_Calmodulin_MINUS = 31
# Calmodulin_T = 0.036
# # Troponin C
# K_TroponinC_PLUS = 125000
# K_TroponinC_MINUS = 250
# TroponinC_T = 0.07
# # SR membrane
# K_SR_PLUS = 115000
# K_SR_MINUS = 100
# SR_T = 0.047
# # SL membrane
# K_SL_PLUS = 115000
# K_SL_MINUS = 1000
# SL_T = 1.124

# # 缓冲物（情况一）暂时没跑过
# # Calmodulin
# K_Calmodulin_PLUS = 100000
# K_Calmodulin_MINUS = 38
# Calmodulin_T = 0.024
# # Troponin C
# K_TroponinC_PLUS = 39000
# K_TroponinC_MINUS = 20
# TroponinC_T = 0.07
# # SR membrane
# K_SR_PLUS = 7692.307
# K_SR_MINUS = 100
# SR_T = 13
# # SL membrane
# K_SL_PLUS = 909.0909
# K_SL_MINUS = 1000
# SL_T = 165


# 缓冲物（基本情况）v1 Calmodulin Troponin C只在大空间有，SR SL只在小空间有
# Calmodulin
# K_Calmodulin_PLUS = 100000
# K_Calmodulin_MINUS = 31
# Calmodulin_T = 0.036
# # Troponin C
# K_TroponinC_PLUS = 125000
# K_TroponinC_MINUS = 250
# TroponinC_T = 0.07
# # SR membrane 之后只有小空间有
# K_SR_PLUS = 7692.307
# K_SR_MINUS = 100
# SR_T = 13
# # SL membrane
# K_SL_PLUS = 909.0909
# K_SL_MINUS = 1000
# SL_T = 165

# 缓冲物（基本情况）v2.1
# 只调 SR_T = 1.3
# # Calmodulin
# K_Calmodulin_PLUS = 100000
# K_Calmodulin_MINUS = 31
# Calmodulin_T = 0.036
# # Troponin C
# K_TroponinC_PLUS = 125000
# K_TroponinC_MINUS = 250
# TroponinC_T = 0.07
# # SR membrane
# K_SR_PLUS = 7692.307
# K_SR_MINUS = 100
# SR_T = 1.3
# # SL membrane
# K_SL_PLUS = 909.0909
# K_SL_MINUS = 1000
# SL_T = 165

# # 缓冲物（基本情况）v2.2
# # 只调 TOTAL_SLM = 16.5
# # Calmodulin
# K_Calmodulin_PLUS = 100000
# K_Calmodulin_MINUS = 31
# Calmodulin_T = 0.036
# # Troponin C
# K_TroponinC_PLUS = 125000
# K_TroponinC_MINUS = 250
# TroponinC_T = 0.07
# # SR membrane
# K_SR_PLUS = 7692.307
# K_SR_MINUS = 100
# SR_T = 13
# # SL membrane
# K_SL_PLUS = 909.0909
# K_SL_MINUS = 1000
# SL_T = 16.5

# 缓冲物（基本情况）v2.3
# 只调 SL_T = 16.5 SR_T = 1.3
# Calmodulin
K_Calmodulin_PLUS = 100000
K_Calmodulin_MINUS = 31
Calmodulin_T = 0.036
# Troponin C
K_TroponinC_PLUS = 125000
K_TroponinC_MINUS = 250
TroponinC_T = 0.07
# SR membrane
K_SR_PLUS = 7692.307
K_SR_MINUS = 100
SR_T = 1.3
# SL membrane
K_SL_PLUS = 909.0909
K_SL_MINUS = 1000
SL_T = 16.5

# 网格参数
nano_grid_file_name = "../config/nano/4RYRgridt.dat"
nod_file_name = "../config/nano/4RYRnod.dat"
npoch_file_name = "../config/nano/4RYRnpoch.dat"
npoch = np.loadtxt(npoch_file_name, dtype=int)
grid = np.loadtxt(nano_grid_file_name, dtype=np.float64)
nod = np.loadtxt(nod_file_name, dtype=int) - 1
NE = len(nod)
NP = len(grid)
