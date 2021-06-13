a = int(input("Please enter a positive integer"))
b = int(input("Please enter a positive integer"))
aDivisors = set()
bDivisors = set()
for x in range(1, a+1):
    if a % x == 0:
        aDivisors.add(x)
for x in range(1, b+1):
    if b % x == 0:
        bDivisors.add(x)
commonDivisors = aDivisors.intersection(bDivisors)
commonDivisorsArray = list(commonDivisors)
print("Your greatest common divisor is:", commonDivisorsArray[-1])
