# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast(numbers):
    n = len(numbers)
    max_1 = 0
    max_2 = 0
    for first in range(n):
        if numbers[first] > max_1:
            max_2 = max_1
            max_1 = numbers[first]
        elif numbers[first] > max_2:
            max_2 = numbers[first]
        #print (max_1,max_2)
    return max_1*max_2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    #input_numbers = [7,5,14,2,8,8,10,1,2,3]
    input_numbers = [1, 2,3,4,5,6,7,8,9,10,11]
    print(max_pairwise_product(input_numbers))
