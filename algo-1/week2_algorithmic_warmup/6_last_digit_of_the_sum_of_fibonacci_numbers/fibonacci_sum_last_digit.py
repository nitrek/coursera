# Uses python3
import sys


def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1

# Uses python3
# Given two integers n and m, output Fn mod m (that is, the remainder of Fn when divided by m
def Huge_Fib(n,m):

    # Initialize a matrix [[1,1],[1,0]]
    v1, v2, v3 = 1, 1, 0
    # Perform fast exponentiation of the matrix (quickly raise it to the nth power)
    for rec in bin(n)[3:]:
        calc = (v2*v2) % m
        v1, v2, v3 = (v1*v1+calc) % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
        if rec == '1': v1, v2, v3 = (v1+v2) % m, v1, v2
    return v2;

def fibosum(n):
    sum = 0
    for i in range(0,n):
        #print("s"+str(i))
        sum = sum + Huge_Fib(i+1,10)
        sum = sum%10
    return sum

if __name__ == '__main__':
    input = input()
    n = int(input)
    #from datetime import datetime
    #start_time = datetime.now()
    # sys.setrecursionlimit(1500)
    # print(sys.getrecursionlimit())
    # sys.getrecursionlimit
    # n = 12
    # m = 5
    rem = n % 60
    print(fibosum(rem))
    #print(datetime.now() - start_time)
