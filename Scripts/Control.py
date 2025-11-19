from ControlSimulation import Simulation
from Car import Car
import math
import turtle
import time
#import PyQt

def getAngle(car:Car):
    return (car.GetDirection() - math.pi*0.5) * (180/math.pi)

def getDisp(car:Car):
    return math.sqrt(math.pow(car.GetPosition()[0] - car.GetPrevPosition()[0], 2) + math.pow(car.GetPosition()[1] - car.GetPrevPosition()[1], 2))

screen = turtle.Screen()
t = turtle.Turtle()

car = Car()
simulation = Simulation(car)
car.SetAcceleration(1.0)
car.SetVelocity([1.0, 0.0])
#car.SetDirection(math.pi*0.75)

for a in range(200):
    time.sleep(0.75)
    car.SetDirection((a * 0.1 * math.pi) % math.pi * 2)
    simulation.stepForward()
    car.PrintValues()

    t.setheading(getAngle(car))
    t.forward(getDisp(car)*1000)

time.sleep(60)