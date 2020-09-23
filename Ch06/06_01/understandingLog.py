#!/usr/bin/python3
# Repeated doubling
ndays = 0
nrabbits = 1
while nrabbits <= 1000:
    nrabbits *= 2
    ndays = ndays + 1
print(ndays)
# ----------------------------
# Repeated Halving
ndays = 0
ncovid = 1000
while ncovid >= 1:
    ncovid /= 2
    ndays = ndays + 1
print(ndays)
# ----------------------------
# Total Spread
ndays = 0
total = 0
ncovid = 1
while total <= 1000:
    total += ncovid
    ncovid *= 2
    ndays = ndays + 1
print(ndays)
