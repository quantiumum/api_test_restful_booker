from faker import Faker
import datetime as dt

def get_fake_data():
    fake = Faker()
    set_param = { "firstname" : fake.first_name(),
                  "lastname" : fake.last_name(),
                  "totalprice" : fake.random_int(min=100, max=999),
                  "depositpaid" : fake.boolean(),
                  "bookingdates" : {
                        "checkin" : (fake.past_date()).strftime('%Y-%m-%d'),
                        "checkout" : (fake.future_date()).strftime('%Y-%m-%d')
                  },
                  "additionalneeds" : "Breakfast"
                  }
    return set_param

def check_date(last_date, checked_date):
    last_date = dt.datetime.strptime(last_date, '%Y-%m-%d')
    checked_date = dt.datetime.strptime(checked_date, '%Y-%m-%d')
    if last_date > checked_date:
        return False
    else:
        return True