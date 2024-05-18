def manipulation(lists):
    even = []
    for i in lists:
        if i%2==0:
            even.append(i)
    return even

n=[4,6,3,4,7,8,2,9]
print("The even numbers are", manipulation(n))