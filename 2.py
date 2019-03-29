
def esprimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

def app():
    num = int(input('Escribe un numero: '))
    result = esprimo(num)

if __name__ == '__mein__':
    app()
