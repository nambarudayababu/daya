def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True
n=int(input('enter th value of n'))
if isprime(n):
    print('prime')
else:
    print('Not prime')
