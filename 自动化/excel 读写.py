import pandas as pd

class excel:

    def __init__(self,excel_file):
        self.excel_file = pd.read_excel(excel_file,encodeing="utf-8")
    def getdata(self,index):
        data = []
        # print(self.excel_file)
        data.append(self.excel_file.loc[index][0])
        data.append(self.excel_file.loc[index][1])


        return data[0],data[1]


if __name__ == '__main__':
    f =excel("./地址.xlsx")
    print(f.getdata(1))