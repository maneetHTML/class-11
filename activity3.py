num = int(input("Enter a 3 digit number :"))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit **3
    temp //= 10
if num ==sum :
    print("it is a armstrong number")
else:
    print("it is not a armstrong number")