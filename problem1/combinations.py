def generate_combinations(iterable, n):
    if n==0:
        yield []  
    
    for i in range(len(iterable)):
        for sub_comb in generate_combinations(iterable[i+1:], n-1):
            yield list(iterable[i]) + sub_comb
   