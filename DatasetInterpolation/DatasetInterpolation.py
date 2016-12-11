import math
import plotly.plotly as py
import plotly.graph_objs as go
import time 
import datetime


def main():
    py.sign_in('tpressley', 'komTQBzvw4OWlX8u4cBO') #totally secure
    previous = TimestampMillisec64()
    print( "Starting...")

    xs = []
    yas = []
    ybs = []
    f = open("data.txt")
    for line in f:
        s = line.split("\t")

        xs.append(int(s[0]))
        yas.append(int(s[1]))
        ybs.append(int(s[2].strip('\n')))
    f.close()

    #INDEX FOR CUBIC SUBSECTION
    start = 0
    end = 0
    os = []
    ls = subdivide(xs,4)
    print (len(ls))
    i = 0
    for x in ls:
        os.append(evalCublicSplines(x,xs,yas))
        print (len(ls) - (i))
        i += 1
    trace = go.Scatter(x = ls, y = os)
    data = [trace]
    py.iplot(data, filename='dataInterpolationAssignment')

def evalCublicSplines(x, xs, ys):

    i = 1
    while(xs[i] < x):
        i += 1
    t = (x - xs[i-1]) / (xs[i] - xs[i-1])
    a = 0
    b = 0
    r = (1-t)*ys[i-1] + t*ys[i] + t*(1-t)*(a*(1-t)+b*t)
    return r

def evalLagrangeInterpolation(x, xs, ys):
    r = 0
    
    for j in range(0,len(ys)):
        m = 1
        for k in range(len(xs)):
            if (k != j):
                m *= (x - xs[k]) / (xs[j] - xs[k])
        r += ys[j] * m
        #print (j)
    return r


#Algorithm found at http://csharphelper.com/blog/2014/10/find-a-linear-least-squares-fit-for-a-set-of-points-in-c/
def evalLeastSquares(x, xs, ys):
    s1 = len(xs)
    sx = 0
    sxx = 0
    sy = 0
    sxy = 0
    for i in range(0,s1):
        sx += xs[i]
        sy += ys[i]
        sxx = xs[i] * xs[i]
        sxy = xs[i] * ys[i]
    m = (sxy * s1 - sx * sy) / (sxx * s1 - sx * sx)
    b = (sxy * sx - sy * sxx) / (sx * sx - s1 * sxx)

    return m*x + b

def subdivide(xs,count):
    ts = xs.copy()
    rs = xs.copy()
    while count > 0:
        count -= 1
        for i in range(0,len(ts)-1):
            rs.insert(i+1+i,(ts[i]+ts[i+1])/2)
        ts = rs.copy()
    return rs


def TimestampMillisec64():
    return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000) 
main()