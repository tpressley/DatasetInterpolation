import math;

def main():
    xs = [0,1,2,3,4]
    ys = [1,2,4,8,16]


def evalLagrangeInterpolation(x, xs, ys):
    r = 0
    
    for j in range(0,len(y)):
        m = 1
        for k in range(len(y)):
            if (xs[k] != xs[j]):
                m *= (x - xs[k]) / (xs[j] - xs[k])
            r += ys[j] * m
    return r
main()