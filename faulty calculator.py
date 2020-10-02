# make an claculator and print the outpu as"(2+3=100)" and (2-4=777)
print("enter the number")
n = int(input())
print("enter the second number")
m = int(input())
print("enter the operator + _ * ?")
opt = input()
if n == 2 and  m == 3 and opt == "+" :
    print("100")
elif n == 2 and m == 4 and opt == "-" :
    print("777")
elif opt == "+" :
    print(n+m)
elif opt == "-" :
    print(n-m)
elif opt == "*" :
    print(n*m)
else:
    print(n/m)
