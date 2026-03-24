from lexico import *
from sintacticoExt import * 
from semantico import *

codigoFuente = """
int suma(int a, int b, int c){
    return a + b;
    printf(c);
}

int main(){
    int resultado = suma(3, 5);
    return 0;
}
"""

# Análisis léxico
tokens = identificarTokens(codigoFuente)

print("========= Elementos ==========")
for elemento in tokens:
    print(f"{elemento}\n")

print("=======Analisis Sintactico ===========")
# Análisis sintáctico
try:
    print("Iniciando analisis sintactico")
    parser = Parse(tokens)
    arbol_ast = parser.parsear()
    print("Analisis sintactico exitoso")

    # Imprimir el AST
    print(json.dumps(imprimir_ast(arbol_ast), indent=1))

    print("========= Traducciones ===============")
    # Traducir a Python
    print("========= Python ===============")
    print(arbol_ast.traducirPy())
    #Traducir a ruby 
    print("========= Ruby ===============")
    print(arbol_ast.traducirRuby())
    print("==========Asembler=========")
    print(arbol_ast.generarCodigo)
except SyntaxError as e:
    print(f"Error sintáctico: {e}")





