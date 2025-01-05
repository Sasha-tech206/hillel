number = int(input("Enter your number: "))

if number < 0 or number >= 8640000:
    print("Число повинно бути від 0 до 8640000.")
else:
    days, remainder = divmod(number, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        day_word = "дня"
    else:
        day_word = "днів"

    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)
    seconds = str(seconds).zfill(2)

    print(f"{days} {day_word}, {hours}:{minutes}:{seconds}")