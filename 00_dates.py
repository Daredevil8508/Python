### Dates ###

from datetime import datetime

now = datetime.now()

print(now.day)
print(now.month)
print(now.year)
print(now.minute)
print(now.second)


timestamp = now.timestamp()

print(timestamp)