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
        lines = self.get_lines(contents)

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

    @staticmethod
    def get_lines(contents):
        lines = contents.splitlines()

        # Return only non-empty lines
        return [l for l in lines if l]

    @staticmethod
    def remove_comments(text):
        return re.sub(Parser.COMMENT_REGEX, '', text, flags=re.MULTILINE)
