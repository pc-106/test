# try:
#     f=open("abc.txt","r",encoding="UTF-8")
# except FileNotFoundError:
#     print("文件不存在")
#     f=open("abc.txt","w",encoding="UTF-8")
# else:
#     print("文件打开成功")
# finally:
#     f.close()
# try:
#     print(name)
# except NameError as e:
#     print("变量name未定义")
#     print(e)
# try:
#     print(10/0)
# except (NameError,ZeroDivisionError) as e:
#     print("变量name未定义或除数为0")
#     print(e)
# try:
#     print(10+2)
# except Exception as e:
#     print("变量name未定义或除数为0")
#     print(e)
# else:
#     print("程序正常运行")
# finally:
#     print("程序结束")
def fun1():
    print("fun1开始执行")
    num=100/0
    print("fun1结束执行")
def fun2():
    print("fun2开始执行")
    fun1()
    print("fun2结束执行")
try:
    fun2()
except Exception as e:
    print("程序异常")
    print(e)
else:
    print("程序正常运行")
finally:
    print("程序结束")