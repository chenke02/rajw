# -*- coding: utf-8 -*-
# author:chenke

from method import select
from method import week

values = select()
max1 = 0
for i in xrange(len(values)):
    max2 = max(week(values[i][3]))
    max1 = max(max1, max2)
print max1