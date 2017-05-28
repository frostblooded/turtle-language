import re

from src.command_parser import CommandParser


class Parser:
    COMMENT_REGEX = r'#.*$'

    def __init__(self):
        self.command_parser = CommandParser()

    def parse_file(self, file_name):
        file = open(file_name, 'r')

        contents = file.read()
        contents = self.remove_comments(contents)

        lines = contents.splitlines()

        for l in lines:
            self.handle_line(l)

    def handle_line(self, line):
        line = line.strip()
        split_line = line.split(' ')
        command = split_line[0]
        arg = None

        if len(split_line) > 1:
            arg = split_line[1]

        self.command_parser.handle_command(command, arg)

    def remove_comments(self, text):
        return re.sub(Parser.COMMENT_REGEX, '', text, flags=re.MULTILINE)
