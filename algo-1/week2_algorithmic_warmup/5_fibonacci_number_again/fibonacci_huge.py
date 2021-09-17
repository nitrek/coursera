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

dp = {}
steps_dp =0

def calc_fib_dp(n):
    global steps_dp
    global dp
    #print (n)
    if (n <= 1):
        steps_dp = steps_dp + 1
        return n
    if ((n - 1) not in dp.keys()):
        dp[n - 1] = calc_fib_dp(n - 1)
    if ((n-2) not in dp.keys()):
        dp[n - 2] = calc_fib_dp(n - 2)
    steps_dp = steps_dp + 1
    return dp[n - 1] + dp[n - 2]

def fibonacciModulo(n, m):
    # Getting the period
    pisano_period = pisanoPeriod(m)
    #print(pisano_period)
    # Taking mod of N with
    # period length
    n = n % pisano_period
    #print(n)
    return Huge_Fib(n,m)

def fibonacciModulo2(n, m):
    # Getting the period
    pisano_period = pisanoPeriod(m)
    #print(pisano_period)
    # Taking mod of N with
    # period length
    n = n % pisano_period
    #print(n)
    return calc_fib_dp(n)%m

if __name__ == '__main__':
    input = input()
    n, m = map(int, input.split())
    #from datetime import datetime
    #start_time = datetime.now()
    # sys.setrecursionlimit(1500)
    # print(sys.getrecursionlimit())
    # sys.getrecursionlimit
    # n = 12
    # m = 5
    if(m>2):
        print(fibonacciModulo(n, m))
    else:
        print(fibonacciModulo2(n, m))
    #print(datetime.now() - start_time)
