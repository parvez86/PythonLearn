import time, datetime
epochseconds = time.time()
print(epochseconds)

t = time.ctime(epochseconds)
print(t)

dt = datetime.datetime.today()
print('Current Date: {}/{}/{}'.format(dt.day, dt.month, dt.year))
print('Current Time: {}:{}:{}'.format(dt.hour, dt.minute, dt.second))

print(dir(datetime))
print(dir(time))

datetime_func = ['date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
print('# of datatime function: ', len(datetime_func))

print('\nShowing some datetime module functions:')
print('date: ', dt.date())
print('time: ', dt.time())
print('zone: ', dt.astimezone())
print('tzinfo: ', datetime.tzinfo())
print('timedelata: ', datetime.timedelta(days=20, hours=10, minutes=24, seconds=3, microseconds=23))

time_func = ['altzone', 'asctime', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime',
             'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns',
             'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns',
             'timezone', 'tzname']
print('\n\n# of time function: ', len(time_func))

print('\nShowing some time module functions:')
print('time: ', time.time())
print('ctime: ', time.ctime())
print('altzone: ', time.altzone)
print('daylight: ', time.daylight)

# if passing parameter is null it returns ctime
# otherwise it returns epoch respect of passing second
print('gmtime: ', time.gmtime(1890))
print('localtime: ', time.localtime())

# accepts local time as inputs and return inverse of local time
# or whether the time given refers to daylight saving time or standard time.
print('mkime: ', time.mktime(time.gmtime()))

print('monotonic: ', time.monotonic())          # returns the value of clock which never goes backward
print('monotonic_ns: ', time.monotonic_ns())    # ns-> nano seconds
print('perf_counter: ', time.perf_counter())        # return execution time
print('perf_counter_ns: ', time.perf_counter_ns())        # return execution time
print('process time: ', time.process_time())
print('sleep: ', time.sleep(1))     # halt program for a specific duration

# Convert a time tuple to a string according to a format specification
# converts data & time to its string representations & return it
print('strftime: ', time.strftime(t))

# converts data & time string representations to its corresponding & return it
print('strptime: ', time.strptime(t))


print('struct time: ', time.struct_time)
print('thread time: ', time.thread_time())
print('timezone: ', time.timezone)
print('tzname: ', time.tzname)

time_time_func = ['as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
print('\n\n# of time() function: ', len(time_time_func))

print('\nShowing some time() module functions:')
print('is integer: ', time.time().is_integer())
print('as integer ratio: ', time.time().as_integer_ratio())     # Convert a string or number to a floating point number, if possible.
print('conjugate: ', time.time().conjugate())       # return complex conjugate  if any
print('real val: ', time.time().real)
print('imaginary val: ', time.time().imag)
print('hex: ', time.time().hex())
print('fromhex: ', time.time().fromhex(time.time().hex()))


datetime_datetime_func = ['astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
# instances: date, time, hour, minute, second, milli-second, day, dst, month, year, weekday
print('\n\n# of datatime() function: ',len(datetime_datetime_func))
print('astimezone: ', dt.astimezone())
print('combine: ', dt.combine(dt.date(), dt.time(), dt.tzinfo)) # as dt.date() is as datetime object, tz.info is just ignored
print('ctime: ', dt.ctime())
print('dst: ', dt.dst())        # haven't figured out yet
print('fold:', dt.fold)     # 0 / 1 , 0-> earlier reading of ambiguous local time, 1-> later reading.
print('date: ', dt.date())
print('month: ', dt.month)
print('minute: ', dt.minute)
print('year: ', dt.year)
print('weekday: ', dt.weekday())
print('min: ', dt.min)  # return starting datetime
print('max: ', dt.max)  # return largest datetime
print('now: ', dt.now())
print('resolution: ', dt.resolution)
print('strftime: ', datetime.datetime.strftime(dt, '%Y %m %d, %H:%M:%S'))   # converts string to object format
print('strptime: ', datetime.datetime.strptime("2018/11/12 09:15:32",'%Y/%m/%d %H:%M:%S'))      #converts object to string format
print('isoweekday: ', dt.isoweekday())
print('isocalender: ', dt.isocalendar())
print('fromoisocalender: ', datetime.datetime.fromisocalendar(2020, 40, 3))    # return the mid-object(like datetime/date)
print('isoformat: ', dt.isoformat('#', 'seconds'))
print('fromisoformat: ', datetime.datetime.fromisoformat('2020-09-29'))
print('timestamp: ', dt.timestamp())
print('timetz: ', dt.timetz())
print('timetuple: ', dt.timetuple())
print('today: ', dt.today())
print('fromordinal: ', dt.fromordinal(1))
print('toordinal: ', dt.toordinal())    # returns the day count from the date 01/01/01
print('tzinfo: ', dt.tzinfo)
print('tzname: ', dt.tzname())
print('utcnow: ', dt.utcnow())
print('utcoffset: ',dt.utcoffset())
print('utctimetuple: ', dt.utctimetuple())
print('utctimstamp: ', datetime.datetime.utcfromtimestamp(dt.timestamp()))
print('replace: ', dt.replace(month=11))