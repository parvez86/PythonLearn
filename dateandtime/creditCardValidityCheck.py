import datetime

def checkValidity(cdate_timestamp, expdate_timestamp):
    return 'Valid' if float(cdate_timestamp) <= float(expdate_timestamp) else 'Not valid'

print(checkValidity(datetime.datetime.now().timestamp(), datetime.datetime(2020, 9, 30, hour= 12, minute=0, second=0).timestamp()))