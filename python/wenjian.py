import time

# f=open("study.txt","r",encoding="UTF-8")
# print(type(f))
# #t=f.read(5)
# #print(t)
# #d=f.read()
# #print(d)
# #lines=f.readlines()
# #print(lines)
# # line1=f.readline()
# # print(line1)
# # line2=f.readline()
# # print(line2)
# for line in f:
#     print(line,end="")
# time.sleep(10)
# f.close()
# with open("study.txt","r",encoding="UTF-8") as f:
#     for line in f:
#         print(line,end="")
# #已经关闭文件
# f=open("study.txt","w",encoding="UTF-8")
# f.write("hello world")
# f.flush()
# f.close()
f=open("study.txt","a",encoding="UTF-8")
f.write("hello world\n")
f.flush()
f.close()
