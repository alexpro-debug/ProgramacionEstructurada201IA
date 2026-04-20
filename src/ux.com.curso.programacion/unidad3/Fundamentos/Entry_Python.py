def pregunta_1():
    print(2**3**2)

def pregunta_2():
    x = 10/2
    print(type(x))

def pregunta_3():
    x = 1 
    X = x
    x == x
    print(x)

"""
orden de las operaciones primero ejecuta la // y da resulatado entero y no con decimales
"""
def pregunta_4():
    print(1 // 2 * 3)

def pregunta_5():
    y = 2 + 3 * 5
    print(y)

"""
contenacion de cadenas
"""
def pregunta_6():
    a = '1'
    b = '2'
    print(a + b)

def pregunta_7():
    z = 11 % 3
    print(z)

def pregunta_8():
    x = 5
    y = 2
    print(x//y)

def pregunta_9():
    val = 10
    val += 5*2
    #diferente representacion mismo resultado
    v = 10
    v = v+5*2
    print(v)

"""
bool("") es false porque una cadena vacia se considera false"""
def pregunta_10():
    print(bool(""), bool(" "), bool(0), bool(0.00))


def main():
    pregunta_1()
    pregunta_2()
    pregunta_3()
    pregunta_4()
    pregunta_5()
    pregunta_6()
    pregunta_7()
    pregunta_8()
    pregunta_9()
    pregunta_10()

if __name__ == "__main__":
    main()