import requests


def get_weather_data():
    # 使用requests模块获取天气数据
    url = 'https://wttr.in/Chengdu?format=%C\n%t\n%T\n'
    r = requests.get(url)
    # 返回天气数据
    return r.text


# 实现冒泡排序
# 1. 从第一个元素开始，依次比较相邻的两个元素，如果前一个元素比后一个元素大，则交换两个元素的位置。
# 2. 重复上述步骤，直到最后一个元素。
# 3. 重复上述步骤，直到没有任何元素交换位置。
def bubble_sort(alist):
    # 外层循环控制比较的轮数
    n = len(alist)
    # 内层循环控制每轮比较的次数
    for j in range(n - 1):
        count = 0
        for i in range(0, n - 1 - j):
            # 如果前一个元素比后一个元素大，则交换两个元素的位置
            if alist[i] > alist[i + 1]:
                # 交换两个元素的位置
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                # 如果有元素交换位置，则count+1
                count += 1
                # 如果count=0，说明没有元素交换位置，说明列表已经有序，直接退出循环
        if 0 == count:
            break
            # 返回排序后的列表
    return alist


# 实现快速排序
def quick_sort(alist, start, end):
    # 递归的退出条件
    if start >= end:
        return
    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]
    # low为序列左边的由左向右移动的游标
    low = start
    # high为序列右边的由右向左移动的游标
    high = end
    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]
    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid
    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low - 1)
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low + 1, end)

# q: 1. 为什么要用到递归？
# a: 递归是一种解决问题的方法，它把一个问题分解为两个或更多的相同或相似的子问题，直到最后子问题可以简单的直接求解，原问题的解即子问题的解的合并。
#    递归的三个条件：
#    1. 一个问题的解可以分解为几个子问题的解
#    2. 这个问题与分解之后的子问题，除了数据规模不同，求解思路完全一样
#    3. 存在递归终止条件
#    递归的优点：
#    1. 代码的表达力很强
#    2. 递归代码的执行效率不高，因为递归会使用栈来保存临时变量，每一层递归都会增加一次函数调用的开销
#    3. 递归代码编写不容易调试
#    递归的缺点：
#    1. 递归代码的执行效率不高，因为递归会使用栈来保存临时变量，每一层递归都会增加一次函数调用的开销
#    2. 递归代码编写不容易调试
#    3. 递归代码占用内存比较多，因为每一次函数调用，都需要在内存栈中分配空间保存临时变量
#    4. 递归存在堆栈溢出的风险，因为每一次函数调用，都需要在内存栈中分配空间保存临时变量，如果递归层次太多，就有可能发生栈溢出
#    5. 递归存在重复计算的问题，因为存在大量的重复计算，比如斐波那契数列
#    6. 递归代码可读性差
#    递归的应用场景：
#    1. 问题的解可以分解为几个子问题的解
#    2. 这个问题与分解之后的子问题，除了数据规模不同，求解思路完全一样
#    3. 存在递归终止条件


if __name__ == '__main__':
    print(get_weather_data())
