def addzero(str):
    if (str=='0'):
        return '00';
    elif (int(str) < 10):
        return '0' + str
    else:
        return str

def cope(flight):
    flight.arrive_time1 = addzero(str(flight.arrive_time.hour)) + ":" + addzero(str(flight.arrive_time.minute))
    flight.leave_time1 = addzero(str(flight.leave_time.hour)) + ":" + addzero(str(flight.leave_time.minute))
    flight.ticket_price1 = int(flight.ticket_price)
    flight.ticket_per = int(flight.ticket_bought * 100 / flight.ticket_number)
            