#!/usr/local/bin/python3

import numpy as np

from rotex.desarrollo2tex import diccionario_sistemas_ecuaciones as dic

B = np.array([[1 / 6], [1], [0], [0]])


def bmatrix(A, unit="", form="{}"):
    line = [r'\begin{bmatrix}']

    for x in A:
        rv = []
        for y in x:
            rv.append(form.format(y) + r"\mbox{ }" + unit)
        line.append(' & '.join(rv) + r"\\")
    line.append(r'\end{bmatrix} ' + '\n')
    return ' \n'.join(line)


def varmatrix(x="x", dim=3):
    if dim == 3:
        if x == "x":
            return bmatrix([["x"], ["y"], ["z"]])
        if x == "X":
            return bmatrix([["X"], ["Y"], ["Z"]])
    var = []
    for i in range(dim):
        var.append([f"{x}_{i + 1}"])
    return bmatrix(var)


def dic_printer():
    print(dic.calcular.get("corriente"))


def matrix_tex_solve(A, b, dic_key):
    X = np.linalg.inv(A).dot(B)
    dic_cal = dic.calcular.get(dic_key)
    dic_A = dic_cal["A"]
    dic_X = dic_cal["X"]
    dic_b = dic_cal["b"]
    s = 'planteo el sistema de ecuaciones como una matriz \n\n' + \
        "$$ " + bmatrix(b, dic_b["unidad"], dic_b["formato"]) + "=" + \
        bmatrix(A, dic_A["unidad"], dic_A["formato"]) + r"\cdot " + \
        varmatrix(dic_cal["variable"], len(A.shape)) + "$$ \n\n" + \
        'hago la inversa y calculo ' + dic_cal["texto"] + '\n\n' + \
        "$$ " + bmatrix(np.linalg.inv(A), dic_A["unidad_inversa"], dic_A["formato"]) + r"\cdot " + \
        bmatrix(b, dic_b["unidad"], dic_b["formato"]) + "=" + \
        varmatrix(dic_cal["variable"], len(A.shape)) + "$$ \n\n" + \
        'obtengo ' + dic_cal["texto"] + '\n\n' + \
        "$$ " + varmatrix(dic_cal["variable"], len(A.shape)) + "=" + \
        bmatrix(X, dic_X["unidad"], dic_X["formato"]) + "$$ \n\n"
    print(s)


def main():
    A = np.array([[13, -6, -2, -5], [-6, 10, -3, 0], [-2, -3, 6.6, -1], [-5, 0, -1, 10]])
    b = np.array([[1], [0], [0], [0]])

    matrix_tex_solve(A, b, "corriente")


if __name__ == '__main__':
    main()
