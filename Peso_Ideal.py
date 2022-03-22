def peso_Ideal(altura, sex):
            if sex == "F":
                print(f"Your ideal weight is ? { (62.1 * altura) - 44.7:.1f} KG")
            elif sex == "M":
                 print(f"Your ideal weight is ? {(72.7 * altura) - 58:.1f} KG")
            else:
                print("Error! THE PROGRAM WILL BE CLOSED")


Altura =float(input("Enter your height:"))
Sex = str(input("SEX [F/M]:")).strip()
peso_Ideal(Altura,Sex)