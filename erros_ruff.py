
def function_one():
    pass
def function_two():
    pass

def example_function(a,b):
    """Exemplo de função com vários erros"""
    print("Esta é uma linha de código que é \
          muito longa e ultrapassa o limite \
           de 79 caracteres, o que não está \
          de acordo com o PEP8.")
    result = 1 \
        + 2
    my_variable = 10  # Nome de variável não está no estilo snake_case
    print(my_variable)
    return result + a + b

def another_function():
    undefined_variable = 2
    print(undefined_variable)  # Variável não definida

def function_with_trailing_whitespace():
    pass