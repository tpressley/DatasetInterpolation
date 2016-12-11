import math;

def main():
    xs = [0,1,2,3,4]
    ys = [1,2,4,8,16]

    ls = subdivide(xs,7)
    for x in ls:
        evalLagrangeInterpolation(x,xs,ys)

def evalLagrangeInterpolation(x, xs, ys):
    r = 0
    
    for j in range(0,len(ys)):
        m = 1
        for k in range(len(xs)):
            if (k != j):
                m *= (x - xs[k]) / (xs[j] - xs[k])
        r += ys[j] * m
    print (r)
    return r

def subdivide(xs,count):
    ts = xs.copy()
    rs = xs.copy()
    while count > 0:
        count -= 1
        for i in range(0,len(ts)-1):
            rs.insert(i+1+i,(ts[i]+ts[i+1])/2)
        ts = rs.copy()
    return rs

main()