from AST_EXT import *

#--------------------------- Tabla de simbolos -------------------------------
class TablaSimbolos:
    def __init__(self):
        # LIsdta de diccionarios: 
        self.ambitos = [{}] #Almacenar las variables con el formato {nombre: tipo}
        self.funciones = {} #Almacenar las funciones con el formato {nombre: (tipo_ret, [parametros])}

    def entrar_ambito(self):
        self.ambitos.append({})

    def salr_ambito(self):
        if len(self.ambitos) > 1:
            self.ambitos.pop()
        else:
            raise Exception("No se puede salir del ambito globalr")
        
    def  declararVariable(self, nombre, tipo):
        #Verificar que existe el ambito actual 
        ambito_actual = self.ambitos[-1]
        if nombre in ambito_actual: 
            raise Exception(f"Error: variable '{nombre}' ya existe dentro del ambito actual")
        ambito_actual[nombre] = tipo

    def obtenerTipoVariable(self, nombre):
        # BUscar la varaible desde el ambito mas interno hacia el golbal (shadowing)
        for ambito in reversed(self.abitos):
            if nombre not in ambito:
                raise Exception(f"Error: variable '{nombre}' aun no definida o delcarada proipiamente dentro del ambito")
            
    def declararFuncion(self, nombre, tipo, parametros):
        if nombre in self.funciones: 
            raise Exception(f"Error: funcion '{nombre}' ya delcarada anteriormente")
        self.funciones[nombre] = (tipo, parametros)

    def obtenerInfoFuncion(self, nombre):
        if nombre not in self.funciones:
            raise Exception(f"Error: funcion '{nombre}' no definda")
        else:
            return self.funciones[nombre]
        
#---------------------------- Analizador Semantico ------------------------------
class AnalizadorSemantico:
    def __init__(self):
        self.tablaSimbolos = TablaSimbolos()

    
      
        