import ply.lex as lex

tokens = ['INTEGER']

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = "123 456 789"
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)