import re


class Parser:
    COMMENT_REGEX = r'#.*$'

    @staticmethod
    def parse_file(file_name):
        file = open(file_name, 'r')

        contents = file.read()
        contents = Parser.remove_comments(contents)

        lines = contents.splitlines()

        for l in lines:
            l = l.strip()
            Parser.handle_command(l)

    @staticmethod
    def handle_command(line):
        split_line = line.split(' ')
        command = split_line[0]
        arg = None

        if len(split_line) > 1:
            arg = split_line[1]

    @staticmethod
    def remove_comments(text):
        return re.sub(Parser.COMMENT_REGEX, '', text, flags=re.MULTILINE)
