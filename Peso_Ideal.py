def peso_Ideal(altura, sexo):
            if sexo == "F":
                print(f"Seu PESO IDEAL É { (62.1 * altura) - 44.7:.1f} KG")
            elif sexo == "M":
                 print(f"Seu PESO IDEAL É {(72.7 * altura) - 58:.1f} KG")
            else:
                print("Erro! O PROGRAMA SERA FECHADO")


Altura =float(input("Informe sua Altura:"))
Sex = str(input("SEXO [F/M]:")).strip()
peso_Ideal(Altura,Sex)