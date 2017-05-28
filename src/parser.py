import re

from src.command_parser import CommandParser


class Parser:
    COMMENT_REGEX = r'#.*$'

    @staticmethod
    def parse_file(file_name):
        file = open(file_name, 'r')

        contents = file.read()
        contents = Parser.remove_comments(contents)

        lines = contents.splitlines()

        for l in lines:
            Parser.handle_line(l)

    @staticmethod
    def handle_line(line):
        line = line.strip()
        split_line = line.split(' ')
        command = split_line[0]
        arg = None

        if len(split_line) > 1:
            arg = split_line[1]

        CommandParser.handle_command(command, arg)

    @staticmethod
    def remove_comments(text):
        return re.sub(Parser.COMMENT_REGEX, '', text, flags=re.MULTILINE)
