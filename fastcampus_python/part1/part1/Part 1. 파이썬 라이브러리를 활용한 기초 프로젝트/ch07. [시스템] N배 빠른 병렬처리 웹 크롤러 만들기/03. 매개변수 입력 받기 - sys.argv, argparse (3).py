from __future__ import print_function
import argparse


def main():
    parser = argparse.ArgumentParser(description='This code is written for practice about argparse')
    parser.add_argument('X', type=float,
                        metavar='First_number',
                        help='첫번째 숫자는?')
    parser.add_argument('Y', type=float,
                        metavar='Second_number',
                        help='두번째 숫자는?')
    parser.add_argument('--op', type=str, default='덧셈',
                        choices=['덧셈', '뺄셈', '곱하기', '나누기'],
                        help='연산 방법을 선택해 주세요')
    args = parser.parse_args()

    X = args.X
    Y = args.Y
    op = args.op
    print(calc(X, Y, op))


def calc(x, y, op):
    if op == '덧셈':
        return x + y
    elif op == '뺄셈':
        return x - y
    elif op == '곱하기':
        return x * y
    elif op == '나누기':
        return x / y


if __name__ == "__main__":
    main()