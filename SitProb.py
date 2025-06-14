
"""
En este archivo van a programar un reconocedor sintáctico (parser) de un pequeño lenguaje
de programación que viene descrito más abajo.

La primera parte de este ejercicio es escribir un reconocedor léxico para los componentes
básicos del lenguaje: constantes numéricas, operadores aritméticos y de otro tipo,
símbolos varios (paréntesis, comas, etc.), tipos de valores y, finalmente, identificadores
(nombres de variables).

El analizador léxico deberá estar en un archivo llamado "lexer.py", del cual tienen una
copia incompleta.

La gramática del lenguaje en cuestión es la siguiente:

programa : opt_decls opt_stmts

opt_decls -> decl_lst
          | epsilon

decl_lst -> decl ; decl_lst
	 | decl

decl -> type : id_lst

id_lst -> id, if_list
       | id

type -> int | float

stmt -> id := expr
     | ifelse (expression) [opt_stmts] [opt_stmts]
     | while (expression) [opt_stmts]
     | print expr
     | read id

opt_stmts -> stmt_lst
          | epsil

stmt_lst -> stmt ; stmt_lst
         | stmt

expr -> expr + term
     | expr - term
     | term

term -> term * factor
     | term / factor
     | factor

factor -> ( expr )
       | id
       | numint
       | numfloat

expression -> expr < expr
           | expr <= expr
           | expr > expr
           | expr >= expr
           | expr = expr
---------------

Todos los elementos de la gramática que no aparecen a la izquierda de una flecha (->) son
los terminales, y por tanto, lo que debe ser reconocido por el analizador léxico (lexer).

"""

import sys
import ply.yacc as yacc

# Se traen las fichas o tokens del lenguaje

from lexer import tokens


# deber hacer uso de una tabla de símbolos. La tabla de símbolos contiene información
# La tabla de símbolos se implementa como un diccionario, donde las llaves

class ValoresTabla:
	
	def __init__(self, tipo, valor):
		self.tipo = tipo
		self.valor = valor
	
	
	def get_valor(self):
		return self.valor
	
	def set_valor(self, valor):
		self.valor = valor

# La siguiente declaración es para los nodos del árbol sintáctico reducido. Cada nodo
# Los nodos "punto y coma" son una parte del árbol sintáctico reducido que va "pegando" a
# las demás partes del árbol sintáctico reducido, esto es, a los árboles sintácticos de

class NodoArbolSint:
        def __init__(self, tipo, tipoDato, valor, primero, segundo, tercero) :
                self.tipo = tipo
                self.tipoDato = tipoDato
                self.valor = valor
                self.primero = primero # Primer subarbol
                self.segundo = segundo # Segundo subarbol
                self.tercero = tercero # Tercer subarbol
	
# Lo que sigue es la gramática en formato tipo yacc. Ustedes deben completarla de acuerdo
# a la gramática definida más arriba.

# Se declara un diccionario que será la tabla de símbolos

TS = {}

linea = 1  # El número de línea

def p_program(p):
        '''program : opt_decls opt_stmts'''
        interprete(p[2])

def p_opt_decls(p):
        '''opt_decls : decl_lst
        | empty'''

        pass

	
def p_decl_lst(p):
	'''decl_lst : decl SEMICOLON decl_lst
				| decl'''
	pass

def p_decl(p):
	'decl : type COLON id_lst'
	# de identificadores en la tabla de símbolos añadiendo el tipo y el valor
	for ident in p[3]:
		if ident not in TS:
			TS[ident] = ValoresTabla(p[1], 0)  # Valores numéricos
		else: 
                        print("Variable" + ident +  "ya declarada") # Error.
                        quit()  # Se termina el programa.

def p_id_lst(p):
        '''id_lst : ID COMMA id_lst
			 | ID'''
        if(len(p) == 4):
                p[3].append(p[1])  # Se añade el identificador a la lista.
                p[0] = p[3]
        else:
                p[0] = [p[1]]

def p_type(p):
        '''type : INT
           | FLOAT'''
        p[0] = p[1]

# Ahora vienen los stmts. Se debe construir el árbol sintáctico reducido del
# clase NodoArbonSint que se definió más arriba. Para cada regla de la gramática se debe

