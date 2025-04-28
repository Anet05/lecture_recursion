def recursive_nth_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)



def main():
    n = int(input("Pořadí členu: "))
    seq = [recursive_nth_fibo(num) for num in range(n+1)]
    print(seq)
    print(recursive_nth_fibo(n))
    pass


if __name__ == "__main__":
    main()
