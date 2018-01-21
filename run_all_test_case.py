#这个python文件专门用来 执行所有的测试用例
import unittest
#如果这个文件不是最初的启动文件,那么代码快中的语句不能执行
if __name__=='__main__':
    # 1 找到所有符合条件的测试用例
    #那里的文件,那些文件(文件名有特殊格式), 遍历到几级子目录
    testcases = unittest.defaultTestLoader.discover(".",pattern='*Test.py')
    # 2 执行这些测试用例
    unittest.TextTestRunner().run(testcases)