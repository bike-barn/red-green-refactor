import traceback
from calc import Calc, CalcError


def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break

        if not text:
            continue

        calc = Calc(text)
        try:
            result = calc.parse()
        except CalcError:
            traceback.print_exc()
        else:
            print(result)

if __name__ == '__main__':
    main()
