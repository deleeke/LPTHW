from nose.tools import *
from ex49.ex49 import *
from ex49.lexicon import Lexicon

lex = Lexicon('north south east west',
                  'go kill eat',
                  'the in of then',
                  'bear princess witch mage warrior')

entry1 = lex.scan('kill')
entry2 = lex.scan('Eat the princess')
entry3 = lex.scan('Go north')
badentry = lex.scan('Poop in a bucket')

def test_peek():
    assert_equal(peek(lex.scan('kill')), 'verb')

    result = peek(lex.scan('north'))
    assert_equal(result, 'direction')

    assert_equal(peek(lex.scan('bear')), 'noun')
    result = peek(lex.scan('bear'))
    assert_equal(result, 'noun')

def test_match():
    assert_equal(match(lex.scan('Eat the princess'), 'verb'),
                                ('verb', 'eat'))
    result = match(lex.scan('go kill eat'), 'verb')
    assert_equal(result, ('verb', 'go'))

    assert_equal(match(lex.scan('Devour the princess'), 'verb'),
                                None)
    result = match(lex.scan('Poop kill eat'), 'verb')
    assert_equal(result, None)

    assert_equal(match(lex.scan(' '), 'verb'),
                                None)
    result = match(lex.scan(' '), 'verb')
    assert_equal(result, None)

    assert_equal(match(badentry, 'verb'),
                                None)
    result = match(badentry, 'verb')
    assert_equal(result, None)

def test_parse_verb():
    #implicitly, this tests the skip() function
    assert_equal(parse_verb(lex.scan("kill the bear")),
                            ('verb', 'kill'))

    result = parse_verb(lex.scan("Eat the poop"))
    assert_equal(result, ('verb', 'eat'))

    assert_raises(ParserError, parse_verb, lex.scan('the witch'))

def test_parse_object():
    assert_equal(parse_object(lex.scan("the bear")),
                            ('noun', 'bear'))
    result = parse_object(lex.scan("the witch"))
    assert_equal(result, ('noun', 'witch'))

    assert_raises(ParserError, parse_object, lex.scan('kill the kill'))

def test_parse_sentence():
    # also tests the Sentence() class and
    # the parse_subject() function
    assert_equal(type(parse_sentence(lex.scan("kill the bear"))),
                 type(Sentence('player', 'kill', 'bear')))
    assert_raises(ParserError, parse_sentence, (lex.scan('Cruton salad')))
