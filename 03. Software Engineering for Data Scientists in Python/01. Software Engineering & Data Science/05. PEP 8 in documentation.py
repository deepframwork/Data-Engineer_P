'''
PEP 8 in documentation
So far we've focused on how PEP 8 affects functional pieces of code. There are also rules to help make comments and documentation more readable. In this exercise, you'll be fixing various types of comments to be PEP 8 compliant.

The result of a pycodestyle style check on the code can be seen below.

my_script.py:2:15: E261 at least two spaces before inline comment
my_script.py:5:16: E262 inline comment should start with '# '
my_script.py:11:1: E265 block comment should start with '# '
my_script.py:13:2: E114 indentation is not a multiple of four (comment)
my_script.py:13:2: E116 unexpected indentation (comment)
Instructions
100 XP
Leverage the output of pycodestyle to edit the code's comments to be compliant with PEP 8.
'''
SOLUTION

def print_phrase(phrase, polite=True, shout=False):
    if polite:  # It's generally polite to say please
        phrase = 'Please ' + phrase

    if shout:  # All caps looks like a written shout
        phrase = phrase.upper() + '!!'

    print(phrase)


# Politely ask for help
print_phrase('help me', polite=True)
# Shout about a discovery
print_phrase('eureka', shout=True)
