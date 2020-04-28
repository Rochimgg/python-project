#!/usr/local/bin/python3

import numpy as np
from rotex.desarrollo2tex.matrix2tex import matrix_tex_solve

A = np.array([[13, -6, -2, -5], [-6, 10, -3, 0], [-2, -3, 6.6, -1], [-5, 0, -1, 10]])
b = np.array([[1], [0], [0], [0]])


def main():
    matrix_tex_solve(A, b, "corriente")


if __name__ == '__main__':
    main()
