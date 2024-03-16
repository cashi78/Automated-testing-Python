def is_year_leap(year):
    return (year % 4 == 0)


is_leap = is_year_leap(2023)
print('2023 год : ', is_leap)


is_leap = is_year_leap(2024)
print('2024 год : ', is_leap)
