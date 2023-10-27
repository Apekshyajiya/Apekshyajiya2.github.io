print("Find perfect nos with me!")
#a perfect no is one where the sum of its divisors gives the number itself, 6=1+2+3
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
def main():
    i =2
    result =0
    for i in range(1000):
        result = perfect_number(i)
        if(result == True):
            print(i)
main()

