import sys


def main():
    a = [1,2,3,4,5,6,7,8,9]
    b = [0,1,2,-3,-4]
    c = (1,10,100,10,1000)
    d = "abrakadabra"
    e = {
        "MS": "605 978 567",
        "BK": "987 654 345"
    }
    f = { "MS", "MSA", "O", "OO" }
    print(a[1::].append(b))
    print(-10 in c)
    print(len(d) + len(b))
    print(d * 2)
    print(list(e.keys()))
    print(min(f))
    return 0


if __name__ == '__main__':
    sys.exit(main())
