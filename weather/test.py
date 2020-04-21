lit = [x for x in range(1,14)]

print(lit)
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

print(list(chunks(lit,5)))