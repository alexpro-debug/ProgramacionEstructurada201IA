if __name__ == '__main__':
    n = int(input().strip())
    
    # Si n es impar
    if n % 2 != 0:
        print("Weird")
    # Si n es par y está entre 2 y 5 (inclusivo)
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    # Si n es par y está entre 6 y 20 (inclusivo)
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    # Si n es par y es mayor a 20
    elif n % 2 == 0 and n > 20:
        print("Not Weird")