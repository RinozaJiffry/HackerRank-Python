## The provided code stub reads and integer,n , from STDIN. For all non-negative integers i < n, print i^2.

## Sample Input 0
# 5

## Sample Output 0
# 0
# 1
# 4
# 9
# 16

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i);
