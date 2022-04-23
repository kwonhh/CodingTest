
def fibo(n):
    if n < 3:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

if __name__ == '__main__':
    for n in range(1,11):
        print("fibonacci f(",n, ") = ", fibo(n))
