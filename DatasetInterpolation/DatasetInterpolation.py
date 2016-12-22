import math
import plotly.plotly as py
import plotly.graph_objs as go
import time 
import datetime

#I'm coding at 3:30 AM please forgive me I'll refactor later
def main():
    py.sign_in('*****', '*****') #Obfuscated until I can take the time to add config files and such
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

    


    os = []
    ls = subdivide(xs,2)

    #INDEX FOR CUBIC SUBSECTION -- long set
    start = 0
    end = 0
    i = 0
    while(ls[i] < 230):
        i += 1
        if(ls[i] < 220):
            start = i
        end = i
    #INDEX FOR CUBIC SUB -- X set
    xstart = 0
    xend = 0
    i = 0
    while(xs[i] < 230):
        i += 1
        if(xs[i] < 220):
            xstart = i
        xend = i
    i = 0
    print (len(ls))
    for x in ls[0:start]:
        os.append(evalLeastSquares(x,xs[0:xstart],yas[0:xstart]))
        print (len(ls) - (i))
        i += 1
    for x in ls[start:end]:
        os.append(evalCublicSplines(x,xs[xstart:xend],yas[xstart:xend]))
        print (len(ls) - (i))
        i += 1
    for x in ls[end:len(ls)-1]:
        os.append(evalLeastSquares(x,xs[xend:len(ls)-1],yas[xend:len(ls)-1]))
        print (len(ls) - (i))
        i += 1
    #for x in ls[end:len(ls)-1]:
    #    os.append(evalLeastSquares(x,xs[xend:len(ls)-1],yas[xend:len(ls)-1]))
    #    print (len(ls) - (i))
    #    i += 1
    trace = go.Scatter(x = ls, y = os)
    data = [trace]
    py.iplot(data, filename='dataInterpolationAssignment-LSA')

#Algorithm from http://blog.ivank.net/interpolation-with-cubic-splines.html
def evalCublicSplines(x, xs, ys):

    i = 1
    while(xs[i] < x and i < len(xs) - 1):
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
        sxx += xs[i] * xs[i]
        sxy += xs[i] * ys[i]
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