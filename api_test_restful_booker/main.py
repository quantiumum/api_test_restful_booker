import basic_method as bm, fake_param as fp, scheme_validate as sv
import pytest


def test_create_token_with_corect_data():
    select = bm.BasicMethods()
    token = select.get_token('admin', 'password123')
    token = sv.to_dict(token, 'text')
    assert 'reason' not in token, r"Can't get token with correct login\pass"

def test_create_token_with_uncorect_data():
    select = bm.BasicMethods()
    token = select.get_token('aaaadmin', 'password123')
    token = sv.to_dict(token, 'text')
    assert 'reason' in token, r"Can't get token with correct login\pass"

def test_get_all_booking_id():
    select = bm.BasicMethods()
    all_id = select.get_all_booking_id()
    all_id = sv.to_dict(all_id, 'text')
    for i in all_id:
        assert sv.valid_data(i, sv.schema_get_all_id) == True, r'Get data not math with based json scheme'

@pytest.mark.xfail
def test_get_all_booking_id_with_all_filters():
    select = bm.BasicMethods()
    fake_booking = fp.get_fake_data()
    for i in range(4):
        booking = select.create_booking(fake_booking)
    filters = {
                "firstname" : fake_booking["firstname"],
                "lastname" : fake_booking["lastname"],
                "checkin" : fake_booking['bookingdates']["checkin"],
                "checkout" : fake_booking['bookingdates']["checkout"]
    }
    all_id = select.get_all_booking_id(filters)
    all_id = sv.to_dict(all_id, 'text')
    assert all_id != [], r'Matches not founded'
    for i in all_id:
        assert sv.valid_data(i, sv.schema_get_all_id) == True, r'Get data not math with based json scheme'
        real_booking = select.get_booking_on_id(str(i['bookingid']))
        real_booking = sv.to_dict(real_booking, 'text')
        assert real_booking == fake_booking, r'Bad filter'

@pytest.mark.slow
def test_get_all_booking_id_with_name_filters():
    select = bm.BasicMethods()
    fake_booking = fp.get_fake_data()
    for i in range(4):
        booking = select.create_booking(fake_booking)
    filters = {
                "firstname" : fake_booking["firstname"],
                "lastname" : fake_booking["lastname"]
    }
    all_id = select.get_all_booking_id(filters)
    all_id = sv.to_dict(all_id, 'text')
    assert all_id != [], r'Matches not founded'
    for i in all_id:
        assert sv.valid_data(i, sv.schema_get_all_id) == True, r'Get data not math with based json scheme'
        real_booking = select.get_booking_on_id(str(i['bookingid']))
        real_booking = sv.to_dict(real_booking, 'text')
        assert real_booking == fake_booking, r'Bad filter'

@pytest.mark.slow
def test_get_all_booking_id_with_dates_filters():
    select = bm.BasicMethods()
    fake_booking = fp.get_fake_data()
    for i in range(4):
        booking = select.create_booking(fake_booking)
    filters = {
                "checkin" : fake_booking['bookingdates']["checkin"],
                "checkout" : fake_booking['bookingdates']["checkout"]
    }
    all_id = select.get_all_booking_id(filters)
    all_id = sv.to_dict(all_id, 'text')
    assert all_id != [], r'Matches not founded'
    for i in all_id:
        assert sv.valid_data(i, sv.schema_get_all_id) == True, r'Get data not math with based json scheme'
        real_booking = select.get_booking_on_id(str(i['bookingid']))
        real_booking = sv.to_dict(real_booking, 'text')
        assert fp.check_date(fake_booking['bookingdates']["checkin"], real_booking['bookingdates']["checkin"]), r'Bad filter'
        assert fp.check_date(real_booking['bookingdates']["checkout"], fake_booking['bookingdates']["checkout"]), r'Bad filter'

def test_add_booking():
    select = bm.BasicMethods()
    fake_booking = fp.get_fake_data()
    booking = select.create_booking(fake_booking)
    booking = sv.to_dict(booking, 'text')
    assert sv.valid_data(booking, sv.schema_booking) == True, r'Get data not math with based json scheme'
    real_booking = select.get_booking_on_id(str(booking['bookingid']))
    real_booking = sv.to_dict(real_booking, 'text')
    assert fake_booking == real_booking, r'Added another data to system'

def test_update_full_booking_with_good_token():
    select = bm.BasicMethods()
    data_booking = fp.get_fake_data()
    booking = select.create_booking(data_booking)
    booking = sv.to_dict(booking, 'text')
    upd_data_booking = fp.get_fake_data()
    real_booking = select.update_full_booking(str(booking['bookingid']), upd_data_booking, sv.to_dict(select.get_token('admin', 'password123'), 'text'))
    real_booking = sv.to_dict(real_booking, 'text')
    assert upd_data_booking == real_booking, r'Updated data not in system'

def test_update_full_booking_with_bad_token():
    select = bm.BasicMethods()
    data_booking = fp.get_fake_data()
    booking = sv.to_dict(select.create_booking(data_booking), 'text')
    upd_data_booking = fp.get_fake_data()
    real_booking = select.update_full_booking(str(booking['bookingid']), upd_data_booking, {'token': 'thisisbadtoken'})
    real_booking = sv.to_dict(real_booking, 'text')
    assert upd_data_booking != real_booking, r'Updated data not in system'

#Place for partical update, but needed update def generate fake data

def test_delete_booking_on_id_with_good_token():
    select = bm.BasicMethods()
    all_id = select.get_all_booking_id()
    all_id = sv.to_dict(all_id, 'text')
    deleted_id = select.delete_booking_on_id(str(all_id[0]['bookingid']), sv.to_dict(select.get_token('admin', 'password123'), 'text'))    
    assert '201' in str(deleted_id), r'Resourse not avaliable'
    assert sv.to_dict(select.get_booking_on_id(str(all_id[0]['bookingid'])), 'text') == False, 'Booking not deleted'

def test_delete_booking_on_id_with_bad_token():
    select = bm.BasicMethods()
    all_id = select.get_all_booking_id()
    all_id = sv.to_dict(all_id, 'text')
    deleted_id = select.delete_booking_on_id(str(all_id[0]['bookingid']), {'token': 'thisisbadtoken'})    
    assert '201' not in str(deleted_id), r'Response successeful'
    assert sv.to_dict(select.get_booking_on_id(str(all_id[0]['bookingid'])), 'text') != False, 'Booking deleted'