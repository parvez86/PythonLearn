import datetime

def checkValidity(cdate, expdate):
    # return 'Valid' if float(cdate.timestamp()) <= float(expdate.timestamp()) else 'Expired'
    if float(cdate.timestamp()) <= float(expdate.timestamp()):
        return 'Valid'
    else:
        raise RuntimeError('Card has expired')

# print(checkValidity(datetime.datetime.now().timestamp(), datetime.datetime(2020, 9, 30, hour= 12, minute=0, second=0).timestamp()))