from varasto import Varasto

def olut_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def mehu_setterit(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def virhe_tilanteita():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def lisaa_varastoon_olutta(olutta, maara):
    print(f"Olutvarasto: {olutta}")
    print(f"olutta.lisaa_varastoon({maara})")
    olutta.lisaa_varastoon(maara)
    print(f"Olutvarasto: {olutta}")

def lisaa_varastoon_mehua(mehua, maara):
    print(f"Mehuvarasto: {mehua}")
    print(f"mehua.lisaa_varastoon({maara})")
    mehua.lisaa_varastoon(maara)
    print(f"Mehuvarasto: {mehua}")

def ota_varastosta_olutta(olutta, maara):
    print(f"Olutvarasto: {olutta}")
    print(f"olutta.ota_varastosta({maara})")
    saatiin = olutta.ota_varastosta(maara)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

def ota_varastosta_mehua(mehua, maara):
    print(f"Mehuvarasto: {mehua}")
    print(f"mehua.otaVarastosta({maara})")
    saatiin = mehua.ota_varastosta(maara)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    olut_getterit(olutta)

    mehu_setterit(mehua)

    virhe_tilanteita()

    lisaa_varastoon_olutta(olutta, 1000.0)

    lisaa_varastoon_mehua(mehua, -666.0)

    ota_varastosta_olutta(olutta, 1000.0)

    ota_varastosta_mehua(mehua, -32.9)


if __name__ == "__main__":
    main()
