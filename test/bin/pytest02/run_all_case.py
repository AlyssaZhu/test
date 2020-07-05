import pytest

'''
1.   测试文件test_开头（_test 结尾也可以）
2.   测试类以Test开头，并且不能带有init方法
3.   测试函数以test开头
4.   断言使用基本的assert即可
'''
'''
1. 生成html报告
   '--html=../report/report.html'
2. 生成xml报告
       '--junitxml=../report/report.xml'
3. 生成allure报告 （持续集成的报告样式）
        1. 生成allure结果目录，json格式
                '--alluredir','../report/reportallure'
        2. 生成allure报告
                1. 下载allure安装包 :brew install allure
                2. 解压安装包 
                3. 配置环境变量（bin目录）
                4. 进入report目录
                5. 运行命令：
                   allure generate ./reportallure/ -o ./reporthml/ --clean
                6. 查看报告 index.html   

'''
#如何运行测试用例
#单个文件运行，运行添加，对应的文件地址，地址要用相对路径。
#多个文件运行，对应添加多个文件的路径，列表的形式添加多个文件路径
if __name__ == '__main__':
        #pytest.main(['test_case.py','test_case02.py'])
#运行整个目录，当前目录：./ ,其它 ../pytest02

        pytest.main(['./','--html=../report/report.html','--junitxml=../report/report.xml','--alluredir','../report/reportallure'])
        print('运行当前目录')



