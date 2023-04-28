from datetime import datetime


def calculate_age(birth_date):
    birth_date = birth_date.split(" ")[0]
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


# print(calculate_age("1975-11-01 00:00:00"))
# print(datetime.fromisoformat("1975-11-01 00:00:00"))
