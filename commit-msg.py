#!/usr/bin/python3.8

import sys, re


def main():
    with open(sys.argv[1], "r") as fp:
        lines = fp.readlines()
        for line in lines:
            if not line_valid(line):
                print(
                    'Por favor, digite uma mensagem de commit respeitando o padrão\nExemplo:  fix(texto_qualquer): my '
                    'changes are this\nAtente para o limite de 50 caracteres na descrição!')
                sys.exit(1)
            else:
                print('Commit realizado respeitando o padrão!')
                sys.exit(0)


def line_valid(text):
    # return re.match("#\s?\d{,10}\s?-\s?(\w|\s){,49}", text)
    return re.match("(feat|dev|fix|perf|refactory|build|ci|docs|style|test|chore|env)\([^)]*\):(\w|\s){,49}", text)


if __name__ == '__main__':
    main()
