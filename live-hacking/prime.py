import prime_module

candidate = int(input('Bitte zu checkenden Primzahlkandidaten eingeben:'))
if prime_module.is_prime(candidate):
    print('Primzahl')
else:
    print('keine Primzahl')
