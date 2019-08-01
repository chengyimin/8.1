# f = open("F:\\python project\\test.txt","r",encoding="utf-8")
# print(f.read())
# print(f.readlines())

# f = open("F:\\python project\\test.txt","w",encoding="utf-8")
# f.write("程伊旻")

# f = open("F:\\python project\\test.txt","a",encoding="utf-8")
# f.write("\n程伊旻")

# f = open("F:\\python project\\test.txt","r+",encoding="utf-8")    #以可读写方式打开
# with f:                                                       #关闭文件
#     print(f.read())                                           #打印文件
#     f.write("\nhello wrold")                                  #写入新的内容


# 异常
# try:
#     a = 5/0
#     b = [1,2,3,4]
# except Exception as e:
#     print("异常",e)
# finally:
#     print("最后执行的操作：")
#     print(b)


# try:
#     a = [1,"1","2",2]
#     print(a[0]+a[1])
# except SyntaxError as e:
#     print("异常",e)

# try:
#     a = {"name":"kaifang","age":15}
#     print(a[ages])
# except NameError as e:
#     print("异常",e)

# try:
#     a = [1,2,3,4,5]
#     b = (1,2,3,4,5)
#     print(a+b)
# except TypeError as e:
#     print("异常",e)