# 有序可變數列表 List
# data=[[3,4,5],[6,7,8]]
# data[0][0:2]=
# print(data[0][1])
# 有序不可變動列表
# 四則運算
n1=int(input("請輸入數字一"))
n2=int(input("請輸入數字二"))
op=input("請輸入運算: +,-,*,/: ")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援的運算")