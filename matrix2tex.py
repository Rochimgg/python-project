
import numpy as np

B = np.array([[1/6], [1], [0], [0]])

def bmatrix(A, decim, unit= ""):
    """Returns a LaTeX bmatrix
    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(A.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(round(A, decim)).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + unit + r'\\' for l in lines]
    rv +=  [r'\end{bmatrix}']
    return '\n'.join(rv)

def varmatrix(x = "x", dim = 3):
    var = np.array()
    if dim == 3:
        if x == "x":
            return np.array([["x"], ["y"], ["z"]])
        if x == "X":
            return np.array([["X"], ["Y"], ["Z"]])
    for i in range(dim):
        var[0][i] = x + f"_{i}"
    return var


def matrix_tex_solve(A, b, variable = x, decim = 4, unit_A = "", unit_b=""):
    'planteo el sistema de ecuaciones como una matriz\\\\ \n' +
    bmatrix(b, decim, unit_b)  + "=" +
    bmatrix(A, decim, unit_A) + "\\hspace{5pt} " +
    varmatrix(variable, len(A.shape))
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
                                       '\\end{matrix}\\right)$ \n'