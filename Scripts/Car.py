import math

class Car:

    def __init__(self):
        self.__position = [0, 0]
        self.__acceleration = 0
        self.__direction = 0
        self.__velocity = [0, 0]
        self.__drag = 0.2

    #gets and sets
    def GetPosition(self):
        return self.__position
    def GetAcceleration(self):
        return self.__acceleration
    def GetDirection(self):
        return self.__direction
    def GetVelocity(self):
        return self.__velocity
    def GetDirectionDegrees(self):
        radians = self.__direction * (180 / math.pi)
        return radians

    def SetPosition(self, newPosition):
        if not isinstance(newPosition, list):
            raise KeyError("Error, position has to be a list, [x, y]")
        self.__position = newPosition

    def SetAcceleration(self, newAcceleration):
        if not isinstance(newAcceleration, float):
            raise KeyError("Error, acceleration has to be a float")

        if newAcceleration < -1 or newAcceleration > 1:
            raise KeyError("Error, acceleration has to be between -1 and 1")
        self.__acceleration = newAcceleration

    def SetVelocity(self, newVelocity):
        if not isinstance(newVelocity, list):
            raise KeyError("Error, velocity should be a list, [vx, vy]")
        self.__velocity = newVelocity

    def SetDirection(self, newDirection):
        if not isinstance(newDirection, float):
            raise KeyError("Error, direction has to be a float")
        if newDirection > (2 * math.pi) or newDirection < 0:
            raise KeyError("Error, direction is in radians, must be between zero and 2 pie")

    def SetDirectionDegrees(self, newDirection):
        if not isinstance(newDirection, float):
            raise KeyError("Error, direction has to be a float")
        if newDirection > 360 or newDirection < 0:
            raise KeyError("Error, direction is in degrees, must be between 0 and 360")
        self.__direction = newDirection * (math.pi / 180)


    def Update(self, dt):
        # forward directions
        fx = math.cos(self.__direction)
        fy = math.sin(self.__direction)

        # acceleration directions
        ax = self.__acceleration * fx
        ay = self.__acceleration * fy

        # velocity updates
        self.__velocity[0] += ax * dt
        self.__velocity[1] += ay * dt

        # apply drag
        self.__velocity[0] *= (1 - self.__drag) * dt
        self.__velocity[1] *= (1 - self.__drag) * dt

        # position updates
        self.__position[0] += self.__velocity[0] * dt
        self.__position[1] += self.__velocity[1] * dt

    def PrintValues(self):
        print("----------------------------------")
        print("Car position: " + self.__position)
        print("Car acceleration: " + self.__acceleration)
        print("Car direction: " + self.__direction)
        print("Car velocity: " + self.__velocity)
        print("----------------------------------")

