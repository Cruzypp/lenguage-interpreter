import ply.lex as lex

# Lista completa de tokens
tokens = [
    # Palabras reservadas
    'INT', 'FLOAT', 'IFELSE', 'WHILE', 'PRINT', 'READ',
    
    # Operadores y símbolos
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET',
    'SEMICOLON', 'COLON', 'COMMA', 'ASSIGN',
    
    # Operadores de comparación
    'LT', 'LE', 'GT', 'GE', 'EQ',
    
    # Identificadores y literales
    'ID', 'NUMINT', 'NUMFLOAT'
]

# Palabras reservadas
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'ifelse': 'IFELSE',
    'while': 'WHILE',
    'print': 'PRINT',
    'read': 'READ'
}

# Reglas para tokens simples (orden importante para tokens de múltiples caracteres)
t_ASSIGN = r':='
t_LE = r'<='
t_GE = r'>='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_COLON = r':'
t_COMMA = r','
t_LT = r'<'
t_GT = r'>'
t_EQ = r'='

# Ignorar espacios y tabs
t_ignore = ' \t'

# Regla para números flotantes (debe ir antes que enteros)
def t_NUMFLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Regla para números enteros
def t_NUMINT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regla para identificadores y palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Regla para comentarios (los ignora)
def t_COMMENT(t):
    r'\#.*'
    pass

# Regla para manejar saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores léxicos
def t_error(t):
    print(f"Error léxico: Carácter ilegal '{t.value[0]}' en línea {t.lineno}")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Función de prueba
if __name__ == '__main__':
    # Prueba con ejemplo1.txt
    data1 = """
int : x, y, z, c;

read x;
read y;
z := 0;
c := 0;
while (z < y)
   [ c := c + x;
     z := z + 1 ];
print c;
    """
    
    print("--- Análisis ejemplo1 ---")
    lexer.input(data1)
    for tok in lexer:
        print(f"LexToken({tok.type},'{tok.value}',{tok.lineno},{tok.lexpos})")
    
    print("\n--- Análisis ejemplo2 ---")
    data2 = """
int : x, y, z;

read x;
read y;
ifelse (x < y)
   [z := x; print x]
   [z := y; print (y + 1)];
print z;
    """
    
    lexer.input(data2)
    for tok in lexer:
        print(f"LexToken({tok.type},'{tok.value}',{tok.lineno},{tok.lexpos})")