from __future__ import print_function

def is_leap(y):
    if y % 100 == 0 and y % 400 != 0: return False
    return y % 4 == 0

def main():
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mnames = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 
              'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    curr_wd = 1 #monday; sunday is 0

    r = 0

    for y in range(1900, 2001):
        for m in range(0, 12):
            days = months[m] + (m == 1 and is_leap(y))
            curr_wd += days
            curr_wd %= 7

            if y == 2000 and m == 11: break
            if curr_wd % 7 == 0:
                if y > 1900:
                    r += 1

    print(r)

if __name__ == '__main__':
    main()
