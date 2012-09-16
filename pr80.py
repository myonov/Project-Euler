from decimal import localcontext, Decimal

def main():
    a = 0
    b = set(i*i for i in range(11))

    with localcontext() as w:
        w.prec = 110
        for i in range(1, 100):
            if i not in b:
                d = str(Decimal(i) ** Decimal('0.5'))
                ind = d.index('.') + 1
                a += sum(map(int, d[0:ind-1]+d[ind:ind+99]))
        print(a)

if __name__ == '__main__':
    main()