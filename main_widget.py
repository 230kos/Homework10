from src.widget import mask_account_card, get_date

user_account_card = input("Введите тип и номер карты или тип и номер счёта:")
print(mask_account_card(user_account_card))

user_date = input("Введите дату:")
# формат ввода 2024-03-11T02:26:18.671407
print(get_date(user_date))
