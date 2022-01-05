#!/usr/bin/python3
def main():
    import sys
    n = len(sys.argv)
    if n == 1:
        print("0 arguments.")
    else:
        print("{} {}:".format(n - 1, "argument" if n == 2 else "arguments"))
        for i in range(1, n):
            print("{}: {}".format(i, sys.argv[i]))
if __name__ == "__main__":
    main()
