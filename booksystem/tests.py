from datetime import datetime
import pytz

# # Show all available time zones in Asia
# for tz in pytz.all_timezones:
#     if str(tz).startswith('Asia'):
#         print(tz)

utc_tz = pytz.timezone('UTC')
india_tz = pytz.timezone('Asia/Calcutta')
local_naive = datetime.now(tz=utc_tz)
print(local_naive)
local_aware = datetime.now()  #Default tz=none
print(local_aware)

# After setting tz, it is also converted to naive type
local_aware_to_naive = datetime.now(tz=india_tz)  # default tz=None
print(local_aware_to_naive)
if local_aware_to_naive > local_naive:
    print('yes')


mySet = set()
if len(mySet) == 0:
    print('hahh')