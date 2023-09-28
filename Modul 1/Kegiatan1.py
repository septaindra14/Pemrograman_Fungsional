
def minus(angka, nomor):
    return angka-nomor

def tambah(angkapertama, angkakedua):
    return angkapertama+angkakedua

def mult(angkapertama, angkakedua):
    return angkapertama*angkakedua

def div(angkapertama, angkakedua):
    if angkakedua == 0:
        raise ValueError("Perhitungan dengan angka 0 tidak diperbolehkan")
    return angkapertama/angkakedua


def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '+':
            return tambah(tree(left_operand), tree(right_operand))
        elif operator == '-':
            return minus(tree(left_operand), tree(right_operand))
        elif operator == '*':
            return mult(tree(left_operand), tree(right_operand))
        elif operator == '/':
            return div(tree(left_operand), tree(right_operand))
    else:
        raise ValueError("Invalid expression tree node")


expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))
result = tree(expression_tree)
print("Modul Kegiatan 1 \n\nHasil Evaluasi Pohon Ekspresi:", result)