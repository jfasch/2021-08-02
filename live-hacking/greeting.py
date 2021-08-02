name = input('Name:')
sex = input('Sex:')
timeofday = int(input('Hour:'))

if sex == 'm':
    anrede = 'Mr.'
elif sex == 'f':
    anrede = 'Mrs.'
elif sex == 'd':
    anrede = 'Mr[s].'
else:
    print('Kein gueltiges Geschlecht')

if timeofday >= 0 and timeofday <=9:
    goodwhatever = 'Good morning'
elif timeofday >= 10 and timeofday <= 17:
    goodwhatever = 'Good day'
elif timeofday >= 18 and timeofday <= 23:
    goodwhatever = 'Good evening'
else:
    print('Schlechte Stunde erwischt')
    
greeting_phrase = goodwhatever + ', ' + anrede + ' ' + name
print(greeting_phrase)