# https://gist.github.com/brianchung808/867b18b2ad7bdcb27bd2a362e9f84eda
import parsec
'''
""        => ""
"1"       => "One"
"234"     => "Two,Three,Four"
"10,000"  => "One,Zero,Zero,Zero,Zero"
"  4619 " => "Four,Six,One,Nine"
'''

examples = ['', '1', '234', '10,000', '  4619 ']
expected = ['', 'One', 'Two,Three,Four', 'One,Zero,Zero,Zero,Zero', 'Four,Six,One,Nine']

print(parsec.string("1").parse("111"))

whitespace = parsec.regex(r'\s+')
commas = parsec.regex(r',+')
ignore = parsec.many((whitespace | commas))

lexeme = lambda p: p << ignore

zero = lexeme(parsec.string('0')).result('Zero')
one = lexeme(parsec.string('1')).result('One')
two = lexeme(parsec.string('2')).result('Two')
three = lexeme(parsec.string('3')).result('Three')
four = lexeme(parsec.string('4')).result('Four')
five = lexeme(parsec.string('5')).result('Five')
six = lexeme(parsec.string('6')).result('Six')
seven = lexeme(parsec.string('7')).result('Seven')
eight = lexeme(parsec.string('8')).result('Eight')
nine = lexeme(parsec.string('9')).result('Nine')

parser = ignore >> parsec.many((zero | one | two | three | four | five | six | seven | eight | nine))
print(parser.parse('  4619 '))

for i, e in enumerate(examples):
    assert ','.join(parser.parse(e)) == expected[i]
    print("Test {} passed".format(i+1))


