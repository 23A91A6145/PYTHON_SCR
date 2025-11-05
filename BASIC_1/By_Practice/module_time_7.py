

    # Time use cases

import time

print(time.time())
print(time.ctime())

# for more operations on time
print(help(time.time))

print(time.localtime())

a=time.localtime()
b=time.mktime(a)
print(b)

c=time.asctime(time.localtime())
print(c)

# for help
help(time.strftime)

x=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(x)

t = '17 October 2025'
s = time.strptime(t, '%d %B %Y')
print(s)