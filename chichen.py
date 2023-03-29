def fa1(h, f):  # 设鸡c只 兔r只
    if h > 0 and f > 0 and h % 2 == 0 and f % 2 == 0:
        r = f / 2 - h
        c = h - r
        print("鸡有", c, "只，兔有", r, "只")
    else:
        print("输入错误！")


fa1(8, 20)
