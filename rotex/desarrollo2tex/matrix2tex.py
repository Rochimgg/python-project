#!/usr/local/bin/python3

import numpy as np

from rotex.desarrollo2tex import diccionario_sistemas_ecuaciones as dic


def bmatrix(A, unit="", form="{}"):
    line = [r'\begin{bmatrix}']

    for x in A:
        rv = []
        for y in x:
            rv.append(form.format(y) + r"\mbox{ }" + unit)
        line.append(' & '.join(rv) + r"\\")
    line.append(r'\end{bmatrix} ' + '\n')
    return ' \n'.join(line)


def equation_system(A, b, dic_key):
    line = [r'$$\begin{array}{rcl} ']

    for aj in range(len(A)):
        line.append(equation(A[aj], b[aj][0], dic_key))
    line.append(r'\end{array}$$  ' + '\n')
    return ' \n'.join(line)


def equation(Aj, b, dic_key):
    dic_cal = dic.calcular.get(dic_key)
    dic_A = dic_cal["A"]
    dic_X = dic_cal["X"]
    dic_b = dic_cal["b"]
    var = varmatrix(dic_cal["variable"], len(Aj))
    aux = []
    for i in range(len(Aj)):
        signo = ""
        if not np.isclose(Aj[i], 0, 1e-20, 0.0):
            if Aj[i] < 0:
                signo = "-"
            if i == 0:
                aux.append("$$" + dic_b["formato"].format(b) + r"\mbox{ }" + dic_b["unidad"] + " & = & " + signo + dic_X["formato"].format(var[i][0]) + r"\cdot" + dic_A["formato"].format(abs(Aj[i])) + r"\mbox{ }" + dic_A["unidad"])
            if Aj[i] >= 0:
                signo = "+"
            if i != 0:
                aux.append(signo + dic_X["formato"].format(var[i][0]) + r"\cdot" + dic_A["formato"].format(abs(Aj[i])) + r"\mbox{ }" + dic_A["unidad"])
    return ' '.join(aux) + r" $$ \\"


def varmatrix(x="x", dim=3):
    if dim == 3:
        if x == "x":
            return [["x"], ["y"], ["z"]]
        if x == "X":
            return [["X"], ["Y"], ["Z"]]
    var = []
    for i in range(dim):
        var.append([f"{x}_{i + 1}"])
    return var


def dic_printer():
    print(dic.calcular.get("corriente"))


def sis_tex_solve(A, b, dic_key):
    s = 'armo el sistema de ecuaciones \n\n' + \
        equation_system(A, b, dic_key) + matrix_tex_solve(A, b, dic_key)
    return s


def matrix_tex_solve(A, b, dic_key):
    X = np.linalg.inv(A).dot(b)
    dic_cal = dic.calcular.get(dic_key)
    dic_A = dic_cal["A"]
    dic_X = dic_cal["X"]
    dic_b = dic_cal["b"]
    s = 'planteo el sistema de ecuaciones como una matriz \n\n' + \
        "$$ " + bmatrix(b, dic_b["unidad"], dic_b["formato"]) + "=" + \
        bmatrix(A, dic_A["unidad"], dic_A["formato"]) + r"\cdot " + \
        bmatrix(varmatrix(dic_cal["variable"], len(A.shape))) + "$$ \n\n" + \
        'hago la inversa y calculo ' + dic_cal["texto"] + '\n\n' + \
        "$$ " + bmatrix(np.linalg.inv(A), dic_A["unidad_inversa"], dic_A["formato"]) + r"\cdot " + \
        bmatrix(b, dic_b["unidad"], dic_b["formato"]) + "=" + \
        bmatrix(varmatrix(dic_cal["variable"], len(A.shape))) + "$$ \n\n" + \
        'obtengo ' + dic_cal["texto"] + '\n\n' + \
        "$$ " + bmatrix(varmatrix(dic_cal["variable"], len(A.shape))) + "=" + \
        bmatrix(X, dic_X["unidad"], dic_X["formato"]) + "$$ \n\n"
    return s


def main():
    A = np.array([[13, -6, -2, -5], [-6, 10, -3, 0], [-2, -3, 6.6, -1], [-5, 0, -1, 10]])
    b = np.array([[1], [0], [0], [0]])

    print(sis_tex_solve(A, b, "tension"))


if __name__ == '__main__':
    main()
