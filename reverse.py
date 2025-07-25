num=[]
for i in range (5):
    num.append (int(input("enter a number")))
print("first:",num[0])
print("last:",num[-1])
print("all elemnts:")
for n in num:
        print(n)
num.reverse()
print("reversed list:",num)