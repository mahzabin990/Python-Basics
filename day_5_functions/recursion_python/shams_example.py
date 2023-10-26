# recursion
# Shams's example
def fact_rec(x):
    if x==1:
        return 1
    elif x>1:
        return x * fact_rec(x-1)
    
print(fact_rec(5))