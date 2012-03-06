from __future__ import print_function
from itertools import product
from string import letters

def main():
    common_words = [
        'the', 'a', 'and', 'to', 'of', 'that', 'on', 'at', 'this',
    ]

    bound = 7

    text = map(int, open('cipher1.txt', 'r').read().strip().split(','))

    let = [ord(x) for x in letters[:26]]

    for p in product(let, repeat=3):
        new_text = ''.join([
            chr(x ^ p[i%3]) for i, x in enumerate(text)
        ])

        oc = sum([x in new_text.lower() for x in common_words])
        if oc > bound:
            print(new_text)
            print(sum([ord(x) for x in new_text]))

if __name__ == '__main__':
    main()
