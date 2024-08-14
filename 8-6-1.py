from datetime import datetime
now = datetime.today()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

dt = datetime.strptime("21/11/2006 16:30", "%d/%m/%Y %H:%M")
print(dt)
print(dt.strftime("%Y年%m月%d日 %H時%M分"))

import datetime
t_delta = datetime.timedelta(days=1)
print(dt + t_delta)
