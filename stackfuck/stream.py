class InputStreamError(Exception):
    """ An error occurred while reading source input """

class InputStream(object):

    def __init__(self, data):
        self.data = data
        self.pos = 0
        self.line = 1
        self.col = 0

    def next(self):
        self.pos += 1
        ch = self.data[self.pos]
        if ch == '\n':
            self.line += 1
            self.col = 0
        else:
            self.col += 1
        return ch

    def next_n(self, n):
        return ''.join(self.next() for _ in range(n))

    def peek(self, offset=0):
        try:
            return self.data[self.pos + offset]
        except IndexError:
            self.croak("Expected parameters but got EOF!")

    def eof(self):
        try:
            self.peek(offset=1)
            return False
        except:
            return True

    def croak(self, message="An unknown error occurred"):
        raise InputStreamError("{} at line {}, col {}".format(message, self.line, self.col))
