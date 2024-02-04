# Write a function that will accept a string and a keyword argument. 
# The function will be responsible to get rid off any white spaces or new lines around the given string. 
# By default it will trim of heading and trailing white spaces (or new lines). 
# However, if "left" is passed as keyword argument it will trim only the heading white spaces. 
# Similarly if "right" is passed it will get rid off only the trailing white spaces. Name the function as trim. 
# The mandatory argument will be named text and name the keyword argument as side . 
# side can be any of these three values: "both", "left", "right" where "both" is default.
#  Here are some examples.

# Output:
# Given: " I am rock. \n"
# trim(text) -> "I am rock."

# Given: "\n I will apply for VISA soon!    \t"
# trim(text, side="right") -> "\n I will apply for VISA soon!"

# Given: "  Let's explore Mississippi!!!         "
# trim(text, side="left") -> "Let's explore Mississippi!!!         "

# Solution -1 
def trim(text:str, side='both'):
    text_trimmed = text.strip()
    if side == 'left':
        text_trimmed = text.lstrip()
    elif side == 'right':
        text_trimmed = text.rstrip()
    return text_trimmed


# Solution -2 
def trim(text:str, side=None):
    if side == 'left':
        return text.lstrip()
    if side == 'right':
        return text.rstrip()
    return text.strip()

    
def main():
    # text = input('Enter your text:')
    text1 = " I am rock. \n"
    text2 = "\n I will apply for VISA soon!    \t"
    text3 = "  Let's explore Mississippi!!!      \n   "
    print(trim(text1))
    print(trim(text2,side='both'))
    print(trim(text3,side='left'))

if __name__ == '__main__':
    main()

