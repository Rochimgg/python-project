#!/usr/local/bin/python3

import os, sys

import numpy as np

A = np.array([[13, -6, -2, -5], [-6, 10, -3, 0], [-2, -3, 6.6, -1], [-5, 0, -1, 10]])
B = np.array([[1], [0], [0], [0]])
X = np.linalg.inv(A).dot(B)
A_inv = np.linalg.inv(A)
decim_inv = 4
decim_res = 4


def bmatrix(a):
    """Returns a LaTeX bmatrix
    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{bmatrix}']
    return '\n'.join(rv)


def main():
    print('planteo el sistema de ecuaciones como una matriz\\\\ \n'
          '$\\left(\\begin{matrix} \n' +
          str(B[0][0]) + '\\\\ \n' +
          str(B[1][0]) + '\\\\ \n' +
          str(B[2][0]) + '\\\\ \n'
                         '\\end{matrix}\\right)= \n' +
          '\\left(\\begin{matrix} \n' +
          str(A[0][0]) + ' & ' + str(A[0][1]) + ' & ' + str(A[0][2]) + '\\\\ \n' +
          str(A[1][0]) + ' & ' + str(A[1][1]) + ' & ' + str(A[1][2]) + '\\\\ \n' +
          str(A[2][0]) + ' & ' + str(A[2][1]) + ' & ' + str(A[2][2]) + '\\\\ \n'
                                                                       '\\end{matrix}\\right)\\hspace{5pt} \n'
                                                                       '\\left(\\begin{matrix} \n'
                                                                       'i_1\\\\ \n'
                                                                       'i_2\\\\ \n'
                                                                       'i_3\\\\ \n'
                                                                       '\\end{matrix}\\right)$ \\\\ \n'
                                                                       'hago la inversa y calculo las corrientes\\\\ \n'
                                                                       '$ \\left(\\begin{matrix} \n' +
          str(round(A_inv[0][0], decim_inv)) + ' & ' + str(round(A_inv[0][1], decim_inv)) + ' & ' + str(round(A_inv[0][2], decim_inv)) + '\\\\ \n' +
          str(round(A_inv[1][0], decim_inv)) + ' & ' + str(round(A_inv[1][1], decim_inv)) + ' & ' + str(round(A_inv[1][2], decim_inv)) + '\\\\ \n' +
          str(round(A_inv[2][0], decim_inv)) + ' & ' + str(round(A_inv[2][1], decim_inv)) + ' & ' + str(round(A_inv[2][2], decim_inv)) + '\\\\ \n' +
          '\\end{matrix}\\right)\\hspace{5pt} \n'
          '\\left(\\begin{matrix} \n' +
          str(B[0][0]) + '\\\\ \n' +
          str(B[1][0]) + '\\\\ \n' +
          str(B[2][0]) + '\\\\ \n'
                         '\\end{matrix}\\right)= \n' +
          '\\left(\\begin{matrix} \n'
          'i_1\\\\ \n'
          'i_2\\\\ \n'
          'i_3\\\\ \n'
          '\\end{matrix}\\right)$ \\\\ \n'
          'obtengo las corrientes\\\\ \n'
          '$\\left(\\begin{matrix} \n'
          'i_1\\\\ \n'
          'i_2\\\\ \n'
          'i_3\\\\ \n'
          '\\end{matrix}\\right) = \n'
          '\\left(\\begin{matrix} \n' +
          str(round(X[0][0], decim_res)) + ' A \\\\ \n' +
          str(round(X[1][0], decim_res)) + ' A \\\\ \n' +
          str(round(X[2][0], decim_res)) + ' A \\\\ \n'
                                           '\\end{matrix}\\right)$ \n')
    print(X)

if __name__ == '__main__':
    main()
