import sys


def main():
    print(f"Number of arguments: {len(sys.argv)}")
    print(f"Argument List: {str(sys.argv)}")

    sys.exit(1)


if __name__ == '__main__':
    main()