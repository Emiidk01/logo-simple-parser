from Lexer import *
from Parser import *
import sys

if __name__ == '__main__':
    parser = Parser("test/bad/input06bad.txt")
    parser.analize()