

# name of mission: Filtering even numbers (Bug Fixes)

def kata_13_december(lst):
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            lst.pop(i)  # remove element at index i
        else:
            i += 1
    return lst