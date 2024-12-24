from src.masks import get_mask_account, get_mask_card_number

user_card_numbers = input("Введите номер карты:")
print(get_mask_card_number(user_card_numbers))

user_account_numbers = input("Введите номер счёта:")
print(get_mask_account(user_account_numbers))
