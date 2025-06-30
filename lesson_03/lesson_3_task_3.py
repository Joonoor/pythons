from mailing import Mailing
from address import Address

address_to = Address(169933, "Vorkuta", "Lenina", 36, 15)
address_from = Address(175964, "Murmansk", "Polar", 9, 40)
mailing = Mailing(address_to, address_from, 5000, "lite")

print(f"Отпрвление {mailing.track} из {address_from.index}, {address_from.city}, {address_from.street}, {address_from.home} - {address_from.flat} в {address_to.index}, {address_to.city}, {address_to.street}, {address_to.home} - {address_to.flat}. Стоимость {mailing.cost}.")
