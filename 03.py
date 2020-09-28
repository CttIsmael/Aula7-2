def somatorio():
    n = int(input())
    i = 1
    H = 1

    while i <n:
        i+=1
        H += (1/i)
        if i ==n:
            break
    print(f'{H:.4f}')
def main():
    somatorio()

if __name__=='__main__':
    main()
