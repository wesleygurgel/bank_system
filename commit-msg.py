#!/usr/bin/python3.8

import sys, re


def main():
    with open(sys.argv[1], "r") as fp:
        lines = fp.readlines()
        for line in lines:
            if not line_valid(line):
                print('Por favor, digite uma mensagem de commit respeitando o padrão\nExemplo: #7 - Meu Commit')
                sys.exit(1)
            else:
                print('Commit realizado respeitando o padrão!')
                sys.exit(0)


def line_valid(text):
    return re.match("#\s?\d{,10}\s?-\s?(\w|\s){,49}", text)


if __name__ == '__main__':
    main()
