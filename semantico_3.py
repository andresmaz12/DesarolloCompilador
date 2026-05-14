from AST_EXT import *

class Simbolo:
    pass

class TablaSimbolos:
    def __init__(self):
        self.ambitos = [{}]
        self.stack_offset = 0 #

    def declarar_variable(self, nombre, tipo):
        #Cada variable int/float ocupa 4 bytes
        self.stack_offset -= 4
        nuevo_simbolo = Simbolo(tipo, self.stack_offset)
        self.ambitos[-1][nombre] = nuevo_simbolo
        return self.stack_offset
    
    def generar_funcion(nodo):
        print(f"{nodo.nombre}: ")
        #Prolog
        print("     push ebp")      # Guardar el ebp del llamador
        print("     mov ebp,  esp") # Establecer el nuevo ebp 

        #Aquí calculamos el espacio total necesario 
        #Esto se obtien de la suma de variables en todos los ambitso del NodoFuncion
        print("     sub esp, 16")

        # CUERPO
        # . . . generar instrucciones . . .

        # EPÍLOGO
        print("     mov esp, ebp") # Deshace el espacio de la pila 
        print("     pop ebp")      # Restaura el ebp anterior
        print("     ret")