import matplotlib.pyplot as plt
import numpy as np


def ex1():

    randomData = np.random.uniform(0, 101, 25)

    print(randomData)

    randomData[randomData.argmax()] = 200

    randomData[randomData<50] = 0

    print(randomData)

def ex2():

    randomMatrix = np.random.randint(-100, 101, (9,9))
    
    print(np.sort(randomMatrix[np.mod(randomMatrix, 2) == 0]))


def ex3():

    angles = np.arange(0, 3 * np.pi, 0.1)
    sines = np.sin(angles)
    cosines = np.cos(angles)

    crossPoints = angles[np.abs(np.sin(angles) - np.cos(angles)) < 0.1]

    print(crossPoints)

    fig = plt.figure(1)

    ax = fig.add_subplot()
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.plot(angles, sines, color = 'blue', zorder = 0)
    plt.plot(angles, cosines, color = 'green', zorder = 0)
    plt.scatter(crossPoints, np.sin(crossPoints), color = 'red', zorder = 10)
    plt.scatter(crossPoints, np.cos(crossPoints), color = 'red', zorder = 10)

    plt.xticks(np.arange(-2, 11, 2))
    plt.yticks(np.arange(-1.5, 1.6, 0.5))

    plt.show()

def ex4():

    cartesian = np.random.uniform(-1., 1., (500, 2))

    r = np.sqrt(cartesian[:,0] ** 2 - cartesian[:,1] ** 2)

    angles = np.arctan2(cartesian[:,1], cartesian[:,0])

    fig = plt.figure(2)

    ax = fig.add_subplot()

    plt.scatter(cartesian[:,0], cartesian[:,1] )

    plt.show()

ex4()
#ex3()
#ex2()
#ex1()