def p_stmt(p):
        '''stmt : ID ASSIGN expr
           | IFELSE LPAREN expresion RPAREN LBRACKET opt_stmts RBRACKET LBRACKET opt_stmts RBRACKET
           | WHILE LPAREN expresion RPAREN LBRACKET opt_stmts RBRACKET
           | PRINT expr
           | READ ID'''
        global linea
        linea = p.lineno(1)
        if p[2] == ':=': 
                # Se trata de una asignación. El árbol sintáctico consiste de un nodo, la
                if p[1] not in TS: # Se revisa que la variable haya sido declarada.
                        print("Variable no declarada " + p[1])
                        quit()
                if TS[p[1]].tipo != p[3].tipoDato:
                        print("Error de tipos en asignación")
                        p_error(p)
                temp = NodoArbolSint(1, TS[p[1]].tipo, p[1], None, None, None)
                p[0] = NodoArbolSint(4, p[2], p[1], temp, p[3], None)
        elif p[1] == "ifelse":
                p[0] = NodoArbolSint(4, p[1], 0, p[3], p[6], p[9])
        elif p[1] == "while":
                p[0] = NodoArbolSint(4, p[1], 0, p[3], p[6], None)
        elif p[1] == "print":
                p[0] = NodoArbolSint(4, p[1], 0, p[2], None, None)
        elif p[1] == "read":
                if p[2] not in TS:
                        print("Variable no declarada " + p[2])
                        quit()
                temp = NodoArbolSint(1, TS[p[2]].tipo, p[2], None, None, None)
                p[0] = NodoArbolSint(4, p[1], p[2], temp, None, None)
        else:
                pass


def p_opt_stmts(p):
        '''opt_stmts : stmt_lst
                     | empty'''
        p[0] = p[1]

def p_stmt_lst(p):
        '''stmt_lst : stmt SEMICOLON stmt_lst
                    | stmt'''
        global linea
        if (len(p) == 4):
                # lista de los árboles sintácticos reducidos usando nodos punto y coma
                p[0] = NodoArbolSint(5, 0, 0, p[1], p[3], None)
        else:
                # corresponden a la variable de la gramática stmt.
                p[0] = NodoArbolSint(5, 0, 0, p[1], None, None)

def p_expr(p):
        '''expr : expr PLUS term
                | expr MINUS term
                | term'''
        if (len(p) == 4):
                if p[1].tipoDato != p[3].tipoDato:
                        print("Error de tipos en operación aritmética")
                        p_error(p)
                p[0] = NodoArbolSint(3, p[1].tipoDato, p[2], p[1], p[3], None)
        else: # Se trata de un term
                p[0] = p[1]

def p_term(p):
        '''term : term TIMES factor
                | term DIVIDE factor
                | factor'''
        if (len(p) == 4):
                if p[1].tipoDato != p[3].tipoDato:
                        print("Error de tipos en operación aritmética")
                        p_error(p)
                p[0] = NodoArbolSint(3, p[1].tipoDato, p[2], p[1], p[3], None)
        else: # Se trata de un factor
                p[0] = p[1]

# Para hacer los árboles sintácticos para la variable "factor" es necesario usar varias
# funciones. Una para cada regla de la gramática para la variable "factor".

def p_factor_expr(p):
        'factor : LPAREN expr RPAREN'
        # Lo unico que debe hacerse es pasar el árbol sintáctico que representa a la expr.

        p[0] = p[2]

def p_factor_id(p):
        'factor : ID'

        if p[1] in TS:
                p[0] = NodoArbolSint(1, TS[p[1]].tipo, p[1], None, None, None)
        else:
                raise SyntaxError

def p_factor_numint(p):
        'factor : NUMINT'

        p[0] = NodoArbolSint(2, "int", p[1], None, None, None)

def p_factor_numfloat(p):
        'factor : NUMFLOAT'

        p[0] = NodoArbolSint(2, "float", p[1], None, None, None)


