from ControlSimulation import Simulation
from Car import Car

car = Car()
simulation = Simulation(car)

while (True):
    simulation.stepForward()