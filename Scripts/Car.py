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
    # def GetDirectionRadians(self):
    #     radians = self.__direction * (math.pi / 180)
    #     return radians

    def SetAcceleration(self, newAcceleration):
        if newAcceleration < -1 or newAcceleration > 1:
            print("Error, acceleration has to be between -1 and 1")
            return 
        self.__acceleration = newAcceleration

    def SetVelocity(self, newVelocity):
        # if (newVelocity):
        self.__velocity = newVelocity

    def SetPosition(self, newPosition):
        self.__position = newPosition

    def SetDirection(self, newDirection):
        if newDirection > (2 * math.pi) or newDirection < 0:
            print("Error, direction is in radians, must be between zero and 2 pie")
            return
        


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

        # position updates
        self.__position[0] += self.__velocity[0] * dt
        self.__position[1] += self.__velocity[1] * dt

    def PrintValues(self):
        print("Car position: " + str(self.__position))
        print("Car acceleration: " + str(self.__acceleration))
        print("Car direction: " + str(self.__direction))
        print("Car velocity: " + str(self.__velocity))

