num = 11
count = 0
for i in range(1,num+1):
    if num % i == 0:
        count = count + 1
if count == num:
    print("prime number:")
else:
    print("not prime number:")
