import pandas as pd

class excel:

    def __init__(self,excel_file,commodity_name):
        self.excel_file = pd.read_excel(excel_file,encodeing="utf-8")
        self.commodity_name = commodity_name
    def getdata(self,index):
        data = []
        # print(self.excel_file)
        data.append(self.excel_file.loc[index][0])
        data.append(self.excel_file.loc[index][1])
        print("当前序号======",index,'\n')
        return data[0],self.commodity_name+data[1]


if __name__ == '__main__':
    f =excel("./地址.xlsx",'北京鲜花')
    print(f.getdata(1))