text = 'Astronomy is an ancient science, long separated from the study of terrestrial physics. In the Aristotelian worldview, bodies in the sky appeared to be unchanging spheres whose only motion was uniform motion in a circle, while the earthly world was the realm which underwent growth and decay and in which natural motion was in a straight line and ended when the moving object reached its goal. Consequently, it was held that the celestial region was made of a fundamentally different kind of matter from that found in the terrestrial sphere; either Fire as maintained by Plato, or Aether as maintained by Aristotle. During the 17th century, natural philosophers such as Galileo, Descartes, and Newton began to maintain that the celestial and terrestrial regions were made of similar kinds of material and were subject to the same natural laws. Their challenge was that the tools had not yet been invented with which to prove these assertions.'

def punc(x:str, punctuations = [',', '.', ';']):
    '''This function will get rid off all the punctuations'''
    for puncuation in punctuations:
        x = x.replace(puncuation, '')
    return x

# def punc(x:str):
#     '''This function will get rid off all the punctuations'''
#     punctuations = [',', '.', ';', '\'']
#     for puncuation in punctuations:
#         x = x.replace(puncuation, '')
#     return x

def word(y:str):
    words = y.split()
    return words

def sort(z:list):
    sort_mylist = sorted(z)
    return sort_mylist

def main():
    refined_text = punc(text)
    words_list = word(refined_text)
    sorted_list = sort(words_list)
    print(sorted_list)


if __name__ == '__main__': 
    main()

