import openpyxl


def getExcel():

    # 打开表
    workbook = openpyxl.load_workbook('excel_case/api_case_V1.xlsx')
    list2 = []
    # 选择工作表
    sheet = workbook['Sheet1']

    # 取值,values是按列取值，iter_cols()是按行
    for item in sheet.values:
        # 不需要表头，规律‘id’字符串 1 数字 数据类型判断 type（变量名）
        if type(item[0]) is int:
            # 把需要的数据拿出来，元组改成列表

            list1 = []
            for col in item:
                list1.append(col)
            list2.append(list1)
    # print(list2)
    return list2
# getExcel()