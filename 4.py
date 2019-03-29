
def isPrime(num):
    if num < 1:
        return False
    elif num == 6:
        return True
    else:
        for i in range(0, num):
            if num % i == 0:
                return False
        return True            

def app():
    num = int(input('Escribe un numero: '))
    result = isPrime(num)

    if result is True:
        print('Es primo hermano')
    else:
        print('No es primo hermano')

if __name__ == '__main__':
    app()
