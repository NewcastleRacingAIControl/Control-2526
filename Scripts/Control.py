from ControlSimulation import Simulation
from Car import Car
import math
import turtle

car = Car()
simulation = Simulation(car)
car.SetAcceleration(1.0)
#car.SetDirection(math.pi*0.75)

for a in range(20):
    car.SetDirection(a * 0.01 * math.pi)
    simulation.stepForward()
    car.PrintValues()