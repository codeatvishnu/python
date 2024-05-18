def fact(n):
    output = 1
    for i in range(1,n+1):
        output = output * i
    return output


num = int(input("Enter the positive number: "))
print(fact(num))