import xlrd


# filepath=r"E:/Work/data/房屋结构(1).xlsx"

def readxls(filepath):

    codedValues = []

    data = xlrd.open_workbook(filepath, 'rb')
    # 拿到第一个sheet，这里你随意，如果有多个，可以拿到一个数组进行循环
    table = data.sheets()[0]
    # 循环读取每一行，跳过第一行
    for row in range(0, table.nrows):
        codevalue = {}
        # 取第一行的第一个单元格的值
        name = table.row(row)[2].value
        codevalue['name'] = name
        codevalue['code'] = name
        codedValues.append(codevalue)
        #print(name)
    print(codedValues)

if __name__ == "__main__":
    readxls("E:/Work/data/房屋结构(1).xlsx")
            
