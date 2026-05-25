from astropy import units as u
import os
import time

# função limpa tela
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# função de processamento
def processing():
    print("\nProcessando...")
    time.sleep(3)
    limpa_tela()

while True:

    limpa_tela()

    while True:
        try:
            light_year = float(input("Digite quantos anos-luz deseja converter: "))
            break
        except ValueError:
            print("Insira apenas números. Tente novamente.")

    processing()

    # converte em anos-luz para logo depois converter para outras unidades
    distance = light_year * u.lightyear

    unit = input(
        "Em qual unidade de medida gostaria de converter?\n\n"
        "[1] Quilômetros (km)\n"
        "[2] Metros (m)\n"
        "[3] Centímetros (cm)\n"
        "[4] Milhas (mi)\n"
        "[5] Unidade astronômica (AU)\n"
        "[6] Parsec (pc)\n"
        "[7] Kiloparsec (kpc)\n"
        "[8] Megaparsec (Mpc)\n"
        "[9] Todas as opções (all)\n\n> "
    ).strip().lower()

    processing()

    match unit:

        case "km" | "1":
            result_km = distance.to(u.km)
            print(f"{light_year} anos-luz em quilômetros equivale a {result_km.value:,.2f} km")

        case "m" | "2":
            result_m = distance.to(u.m)
            print(f"{light_year} anos-luz em metros equivale a {result_m.value:,.2f} m")

        case "centimetro" | "cm" | "3":
            result_cm = distance.to(u.cm)
            print(f"{light_year} anos-luz em centímetros equivale a {result_cm.value:,.2f} cm")

        case "milha" | "mi" | "4":
            result_mi = distance.to(u.imperial.mile)
            print(f"{light_year} anos-luz em milhas equivale a {result_mi.value:,.2f} mi")

        case "au" | "5":
            result_au = distance.to(u.au)
            print(f"{light_year} anos-luz em unidades astronômicas equivale a {result_au.value:,.2f} au")

        case "parsec" | "pc" | "6":
            result_pc = distance.to(u.pc)
            print(f"{light_year} anos-luz em parsec equivale a {result_pc.value:,.2f} pc")

        case "kiloparsec" | "kpc" | "7":
            result_kpc = distance.to(u.kpc)
            print(f"{light_year} anos-luz em kiloparsec equivale a {result_kpc.value:,.2f} kpc")

        case "megaparsec" | "mpc" | "8":
            result_mpc = distance.to(u.Mpc)
            print(f"{light_year} anos-luz em megaparsec equivale a {result_mpc.value:,.2f} Mpc")

        case "all" | "9":

            result_ly = distance.to(u.lightyear)
            result_km = distance.to(u.km)
            result_m = distance.to(u.m)
            result_cm = distance.to(u.cm)
            result_mi = distance.to(u.imperial.mile)
            result_au = distance.to(u.au)
            result_pc = distance.to(u.pc)
            result_kpc = distance.to(u.kpc)
            result_mpc = distance.to(u.Mpc)

            print("============================== CONVERSOR DE ANOS-LUZ ==============================\n")

            print(f"{'Unidade':<25} {'Sigla':<10} {'Valor'}")
            print("-" * 80)

            print(f"{'Anos-luz':<25} {'ly':<10} {result_ly.value:,.2f}")
            print(f"{'Quilômetros':<25} {'km':<10} {result_km.value:,.2f}")
            print(f"{'Metros':<25} {'m':<10} {result_m.value:,.2f}")
            print(f"{'Centímetros':<25} {'cm':<10} {result_cm.value:,.2f}")
            print(f"{'Milhas':<25} {'mi':<10} {result_mi.value:,.2f}")
            print(f"{'Unidade Astronômica':<25} {'au':<10} {result_au.value:,.2f}")
            print(f"{'Parsec':<25} {'pc':<10} {result_pc.value:,.2f}")
            print(f"{'Kiloparsec':<25} {'kpc':<10} {result_kpc.value:,.6f}")
            print(f"{'Megaparsec':<25} {'Mpc':<10} {result_mpc.value:,.6f}")
        case _:
            print("Unidade inválida. Tente novamente.")

    continuar = input("\n\nVocê deseja converter em outras unidades?\n\n[1] Sim\n[2] Não\n\n> ").strip().lower()

    processing()

    if continuar in ["nao", "não", "n", "2"]:
        print("Obrigada por usar o AstroConvert! <3")
        break