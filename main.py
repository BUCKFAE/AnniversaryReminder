from ics import Calendar, Event
from datetime import timedelta, date, datetime


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def main():
    # Use a breakpoint in the code line below to debug your script.
    print("The program has been started!")  # Press ⌘F8 to toggle the breakpoint.

    anniversary_date = date(2020, 4, 14)

    # This time is UTC + 0, Germany is UTC + 2
    default_start_time = ' 00:00:00'

    c = Calendar()

    total_day_passed = 0
    total_months_passed = 0
    total_years_passed = 0

    end_date = date(2150, 1, 1)

    # Looping through all dates between the anniversary and the specified end date
    for single_date in daterange(anniversary_date, end_date):

        current_date_string = single_date.strftime("%Y-%m-%d")
        print(current_date_string)

        # Current day matches anniversary day
        if single_date.day == anniversary_date.day:

            if single_date.month == anniversary_date.month:
                e = Event()
                e.name = "Zusammen seit " + str(total_years_passed) + " Jahren"
                e.begin = current_date_string + default_start_time
                e.make_all_day()
                c.events.add(e)
                total_years_passed += 1
            else:
                e = Event()
                e.name = "Zusammen seit " + str(total_months_passed) + " Monaten"
                e.begin = current_date_string + default_start_time
                e.make_all_day()
                c.events.add(e)

            total_months_passed += 1

        # Checking if multiple of 100
        if total_day_passed % 100 == 0:
            e = Event()
            e.name = "Zusammen seit " + str(total_day_passed) + " Tagen"
            e.begin = current_date_string + default_start_time
            e.make_all_day()
            c.events.add(e)

        # Checking if days is a repdigit
        if len(list(set(str(total_day_passed)))) == 1 and total_day_passed > 10:
            e = Event()
            e.name = "Zusammen seit " + str(total_day_passed) + " Tagen"
            e.begin = current_date_string + default_start_time
            e.make_all_day()
            c.events.add(e)

        # Keeping track of how many days passed
        total_day_passed += 1

    print(c.events)

    with open('anniversary.ics', 'w') as my_file:
        my_file.writelines(c)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
