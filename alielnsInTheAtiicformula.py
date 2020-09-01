from matplotlib import pyplot as plt
import math

def frange(start, final, increment):
    numbers = []

    while start < final:
        numbers.append(start)
        start = start + increment

    return(numbers)

def drawGraph(xCoordinatesList, yCoordinatesList):
    figure = plt.figure()

    graph = figure.add_subplot(111)

    for turns in range(0,len(xCoordinatesList)):
        graph.plot(*xCoordinatesList[turns], *yCoordinatesList[turns])
        # print(*xCoordinatesList[turns], *yCoordinatesList[turns])

    graph.set_xlabel('Distance')
    graph.set_ylabel('Height')
    graph.legend(['Trajectory'])

    plt.show()

def drawParabola(velocity, theta):
    theta = math.radians(theta)

    #gracAvv is gravitational acceleration, or his "g"
    gravAcc = 9.8

    tFlight = 2*velocity*math.sin(theta)/gravAcc
    intervalsForFrange = frange(0, tFlight, 0.001)

    xCoordinates = []
    yCoordinates = []

    for time in intervalsForFrange:
        xCoordinates.append(velocity*math.cos(theta)*time)
        yCoordinates.append(velocity*math.sin(theta)*time - 0.5*gravAcc*time*time)

    return(xCoordinates, yCoordinates)    

def drawTrajectory(numberOfTimes, velocityList, thetaList):
    # "velocity" is his "u"
    xCoordinatesList = []
    yCoordinatesList = []

    for turn in range(0,numberOfTimes):
        xList, yList = drawParabola(velocityList[turn], thetaList[turn])
        xCoordinatesList.append(xList)
        yCoordinatesList.append(yList)

    drawGraph(xCoordinatesList, yCoordinatesList)
    return(True)



if __name__ == "__main__":
    try:

        numberOfTimes = int(input("How mnay trajectories do you want drawn? : "))
        velocityList = []
        thetaList = []

        for loopNumber in range(0,numberOfTimes):
            velocity = float(input('Enter the initial velocity (in m/s) : '))
            velocityList.append(velocity)
            theta = float(input('Enter the angle of projection (in degrees) : '))
            thetaList.append(theta)

        drawTrajectory(numberOfTimes, velocityList, thetaList)

    except Exception as error:
        print(error)

    finally:
        print(f":)")