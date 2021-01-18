# Siia kirjutatud koodi ja sisu saame repositooriumisse ülesse laadida

# Teeme siia faili programmi, mis lihtsalt prindib kasutajale suvalisi küsimusi
# Selleks on meil vaja listi küsimustest, mille seast valida

import random

küsimused = ['Kuidas sul läheb täna?', 'Kas õues on külm?', 'Mis kell sa ärkasid?', 'Millest sa mõtled praegu?']

def valiSuvalineKüsimus():
    listiPikkus = len(küsimused) - 1
    suvalineIndeks = random.randint(0, listiPikkus)
    return küsimused[suvalineIndeks]

print(valiSuvalineKüsimus())

#Nüüd võiks selle ära commitida (salvestada) ja repositooriumisse lükata
