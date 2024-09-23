x1 , y1 = map(int,input().split())
xs , ys = map(int,input().split())
xf , yf = map(int,input().split())
jrk_lngkrn = (xf-x1)**2 + (yf-y1)**2
jrk_mulai = (xf-xs)**2 + (yf-ys)**2
if jrk_lngkrn > jrk_mulai:
    print("Yes")
else:
    print("No")
