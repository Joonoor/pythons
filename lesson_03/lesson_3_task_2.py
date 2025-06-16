from smartphone import Smartphone

phone_1 = Smartphone("iPhone", "15 Pro", "+79005553535")
phone_2 = Smartphone("Sumsung", "S25", "+79123456789")
phone_3 = Smartphone("Xiomi", "14 Pro", "+79987654321")
phone_4 = Smartphone("OnePlus", "12", "+79998887766")
phone_5 = Smartphone("Realme", "6 Pro", "+79121056739")

catalog = [phone_1, phone_2, phone_3, phone_4, phone_5]

for x in catalog:
    print(f"{x.brand} - {x.model}. {x.number}")
