def eh_primo(n):
    inicio = 1
    divisor = 0
    
    while inicio<= n:
        if n % inicio == 0:
            divisor +=1
        inicio +=1
    return divisor
        
def main():
    n =int(input())
    d = eh_primo(n)

    if d ==2:
        print('True')
    else:
        print('False')
        
if __name__ == '__main__':
    main()
