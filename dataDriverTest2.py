import csv

import os
#__file__双下划线开头,双下划线结尾的变量,是python内置变量,表示当前文件,这个变量写在哪个文件中,
#就代表那个文件本身,这时候 path ==C:\Users\51Testing\PycharmProjects\Selenium120\
# path = os.path.dirname(__file__)
# print(path)
# final_path = path + "/data/member_info.csv"
# print(final_path)
#好处 保证项目在任意路经下都可以执行
#公用的代码应该封装成一个独立的方法
def readData():
    path = os.path.dirname(__file__)
    final_path = path + "/data/member_info.csv"
    #查看源代码,ctrl+鼠标左键
    #file = open(final_path,'r')
    #声明一个空的列表,table中的数据保存到列表中,最后返回列表
    result = []
    with open(final_path,'r') as file:
        table = csv.reader(file)
        #需要返回值
        for item in table:
            #print(item)
            result.append(item)
        #file.close()
        return result


abcd = readData()
print(abcd)
print(abcd[0][0])