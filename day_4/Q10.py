# declare the varialbe below

sentence = "I have scored 8.0 on IELTS."

# Make the sentence in all upper case and print it.
upper = sentence.upper()
print(upper)
#print(sentence)
#  Print the last word in the sentence using slicing.
print(sentence[-6:-1])
#print(sentence[0:3])

# Extract the number in the sentence and convert it into a float. Also prove that it is a float.
x=sentence[14]
print(x)
y=float(x)
print(y)
print(type(y))