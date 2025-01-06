from typing import Any

list_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(list_dict: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция фильтрации списка словарей по ключу ('EXECUTED')"""
    new_list_dict = []
    for item_list in list_dict:
        if item_list["state"] == state:
            new_list_dict.append(item_list)
    return new_list_dict


def sort_by_date(list_dict: list[dict[str, Any]], sort_direction: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки списка по дате"""
    return sorted(list_dict, key=lambda x: x["date"], reverse=sort_direction)


print(filter_by_state(list_dict))
print(sort_by_date(list_dict))
