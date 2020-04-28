#!/usr/local/bin/python3

import numpy as np
from rotex.desarrollo2tex.matrix2tex import matrix_tex_solve

A = np.array([[12, -2, 0], [-2, 7, -1], [0, -1, 6]])
b = np.array([[6], [-8], [2]])


def main():
    matrix_tex_solve(A, b, "corriente")


if __name__ == '__main__':
    main()
