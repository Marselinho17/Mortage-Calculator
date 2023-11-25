import math

print("Vítejte v hypoteční kalkulačce pro rok 2023.")
while True:
    try:
        average_salary = int(input("Jaký je Váš průměrný čistý měsíční příjem domácnosti? Zadejte údaj v korunách. "))
        break
    except ValueError:
        print("Chybně zadaný údaj, prosím zadejte číslo.")

while True:
    try:
        installments = int(input("V jaké výši jsou Vaše měsíční závazky domácnosti? Jako kreditní karty, úvěry atd. Zadejte údaj v korunách.  "))
        break
    except ValueError:
        print("Chybně zadaný údaj, prosím zadejte číslo.")

while True:
    try:
        age = int(input("Kolik je Vám let? "))
        break
    except ValueError:
        print("Chybně zadaný věk, zadejte prosím číslo.")

total_debt = int(average_salary-installments) # average income - other expenses (loans)

def mortgage_payment(property_value, interest_rate, years):
    y = years * 12 # number of months
    r = interest_rate / (12 * 100) # monthly interest rate
    monthly_payment = (property_value * r * (1 + r) ** y) / ((1 + r) ** y - 1) # monthly payment calculation
    
    return monthly_payment

if age >= 18 and age <= 36:
    dsti = int((average_salary*0.50)-installments)
    dti = int(total_debt*12*9.5) # up to the age of 36, a maximum of 9.5 times the annual income
    if dsti <= 0:
        print(" ")
        print("Bohužel, máte již vysoké splátky a hypotéku nedostanete.")
    else:
        print(" ")
        print(f"Vaše měsíční splátka hypotéky může být maximálně ve výši {dsti},-KČ a výše hypotéky může být maximálně {dti},-KČ")
        print("Maximální výše hypotéky může být do 90% hodnoty konkrétní nemovitosti.")
        print(" ")
        input("Můžeme spolu spočítat splátku na konkrétní nemovistost, pokud chcete pokračovat, zmáčkněte Enter...")
        print(" ")
        while True:
            try:
                property_value = int(input("Jaká je hodnota nemovitosti?  "))
                break
            except ValueError:
                print("Chybně zadaný údaj, prosím zadejte číslo.")

        while True:
            try:
                interest_rate = float(input("Za jakou procentní úrokovou sazbu Vám banka půjčí? Napište ve formátu x.xx(příklad 5.99):  "))
                break
            except ValueError:
                print("Chybně zadaný údaj, prosím zadejte ve správném formátu x.xx(příklad 5.99).")

        while True:
            try:
                years = int(input("Na kolik let si chcete půjčit?  "))
                break
            except ValueError:
                print("Chybně zadaný údaj, prosím zadejte číslo.")
        
        monthly_payment = mortgage_payment(property_value, interest_rate, years)
                
        print(" ")
        print(f"Pro půjčku {property_value} Kč s úrokovou sazbou {interest_rate}% na {years} let je splátka {monthly_payment:.2f} Kč/měsíc.")
        print("Nezapomeňte, že maximální výše Vaší hypotéky může být do 90% hodnoty nemovitosti.")
        print(f"Tzn. pokud je hodnota Vaší vybrané nemovitosti {property_value},-Kč, banka Vám půjčí maximálně {int(property_value*0.90)},-Kč a minimálně {int(property_value*0.10)},-Kč musíte zaplatit ze svého nebo z jiného zdroje.")
        
        property_value = property_value*0.90
        monthly_payment = mortgage_payment(property_value, interest_rate, years)
        
        if monthly_payment <= dsti:           
            print(f"Když bude hodnota nemovitosti {int(property_value)},-Kč, bude měsíční splátka hypotéky {monthly_payment:.2f},-Kč, tzn. že se vejdete do svého limitu maximální měsíční splátky ({dsti},-Kč).")
            print(" ")
        else:
            print(" ")
            print(f"Bohužel, Váše měsíční splátka({monthly_payment:.2f},-Kč) by byla vyšší než můžete měsíčně platit({dsti},-Kč).")
            print(" ")

elif age >= 37 and age <= 65:   
    dsti = int((average_salary*0.45)-installments)
    dti = int(total_debt*12*8.5) # over 36 years max 8.5 times the annual income
    if dsti <= 0:
        print(" ")
        print("Bohužel, máte již vysoké splátky a hypotéku nedostanete.")
    else:
        print(" ")
        print(f"Vaše měsíční splátka hypotéky může být maximálně ve výši {dsti},-KČ a výše hypotéky může být maximálně {dti},-KČ")
        print("Maximální výše hypotéky může být do 80% hodnoty konkrétní nemovitosti.")
        input("Můžeme spolu spočítat splátku na konkrétní nemovistost, pokud chcete pokračovat, zmáčkněte Enter...")
        print(" ")
        while True:
            try:
                property_value = int(input("Jaká je hodnota nemovitosti?  "))
                break
            except ValueError:
                print("Chybně zadaný údaj, prosím zadejte číslo.")

        while True:
            try:
                interest_rate = float(input("Za jakou procentní úrokovou sazbu Vám banka půjčí? Napište ve formátu x.xx(příklad 5.99):  "))
                break
            except ValueError:
                print("Chybně zadaný údaj, prosím zadejte ve správném formátu x.xx(příklad 5.99).")

        while True:
            try:
                years = int(input("Na kolik let si chcete půjčit?  "))
                break
            except ValueError:
                print("Chybně zadaný údaj, prosím zadejte číslo.")
        
        monthly_payment = mortgage_payment(property_value, interest_rate, years)
                
        print(" ")
        print(f"Pro půjčku {property_value} Kč s úrokovou sazbou {interest_rate}% na {years} let je splátka {monthly_payment:.2f} Kč/měsíc.")
        print("Nezapomeňte, že maximální výše Vaší hypotéky může být do 80% hodnoty nemovitosti.")
        print(f"Tzn. pokud je hodnota Vaší vybrané nemovitosti {property_value},-Kč, banka Vám půjčí maximálně {int(property_value*0.80)},-Kč a minimálně {int(property_value*0.20)},-Kč musíte zaplatit ze svého nebo z jiného zdroje.")
        
        property_value = property_value*0.80
        monthly_payment = mortgage_payment(property_value, interest_rate, years)
        
        if monthly_payment <= dsti and property_value <= dti:           
            print(f"Když bude hodnota nemovitosti {int(property_value)},-Kč, bude měsíční splátka hypotéky {monthly_payment:.2f},-Kč, tzn. že se vejdete do svého limitu maximální měsíční splátky ({dsti},-Kč).")
            print(" ")
        else:
            print(" ")
            print(f"Bohužel, Váše měsíční splátka({monthly_payment:.2f},-Kč) by byla vyšší než můžete měsíčně platit({dsti},-Kč).")
            print(" ")
        
else:
    print("Váš věk je moc nízký nebo vysoký pro získání hypotéky.")
