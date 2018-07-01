import parsec
'''
"a"
3
null
true
[1,2,3]
{ "key": "value" }
'''

examples = ['{"a": "true", "b": false, "C": ["a", "b", "C"]}', '{"a": 10.00}', '{"b":null}', '{"a": {"a": "x", "b":"t", "c": {"a": true, "c": [true, false, true]}}}']

whitespace = parsec.regex(r'\s*')

lexeme = lambda p: p << whitespace

lcbrace = lexeme(parsec.string('{'))
rcbrace = lexeme(parsec.string('}'))
lsbrace = lexeme(parsec.string('['))
rsbrace = lexeme(parsec.string(']'))
colon = lexeme(parsec.string(':'))
comma = lexeme(parsec.string(','))
true = lexeme(parsec.string('true')).result(True)
false = lexeme(parsec.string('false')).result(False)
null = lexeme(parsec.string('null')).result(None)

def number():
    return lexeme(parsec.regex(r'-?(0|[1-9][0-9]*)([.0-9]+)?'))


def string():
    return lexeme(parsec.regex(r'[^"\\]+'))

@parsec.generate
def quoted_string():
    yield parsec.string('"')
    qs = yield string()
    yield parsec.string('"')
    return qs

@parsec.generate
def array():
    # return lexeme(parsec.joint(lsbrace, parsec.sepBy(value, comma), rsbrace))
    yield lsbrace
    elements = yield parsec.sepBy(value, comma)
    yield rsbrace
    return elements

@parsec.generate
def mapping():
    key = yield quoted_string
    yield colon
    val = yield value
    return (key, val)

@parsec.generate
def json():
    yield lcbrace
    pairs = yield parsec.sepBy(mapping, comma)
    yield rcbrace
    return pairs

value = number() | quoted_string | mapping | json | array | true | false | null

parser = whitespace >> json
print(parser.parse('{"a":[1,2,"shyam"]}'))
print(parser.parse('{"a":"b", "c":[1,2,"shyam"]}'))
for e in examples:
    print(parser.parse(e))
