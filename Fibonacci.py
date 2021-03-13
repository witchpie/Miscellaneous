
Num1 = 0 
Num2 = 1
List = []
def Fib(count):

    global Num1
    global Num2
    global List

    Num3=Num1+Num2
    Num1=Num2
    Num2=Num3
    

    List.append(Num1)

    if count == 0:
        return print(List)
    count-=1
    print(count)
    Fib(count)


print(Fib(10))