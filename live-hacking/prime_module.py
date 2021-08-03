def is_prime(number):
    isprime = True
    
    if candidate == 1:
        isprime = False
    else:
        # suche nach einem Teiler (der nebenbei gesagt weder 1 noch die
        # zahl (candidate) selbst ist)
        divisor = 2
        while divisor < candidate:
            if candidate % divisor == 0:   # teiler gefunden
                isprime = False
                break    # keine primzahl -> fertig -> break
            divisor += 1

    return isprime

