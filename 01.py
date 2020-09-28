def fatorial(N):
    i = 0
    fat = N

    while True:
        if N ==0:
            fat = 1
            break
        else:
            i +=1
            fat *= i
            if i == (N-1):
                break
    return fat

def main():
    N = int(input())
    f = fatorial(N)
    print(f'{f}')

if __name__=='__main__':
    main()
