import tkinter as tk
from tkinter import ttk


def execute_steps():
    steps = steps_entry.get()
    continue_execution = continue_var.get()
    version = version_combobox.get()

    # 在这里执行你的逻辑，使用获取到的步数、是否继续和参数版本

    print(f"执行步数: {steps}")
    print(f"是否继续: {continue_execution}")
    print(f"参数版本: {version}")

    return steps, continue_execution, version


# 创建主窗口
root = tk.Tk()
root.title("执行页面")

# 步数输入框
steps_label = tk.Label(root, text="输入执行步数:")
steps_label.grid(row=0, column=0, padx=10, pady=10)
steps_entry = tk.Entry(root)
steps_entry.grid(row=0, column=1, padx=10, pady=10)

# 是否继续复选框
continue_var = tk.BooleanVar()
continue_checkbox = tk.Checkbutton(root, text="勾选是否继续", variable=continue_var)
continue_checkbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# 参数版本下拉框
version_label = tk.Label(root, text="选择参数版本:")
version_label.grid(row=2, column=0, padx=10, pady=10)
versions = ["Version 1", "Version 2", "basic"]
version_combobox = ttk.Combobox(root, values=versions)
version_combobox.grid(row=2, column=1, padx=10, pady=10)
version_combobox.set(versions[0])

# 执行按钮
execute_button = tk.Button(root, text="执行", command=execute_steps)
execute_button.grid(row=3, column=0, columnspan=2, pady=10)

# 启动主循环
root.mainloop()
