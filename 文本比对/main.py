# This is a sample Python script.
#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Sh ift to search everywhere for classes, files, tool windows, actions, and settings.
import  difflib as diff


def Textcompare():
   #  text1 = ''' 有时候我们要对比两份配置文件是不是一样，
   #  或者比较两个文本是否异样，可以使用linux命令行工具diff a_file b_file，
   #  但是输出的结果读起来不是很友好。
   #  这时候使用python的标准库difflib就能满足我们的需求。
   # '''.splitlines(keepends=True)
   #  text2 = '''  有时候我们要对比两份配置文件是不是一样，
   #  或者比较两个文本是否异5样，可以使6用linux命令行工具diff a_file b_file，
   #  但是输出的结果读起来不是很友好。
   #  这时候使用python的标准库difflib就能满7足我们的需求。
   #  '''.splitlines(keepends=True)
    text1=''
    text2=''
    html=''
    with open("./管理条例-原始.txt",'r',encoding='utf-8') as f1,open("./管理条例-新的.txt",'r',encoding='utf-8') as f2:
        text1 = f1.readlines()
        text2 = f2.readlines()

    d = diff.HtmlDiff()
    with  open("index.html",'w',encoding='utf-8') as html:
        HtmlContext = d.make_file(text1, text2)
        html.write(HtmlContext)

    print(text1)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    Textcompare()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
