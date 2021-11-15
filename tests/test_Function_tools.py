def say_hello(word):
    if word =='Hello':
        return 'Hello!'
    else:
        return 'Bye'
    assert 'Hello' == 'Hello'

def long_word(word):
    if word > 5:
        return 'long'
    else:
        return 'short'
    assert 'long' == 'long'
