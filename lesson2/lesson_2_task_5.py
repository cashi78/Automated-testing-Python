def month_to_season(mon):
    match mon:
        case 12 | 1 | 2 : return "Зима"
        case 3 | 4 | 5 : return "Весна"
        case 6 | 7 | 8 : return "Лето"
        case 9 | 10 | 11 : return "Осень"


for x in range(1,13):
    print(x, month_to_season(x))