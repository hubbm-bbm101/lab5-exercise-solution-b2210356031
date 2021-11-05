N = int(input("Enter N value: "))
sum1 = 0
counter = 0
sum = 0
average = 0
for i in range(1 , N):
    if i%2 == 0:
        counter = counter + 1
        sum = sum + i

    else:
        sum1 = sum1 + i

average = sum / (counter)
print("Average of even numbers between the range given is: " , average)
print("Sum of odd numbers between the range given is: " , sum1)
