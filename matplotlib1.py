
import matplotlib.pyplot as plt
from matplotlib import cm, colors
import numpy as np

def lineChart():

    x = [1,2,3,4]

    y = [3,4.5,7,8]

    y2 = [3,7,4.5,8]

    plt.plot(x,y, 'r--^', label = 'funkcja 2')

    plt.plot(x,y2, 'g--o', label = 'funkcja 1')

    plt.xlabel('Parametr X')
    plt.ylabel('Parametr Y')

    plt.title('Wykres - XY')


    plt.xlim(0.5, 4.5)
    plt.xticks(x)

    plt.ylim(2.5, 8.6)
    plt.yticks(y2)

    plt.legend(loc = 'upper left')
    
    plt.show()

def scatterChart():


    f = open('scatter.txt', 'r')
    angles, distances = f.readlines()

    f.close()

    angles = angles.split()
    distances = distances.split()

    angles = [float(num) for num in angles]  
    distances = [abs(float(num)) for num in distances]  

    fig = plt.figure(1)

    ax = fig.add_subplot(polar = True)

    scattered = ax.scatter(angles, distances, c = distances, cmap = 'jet', s = 6)


    ax.set_facecolor('lightgray')
    plt.ylim(0,1.4)

    plt.show()

def barChart():
    
    f = open('bars.txt', 'r')

    x, y = f.readlines()

    x = x.split()
    x = [int(num) for num in x]

    y = y.split()
    y = [float(num) for num in y]

    fig = plt.figure(2)

    c = cm.copper(y)

    ax = fig.add_subplot()

    bars = ax.bar(x,y,align = 'edge', color = c)

    plt.bar_label(bars)
    plt.xlim(0,12)
    plt.ylim(0,1)
    plt.tick_params(top = True, right = True, direction = 'in')
    plt.show()

def pieChart():

    f = open('pie.txt', 'r')
    data = [float(x) for x in ((f.readline()).split())]

    distance = [0.03,0.03,0.03,0.03,0.03]
    colorList = cm.terrain(np.arange(0.0, 1.0, 0.2))

    fig = plt.figure(3)

    ax = fig.add_subplot()

    ax.pie(data, explode = distance, colors = colorList)

    plt.show()

def ex2():

    f = open('data2.dat')

    data = [float(num) for num in ((f.readlines()))]
    print(data)


ex2()
#ex3()
#lineChart()
#scatterChart()
#barChart()
#pieChart()