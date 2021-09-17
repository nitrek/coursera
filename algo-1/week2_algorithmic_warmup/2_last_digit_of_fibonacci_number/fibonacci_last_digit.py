# Uses python3
from datetime import datetime
steps = 0
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


def calc_fib(n):
    global steps
    if (n <= 1):
        steps = steps + 1
        #if(steps % 1000 == 0):
        #    print(steps)
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

dp_lastdigit = {}
#dp_lastdigit[0] = 0
for i in range(0,60):
    dp_lastdigit[i] = calc_fib_dp(i)
n = int(input())
#start_time = datetime.now()
print(dp_lastdigit[n%60]%10)
#print(steps_dp)
#print("time")
#print(datetime.now() - start_time)
# start_time = datetime.now()
# print(calc_fib(n))
# print(steps)
# print("time")
# print(datetime.now() - start_time)
