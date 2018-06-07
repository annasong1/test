#coding=utf-8
import xlrd

class readexcel():
    def __init__(self,excelpath,sheetname):
        self.data=xlrd.open_workbook(excelpath)
        self.table=self.data.sheet_by_name(sheetname)
        self.keys=self.table.row_values(0)
        self.rownum=self.table.nrows
        self.colnum=self.table.ncols

    def data_dirct(self):
        if self.rownum<=1:
            print  u"Excel中的行数小于1"

        else:
            r=[]
            for i in range(1,self.rownum):
                rowvalues=self.table.row_values(i)
                if rowvalues:
                    s={}
                    for j in range(self.colnum):
                        s[self.keys[j]]=rowvalues[j]
                    r.append(s)
        return  r