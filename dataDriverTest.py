from selenium import webdriver
import csv
#文件目录结构
path = "C:/Users/51Testing/PycharmProjects/Selenium120/data/member_info.csv"
#记录路径信息的三种方法
#打开文件,ctrl+鼠标左键,builtins.py文件被打开,执行,
file = open(path,'r')
#csv中的reader方法读取
table = csv.reader(file)
for item in table:
    print(item)