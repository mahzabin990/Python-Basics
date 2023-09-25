text = 'Astronomy is an ancient science, long separated from the study of terrestrial physics. In the Aristotelian worldview, bodies in the sky appeared to be unchanging spheres whose only motion was uniform motion in a circle, while the earthly world was the realm which underwent growth and decay and in which natural motion was in a straight line and ended when the moving object reached its goal. Consequently, it was held that the celestial region was made of a fundamentally different kind of matter from that found in the terrestrial sphere; either Fire as maintained by Plato, or Aether as maintained by Aristotle. During the 17th century, natural philosophers such as Galileo, Descartes, and Newton began to maintain that the celestial and terrestrial regions were made of similar kinds of material and were subject to the same natural laws. Their challenge was that the tools had not yet been invented with which to prove these assertions.'
punctuations = [',', '.', ';']
refined_text = text
for puncuation in punctuations:
   refined_text = refined_text.replace(puncuation, '')

words = refined_text.split()

word_counter = {}

for word in words:
   word_counter[word] = word_counter.get(word, 0) + 1

print(word_counter)
