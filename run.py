from booking.booking import Booking

with Booking() as bot:

    bot.land_first_page()

    bot.change_currency(currency="AUD")

    bot.select_place_to_go("New York")

    bot.select_dates(check_in_date='2021-09-20',
                     check_out_date='2021-10-10')

    bot.select_adults(20)

    