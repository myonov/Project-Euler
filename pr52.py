from __future__ import print_function

from pr10 import gen_primes

def main():
    limit = 1000000
    m = [2, 3, 4, 5, 6]

    for i in range(1, limit):
        multi = [set(str(i * j)) for j in m]
        if all(map(lambda x: x == set(str(i)), multi)):
            print(i)
            break

if __name__ == '__main__':
    main()
