#!/usr/local/bin/python3

import numpy as np

from rotex.desarrollo2tex.matrix2tex import matrix_tex_solve

A = np.array([[5 / 12, -1 / 6, -1 / 12], [-1 / 6, 5 / 9, -1 / 18], [-1 / 12, -1 / 18, 17 / 36]])
b = np.array([[5], [0], [0]])


def main():
    matrix_tex_solve(A, b, "tension")


if __name__ == '__main__':
    main()
