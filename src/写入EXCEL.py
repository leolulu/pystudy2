import xlwt

workbook = xlwt.Workbook()

sheet1 = workbook.add_sheet('一个shit')

sheet1.write(0,0,label = 'sjot')

workbook.save('./1.xlsx')