"""
Created on Tue Jul  9 2019

@author: Shahab Bangash
"""
x = abs(float(input()))
delta = float(0.00001)
iterr = 0
lo_limit = 0
hi_limit = x

result = (lo_limit+hi_limit)/2.0
while (abs(result**2 -x) > delta):
    if result**2>x:
        hi_limit = result
    else:
        lo_limit=result
    result = (lo_limit+hi_limit)/2.0
    iterr+=1
print("it took", iterr, "tries ", "Approx. Answer:", result)
