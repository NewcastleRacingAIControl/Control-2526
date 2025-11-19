import Car
import math

class Simulation:

    def __init__(self, car:Car):
        self.car = car
        self.interval = 0.05

    def stepForward(self):
        pos = self.car.GetPosition()
        dir = self.car.GetDirection()
        acc = self.car.GetAcceleration()
        vel = self.car.GetVelocity()

        accX = math.cos(dir + math.pi/2) * acc
        accY = math.sin(dir + math.pi/2) * acc

        acc = [accX, accY]

        pos = pos + (vel * self.interval) + (0.5*acc*math.pow(self.interval, 2))
        vel = vel + acc * self.interval

        self.car.SetPosition(pos)
        self.car.SetVelocity(vel)