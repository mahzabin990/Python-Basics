data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atops = data.find('@')
print(atops)
sspos = data.find(' ',atops) # it will look for ' ' after positios atops(21)
print(sspos)
host = data[atops+1 : sspos] # it will start from after @ sign to before the space. as last one is excluding.
print(host)
