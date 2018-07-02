import parsec

# "1 - (2 * (3 + 4) / 5)" => -1.8

example = "1 - (2 * (3 + 4) / 5)"
expected = -1.8

whitespace = parsec.regex(r'\s*')

lexeme = lambda p: p << whitespace

plus = lexeme(parsec.string('+'))
minus = lexeme(parsec.string('-'))
divide = lexeme(parsec.string('/'))
multiply = lexeme(parsec.string('*'))
lbrace = lexeme(parsec.string('('))
rbrace = lexeme(parsec.string(')'))

def number():
    return lexeme(parsec.regex(r'-?(0|[1-9][0-9]*)([.0-9]+)?'))

@parsec.generate
def addition():
    n1 = yield number()
    yield plus
    n2 = yield number()
    return float(n1) + float(n2)

@parsec.generate
def subtraction():
    n1 = yield number()
    yield minus
    n2 = yield number()
    return float(n1) - float(n2)

@parsec.generate
def multiplication():
    n1 = yield number()
    yield multiply
    n2 = yield number()
    return float(n1) * float(n2)

@parsec.generate
def division():
    n1 = yield number()
    yield divide
    n2 = yield number()
    return float(n1) / float(n2)

operation = addition | subtraction | multiplication | division

# @parsec.generate
# def value():
#     yield lbrace
#     exp = yield expression
#     yield rbrace
#     return number() | exp
#
# def expression():
#
#     @parsec.generate
#     def without_braces():
#         number()
#
#
#     @parsec.generate
#     def with_braces():
#
#     return without_braces | with_braces

parser = whitespace >> operation

# assert parser.parse(example) == expected

print(parser.parse('1 - 2'))
