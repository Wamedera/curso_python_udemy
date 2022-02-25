def fatorial(n, fat=1):
    fat *= n
    return fat if n == 1 else fatorial(n - 1, fat)


if __name__ == '__main__':
    print(f'10! = {fatorial(10)}')
