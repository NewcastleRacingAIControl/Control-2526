import Car
import math

class Simulation:

    def __init__(self, car:Car):
        self.car = car
        self.interval = 0.05
        self.acc = 5.0

    def stepForward(self):
        pos = self.car.GetPosition()
        dir = self.car.GetDirection()
        acc = self.car.GetAcceleration()
        vel = self.car.GetVelocity()

        accX = math.cos(dir + math.pi/2) * acc
        accY = math.sin(dir + math.pi/2) * acc

        acc = [accX * self.acc, accY * self.acc]

        #pos = pos + (vel * self.interval) + (0.5*acc*math.pow(self.interval, 2))
        pos = [pos[0] + vel[0] * self.interval + 0.5*acc[0]*math.pow(self.interval, 2), pos[1] + vel[1] * self.interval + 0.5*acc[1]*math.pow(self.interval, 2)]
        vel = [vel[0] + acc[0] * self.interval, vel[1] + acc[1] * self.interval]

        self.car.SetPosition(pos)
        self.car.SetVelocity(vel)