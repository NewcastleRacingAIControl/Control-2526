from ControlSimulation import Simulation
from Car import Car
import math

car = Car()
simulation = Simulation(car)
car.SetAcceleration(1)
#car.SetDirection(math.pi*0.75)

for a in range(20):
    car.SetDirection()
    simulation.stepForward()
    car.PrintValues()