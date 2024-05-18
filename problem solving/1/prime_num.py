# to check whether the given number is palindrome or not

def prime_number(num):
    for i in range(2,num):
        if num%i==0 :
            return " not an prime number"
        else :
            return " prime numbers"



num=int(input("Enter the number: "))
print(prime_number(num))