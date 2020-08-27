from matplotlib import pyplot as plt
import math

def drawGraph(xCoordinates, yCoordinates):
    figure = plt.figure()

    graph = figure.add_subplot(111)

    graph.plot(xCoordinates, yCoordinates, color = 'lightcoral')
    graph.set_xlabel('Distance')
    graph.set_ylabel('Height')
    graph.legend(['Trajectory'])

    plt.show()

def frange(start, final, interval):
    numbers = []

    while start < final:
        numbers.append(start)
        start = start + interval

    return(numbers)

def drawTrajectory(velocity, theta):
    theta = math.radians(theta)
    #gracAvv is gravitational acceleration, or his "g"
    gravAcc = 9.8

    tFlight = 2*velocity*math.sin(theta)/9
    intervalsForFrange = frange(0, tFlight, 0.001)

    xCoordinates = []
    yCoordinates = []

    for time in intervalsForFrange:
        xCoordinates.append(velocity*math.cos(theta)*time*time)
        yCoordinates.append(velocity*math.sin(theta)*time - 0.5*gravAcc*time*time)

    drawGraph(xCoordinates, yCoordinates)


if __name__ == "__main__":
    try:
        # "velocity" is his "u"
        velocity = float(input('Enter the initial velocity (in m/s) : '))
        theta = float(input('Enter the angle of projection (in degrees) : '))
        drawTrajectory(velocity, theta)

    except Exception as error:
        print(error)

    finally:
        print(f":)")