def p_expresion(p):
        '''expresion : expr LT expr
                     | expr LE expr
                     | expr GT expr
                     | expr GE expr
                     | expr EQ expr'''
        if p[1].tipoDato != p[3].tipoDato:
                print("Error de tipos en comparación")
                p_error(p)
        p[0] = NodoArbolSint(6, "bool", p[2], p[1], p[3], None)

                        

def p_empty(p):
	'empty : '
	p[0] = None

def p_error(p):
        print("Error de sintaxis")
        print("línea : " + str(p.lexer.lineno))
        print(p.lexer.token())
        quit()

# El código está ahora representado en un árbol sintáctico reducido, que en realidad puede
# sintácticos reducidos. Para interpretar el código sólo se requiere recorrer la lista e

def interprete(raiz):
        # El parámetro raiz es el apuntador a la lista o árbol sintáctico reducido a
        while raiz != None:
                nodo = raiz.primero
                match nodo.tipoDato:
                        case ':=':
                                asigna(nodo.primero, nodo.segundo)
                        case 'ifelse':
                                ifelse(nodo.primero, nodo.segundo, nodo.tercero)
                        case 'while':
                                dowhile(nodo.primero, nodo.segundo)
                        case 'print':
                                eprint(nodo.primero)
                        case 'read':
                                eread(raiz.primero.valor)
                        case _:
                                # Por aquí no debe pasar porque el parser debe haber
                                pass
                raiz = raiz.segundo  # Ahora raíz es el siguiente nodo punto y coma.
# Aquí termina la función interprete


def asigna(nodo1, nodo2):
        if (nodo1.tipoDato != nodo2.tipoDato):
                raise SyntaxError
        valor = evaluaExpr(nodo2)
        TS[nodo1.valor].set_valor(valor)

def ifelse(nodo1, nodo2, nodo3):

        resultado = evaluaExpresion(nodo1)
        if resultado:
                interprete(nodo2)
        else:
                interprete(nodo3)

def dowhile(nodo1, nodo2):
        while evaluaExpresion(nodo1):
                interprete(nodo2)

def eprint(nodo1):
        print(evaluaExpr(nodo1))

def eread(nodo1):
        # variable en la tabla de símbolos una vez leída y procesada la entrada desde la

        if nodo1 not in TS:
                print("Variable no declarada: " + nodo1)
                quit()
        
        tipo_var = TS[nodo1].tipo
        try:
                if tipo_var == "int":
                        valor = int(input("Ingrese valor entero para " + nodo1 + ": "))
                elif tipo_var == "float":
                        valor = float(input("Ingrese valor flotante para " + nodo1 + ": "))
                else:
                        print("Tipo de variable desconocido")
                        quit()
                
                TS[nodo1].set_valor(valor)
        except ValueError:
                print("Error: Valor inválido para el tipo " + tipo_var)
                quit()

        


def evaluaExpr(nodo):

        if nodo.tipo == 2:
                return nodo.valor

        # está guardado en la tabla de símbolos.
        if nodo.tipo == 1:
                return TS[nodo.valor].get_valor()


        if nodo.tipo == 3:  # Operación aritmética
                izq = evaluaExpr(nodo.primero)
                der = evaluaExpr(nodo.segundo)
                
                operador = nodo.valor
                if operador == '+':
                        return izq + der
                elif operador == '-':
                        return izq - der
                elif operador == '*':
                        return izq * der
                elif operador == '/':
                        if der == 0:
                                print("Error: División por cero")
                                quit()
                        return izq / der
        
        return None

def evaluaExpresion(nodo):

        if nodo.tipo == 6:
                izq = evaluaExpr(nodo.primero)
                der = evaluaExpr(nodo.segundo)
                
                operador = nodo.valor
                if operador == '<':
                        return izq < der
                elif operador == '<=':
                        return izq <= der
                elif operador == '>':
                        return izq > der
                elif operador == '>=':
                        return izq >= der
                elif operador == '=':
                        return izq == der
        
        return False
        

parser = yacc.yacc()


if (len(sys.argv) <= 1):
        print("Se requiere el nombre del archivo a procesar como entrada")
        quit()


entrada = open(sys.argv[1])
programa = entrada.read()

result = parser.parse(programa)
for nombre, val in TS.items():
        print(nombre, val.tipo, val.valor)

# 	result = parser.parse(s)                            #
