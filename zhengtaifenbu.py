# 定义金字塔层数
num = 5

# 外层循环控制金字塔的层数
for i in range(1, num + 1):
    # 内层循环控制每层金字塔的空格和星号数量
    for j in range(1, num - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()
