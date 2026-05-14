from AST_EXT import *

class Simbolo:
    pass

class TablaSimbolos:
    def __init__(self):
        self.ambitos = [{}]
        self.stack_offset = 0 #
        self.offste_actual = 0

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

    def calcular_espacio_total(self, nodo):
        """
        Recorre el AST de una función para calcular el tamaño total 
        necesario en el Stack Frame (en bytes)
        """
        espacio = 0
        
        #Si es una lista de instrucciones como el cuerpo de una funcion o bloque 
        if isinstance(nodo, list):
            for instruccion in nodo:
                espacio += self.calcular_espacio_total(nodo.instruccion)

        elif isinstance(nodo, NodoBloque):
            espacio += self.calcular_espacio_total(nodo.instruccion)

        elif isinstance(nodo, NodoAsignacion):
            self.stack_offset += 4
            nodo.offset_pila = self.offste_actual

            self.tabla_simbolos.declarar_variable(nodo.nombre[1], nodo.tipo[1], nodo.offset_pila)


    def generar_codigo_funcion(self, nodo_funcion):
        nombre_func = nodo_funcion.nombre[1]

        #1 Calculamos cuantespacio necesitamos para todas las variables locales
        tamanio_stack = self.calcular_espacio_total(nodo_funcion.cuerpo)

        #2Gerneramos el codigo NASM 
        print(f"; ------ Función: {nodo_funcion} ----- ")
        print(f"global {nombre_func}")
        print(f"{nombre_func}")

        # Prologo estandar
        print(" push ebp") # Guardar el punetro de base anterior 
        print(" mov ebp, esp") #Establecer el nuevo puntero de base

        if tamanio_stack > 0:
            #Alineacion opcional a 16 bytes (buena practica)
            # tamanio_stack = (tamanio_stack + 15) & -15
            print(f"    sub esp, {tamanio_stack} ; Reserva espacio para variables ")

            #3 Generar codgio para el cuerpo 
            #Aqui llamaria as tugenrador de insturccione sparandole el fost

            #Epsilgo estdanra 
            print("     mov esp, ebp")
            print("     pop ebp")
            print("     ret")

