#fizzbuzz means we need to print the number from 1 to 100 sequencly,
# but print fizz for numbers multiple of 3 instead number,
# and buzz for numbers multiple of 5 ,and fizzbuzz for multiple of both 3 and 5


num=100
for i in range(1,num+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz!")
    elif i%3==0:
        print("Fizz!")
    elif i%5==0:
        print("Buzz!")

    else:
        print(i)