from address import Address
from mailing import Mailing

my_mailing = Mailing(Address("602200", "Муром", "Дзержинского", "50", "20"),
                     Address("602113", "Владимир", "Ленина", "2", "3"),
                     4500,
                     "654321")


print("Отправление", my_mailing.track, "из",
      my_mailing.to_address.index,
      my_mailing.to_address.city,
      my_mailing.to_address.street,
      my_mailing.to_address.building,
      my_mailing.to_address.apartments, "в",
      my_mailing.from_address.index,
      my_mailing.from_address.city,
      my_mailing.from_address.street,
      my_mailing.from_address.building,
      my_mailing.from_address.apartments,
      ". Стоимость", my_mailing.cost, "рублей")
