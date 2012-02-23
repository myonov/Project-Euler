from __future__ import print_function

def count(n):

    digits = ['', 'one', 'two', 'three', 'four', 'five',
              'six', 'seven', 'eight', 'nine']
    decimals1 = ['ten', 'eleven', 'twelve' , 'thirteen', 'fourteen',
                 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    decimals2 = ['twenty', 'thirty', 'forty', 'fifty',
                 'sixty', 'seventy', 'eighty', 'ninety']
    hundred = 'hundred'
    thousand = 'thousand'


    if n < 10: return digits[n]
    if n < 20:
        q1 = n % 10
        return decimals1[q1]
    if n < 100:
        if n in range(20, 100, 10):
            return decimals2[n / 10 - 2]

        q1 = n / 10 - 2
        q2 = n % 10
        return decimals2[q1] + digits[q2]

    if n in range(100, 1000, 100):
        q1 = n / 100
        return digits[q1] + hundred

    if n < 1000:
        q1 = n / 100
        n1 = n - q1 * 100

        return count(q1) + 'hundred' + 'and' + count(n1)

    return 'one' + thousand

def main():
    s = 0
    for x in range(1, 1001):
        s += len(count(x))

    print(s)

if __name__ == '__main__':
    main()
