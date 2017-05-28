import sys

from src.parser import Parser

if __name__ == "__main__":
    arguments_count = len(sys.argv) - 1

    if arguments_count > 1:
        print('Please only pass a single file')

    file_arg = sys.argv[1]
    Parser.parse_file(file_arg)
