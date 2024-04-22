
# Dato un intero col_number, restituire il suo corrispondente titolo di colonna come as esempio compare su un foglio Excel.

def convert_to_title(col_number: int) -> str:
    result: str = ""
    while col_number > 0:
        resto: int = (col_number - 1) % 26 # questo mi da i resto
        result = chr(resto + ord('A')) + result
        col_number = (col_number -1) // 26
    return result


"""
col_number = 700
result = ""
iterazione 1
    resto = 23
    result = X
    col_number = 26
iterazione 2
    resto = 25
    result = ZX
    col_number = 0
"""
