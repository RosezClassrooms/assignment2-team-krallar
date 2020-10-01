from abc import ABC, abstractmethod
# In order to only give values for relevant attributes, you must
#   use some form of keyword argument initialization
# However, all of the attributes must be given default values
# Keep in mind that in a real application, these would be endless ...

# Is there any danger in having users decide which attributes to specify?
# What about organization and readability?  Should they all be in one place?
# Even if you didn't apply Builder, are there ways to improve this
#   keyword implementation?
class Robot:
  def __init__(self):
    self.robot_type = None
    self.traversal = list()
    self.detection_systems = list()

  # This is still awful!  What should we do about it??
  def __str__(self):
    string = f"{self.robot_type}\n"

    if self.traversal:
      string += "Traversal modules installed:\n"

    for module in self.traversal:
      string += "- " + str(module) + "\n"

    if self.detection_systems:
      string += "Detection systems installed:\n"

    for system in self.detection_systems:
      string += "- " + str(system) + "\n"

    return string

#---------------------------------------------------------------------------

# Concrete component classes
# If they are defined at this level, they would multiply like rabbits in a
#   real system, and would have an endless list of subcomponents also
# Are there better ways to manage all these components?
class BipedalLegs:
  def __str__(self):
    return "two legs"

class QuadripedalLegs:
  def __str__(self):
    return "four legs"

class Arms:
  def __str__(self):
    return "two arms"

class Wings:
  def __str__(self):
    return "wings"

class Blades:
  def __str__(self):
    return "blades"

class FourWheels:
  def __str__(self):
    return "four wheels"

class TwoWheels:
  def __str__(self):
    return "two wheels"

class CameraDetectionSystem:
  def __str__(self):
    return "cameras"

class InfraredDetectionSystem:
  def __str__(self):
    return "infrared"

 #######################################################

class RobotBuilder(ABC):
    
  @abstractmethod
  def reset(self):
    pass

  @abstractmethod
  def build_traversal(self):
    pass

  @abstractmethod
  def build_detection_system(self):
    pass

    
# Concrete Builder class:  there would be MANY of these
class AndroidBuilder(RobotBuilder):
  def __init__(self):
    self.product = Robot()
    self.product.robot_type = "ANDROID "

  def reset(self):
    self.product = Robot()

  # All of the concrete builders have this in common
  # Should it be elevated to the superclass?  
  def get_product(self):
    return self.product

  def build_traversal(self):
    self.product.traversal.append(BipedalLegs())
    self.product.traversal.append(Arms())

  def build_detection_system(self):
    self.product.detection_systems.append(CameraDetectionSystem())

# Constructing robots by providing only relevant attributes
# Note that when providing attributes via keyword, order doesn't matter!
# Is there a danger here??
class AutoBuilder(RobotBuilder):
  def __init__(self):
    self.product = Robot()
    self.product.robot_type = "AUTONOMOUS CAR "

  def reset(self):
    self.product = Robot()

  def get_product(self):
    return self.product

  def build_traversal(self):
    self.product.traversal.append(FourWheels())
  
  def build_detection_system(self):
    self.product.detection_systems.append(InfraredDetectionSystem())

  
class FlyingMonkeyBuilder(RobotBuilder):
  def __init__(self):
    self.product = Robot()
    self.product.robot_type = "FLYING MONKEY ROBOT "

  def reset(self):
    self.product = Robot()

  def get_product(self):
    return self.product

  def build_traversal(self):
    self.product.traversal.append(Wings())
    self.product.traversal.append(Arms())

  def build_detection_system(self):
    self.product.detection_systems.append(InfraredDetectionSystem())
    self.product.detection_systems.append(CameraDetectionSystem())


class Director:
    def make_robot(self, builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()

director = Director()

builder = AndroidBuilder()
print(director.make_robot(builder))

builder = AutoBuilder()
print(director.make_robot(builder))

builder = FlyingMonkeyBuilder()
print(director.make_robot(builder))
