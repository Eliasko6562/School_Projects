EARTH_GRAVITY = 9.8 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 299792 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

#Vsechny vypocty jsou priblizne

def lightning_thunder_distance():
    """
    Vypocita vzdalenost blesku od pozorovatele na zaklade casu (v sekundach) mezi zableskem a hromem.
    Pouziva rychlost zvuku.
    """
    time = float(input("Zadej cas (s) mezi zableskem a hromem: "))
    distance_sound = SPEED_OF_SOUND * time
    print(f"Vzdálenost blesku přibližně: {distance_sound:.2f} metrů")

def free_fall_time():
    """
    Vypocita cas volneho padu objektu z urcite vysky na Zemi a Mesici.
    Pouziva tihove zrychleni Zeme a Mesice.
    """
    height = float(input("Zadej vysku (m) ze ktereho objekt bude padat: "))
    time_earth = (2 * height / EARTH_GRAVITY) ** 0.5
    time_moon = (2 * height / MOON_GRAVITY) ** 0.5
    print(f"Cas volneho padu na Zemi: {time_earth:.2f}s")
    print(f"Cas volneho padu na Mesici: {time_moon:.2f}s")
    
def light_travel_time():
    """
    Vypocita cas, ktere svetlo potrebuje k urazeni urcite vzdalenosti ve vakuu.
    Pouziva rychlost svetla.
    """
    distance = float(input("Zadej vzdalenost (km), ktere svetlo ma urazit: "))
    time = distance / SPEED_OF_LIGHT
    print(f"Cas potrebny pro svetlo k urazeni {distance:,.0f} km: {time:,.2f} s (vteriny)".format(distance).replace(',', ' '))