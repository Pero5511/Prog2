def pozdrav(ime):
    print("Pozdrav, " + str(ime) + "!")

fun=lambda ime:print("Dobrodošao, " + str(ime) + "!")

def glavna(func):
    func("Perica Topić")

glavna(fun)
glavna(pozdrav)
