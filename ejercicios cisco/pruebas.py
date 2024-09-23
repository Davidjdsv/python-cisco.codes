try:    
    value = input("Ingresa un valor: ")
    print(value/value)
except ValueError:    
    print("Entrada incorrecta...")
except ZeroDivisionError:    
    print("Entrada err%C3%B3nea...")
except TypeError:    
    print("Entrada muy err%C3%B3nea...")
except:    
    print("%C2%A1Buuu!")