import xlwt
import random

# 创建一个workbook对象，相当于创建一个Excel文件
workbook = xlwt.Workbook(encoding='utf-8')

# 创建一个sheet对象，相当于创建一个sheet页
sheet = workbook.add_sheet('Sheet1')

# 写入表头
sheet.write(0, 0, '姓名')
sheet.write(0, 1, '身份证号')
sheet.write(0, 2, '年龄')
sheet.write(0, 3, '性别')
sheet.write(0, 4, '手机号')

# 写入数据
sheet.write(1, 0, '张三')
sheet.write(1, 1, '123456789012345678')
sheet.write(1, 2, '20')
sheet.write(1, 3, '男')
sheet.write(1, 4, '12345678901')

# 写入20条随机数据
for i in range(2, 30):
    sheet.write(i, 0, f'姓名{i}')
    sheet.write(i, 1, f'{random.randint(100000000000000000, 999999999999999999)}')
    sheet.write(i, 2, f'{random.randint(18, 60)}')
    sheet.write(i, 3, random.choice(['男', '女']))
    sheet.write(i, 4, f'{random.randint(10000000000, 99999999999)}')

# 保存文件
workbook.save('example.xls')
