a=int(input("Enter a number :"))
prime=True
for i in range(2,a-1):
    if a%i == 0:
        prime=False
        break
if prime:
    print(f'{a} is a prime number ')
else:
    print(f'{a} is not a prime number')

