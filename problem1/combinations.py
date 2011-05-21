def generate_combinations(iterable, n):
    if n==0:
        return [[]]   
    
    c = []
    for i in range(len(iterable)):
        for sub_comb in generate_combinations(iterable[i+1:], n-1):
            c.append(list(iterable[i]) + sub_comb)
    return c