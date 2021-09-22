#!/usr/bin/python3.8

import sys, re, getpass

rules = """
# Por favor, digite uma mensagem de commit respeitando o padrão!
# Exemplo: feat(done_something): created gambiarra: feature/SW-2820

# Atente para:
#   - Usar apenas letras minúsculas, excessão para o numero do card -> (SW-2820).
#   - Não usar espaços em excesso.
#   - Presença de caracteres como ":" e "/" são importantes! 
"""


def main():
    with open(sys.argv[1], "r") as fp:
        lines = fp.readlines()
        for line in lines:
            print(line)
            if not line_valid(line):
                print(rules)
                sys.exit(1)
            else:
                print(f'Commit realizado respeitando o padrão! Você é o cara {getpass.getuser()}!')
                sys.exit(1)


def line_valid(text):
    return re.match(
        "(feat|dev|fix|perf|refactory|build|ci|docs|style|test|chore|env)\((\s|[a-z]|-|_)*\):(\s|[a-z]|-|_)*:\s?\w{,7}?/?[A-Z]{2}-\d{4}",
        text)


if __name__ == '__main__':
    main()
