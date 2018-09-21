Leeftijd= float(input('Geef je leeftijd: '))
PaspoortBeschikking= input('Heeft u een Nederlands paspoort? (antwoord ja/nee): ')
if Leeftijd >=18 and PaspoortBeschikking=='ja':
    print('Gefeliciteerd, je mag stemmen!')
if Leeftijd <18 or PaspoortBeschikking != 'ja':
    print('Helaas mag je niet stemmen.')