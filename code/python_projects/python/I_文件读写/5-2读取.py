from openpyxl import load_workbook

# 打开文件 read_only=False 可读写
wb = load_workbook("result.xlsx")
ws = wb["测试数据"]

# 读取单个单元格
print(ws["A1"].value)

# 遍历所有行
for row in ws.iter_rows(values_only=True):
    print(row)

    # 打开excel文件
wb = load_workbook("测试日志.xlsx")
# 1. 获取所有工作表名称列表
sheet_names = wb.sheetnames
print("所有表名：", sheet_names)
# 2. 遍历所有工作表对象
for sheet_name in wb.sheetnames:
    ws = wb[sheet_name]
    print(f"当前工作表：{sheet_name}")
    # 可对ws做读取单元格操作
    # print(ws['A1'].value)

# 3. 另一种遍历方式 wb.worksheets
for ws in wb.worksheets:
    print("工作表名称：", ws.title)
    # 读取所有内容，打印内容
    for row in ws.iter_rows(values_only=True):
        print(row)
    # 读取所有内容，打印序号和内容
    for row in ws.iter_rows(values_only=True):
        for r in row:
            print(r.coordinate, r.value)

            '''读取原有数据并新增一行'''
from openpyxl import load_workbook
wb = load_workbook("result.xlsx")
ws = wb.active
ws.append(["guest", 404])
wb.save("result.xlsx")