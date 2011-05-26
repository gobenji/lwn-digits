#!/usr/bin/python

# http://lwn.net/Articles/443683/

import sys

charset = ' Wadefhlnost'
modulo = 13
s = 13682311570832829480888979137834570837851469148689544502986
num = iter(range(2, 9999))
while s != 1 :
        n = num.next()
        if s % n == 0 :
                sys.stdout.write("%s" % charset[(n - 1) % modulo])
                s /= n
        #end if
#end while
sys.stdout.write("\n")

