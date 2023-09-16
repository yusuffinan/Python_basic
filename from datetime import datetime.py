from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"")
a =datetime.now()

print(datetime.strftime(a,"%D %B"))

su_an = datetime.timestamp(a)
print(su_an)
su_an2 = datetime.fromtimestamp(su_an)
print(su_an2)

print(datetime.fromtimestamp(0))

b = datetime(1995,5,1)
print(a-b)