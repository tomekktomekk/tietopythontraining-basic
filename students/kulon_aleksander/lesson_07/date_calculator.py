from datetime import datetime, timedelta


def main():
    current_datetime = datetime.now()
    years, days, hours, mins = 1, 32, 25, 53
    days += years * 365
    print(current_datetime + timedelta(days=days, hours=hours, minutes=mins))


if __name__ == '__main__':
    main()
