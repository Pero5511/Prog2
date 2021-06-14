def fun(string):
    if len(string)==1:
        return string
    else:
        return string[-1]+fun(string[:-1])

print(fun("Programiranje 2 - rekurzija"))
