# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm_euclid(a,b):
    if(a == 0):
        return b
    if(b == 0):
        return a
    return lcm_euclid(b,a%b)

def gcd_euclid(a,b):
    if(a == 0):
        return b
    if(b == 0):
        return a
    return gcd_euclid(b,a%b)

if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    #print(lcm_naive(a, b))
    print(int((a*b)/gcd_euclid(a,b)))

