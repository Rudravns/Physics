from typing import *
import math
from dataclasses import dataclass
import numpy as np
from pygame import Rect as PygameRect

@dataclass
class Rect:
    x: float
    y: float
    width: float
    height: float

    def get_corners(self) -> List[Tuple[float, float]]:
        return [
            (self.x, self.y),
            (self.x + self.width, self.y),
            (self.x, self.y + self.height),
            (self.x + self.width, self.y + self.height)
        ]
    
    def get_rect(self) -> Tuple[float, float, float, float]:
        return (self.x, self.y, self.width, self.height)
    
    def move(self, dx: float, dy: float):
        self.x += dx
        self.y += dy

    @property
    def area(self) -> float:
        return self.width * self.height
    
    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    @x.setter
    def x(self, value: float):
        self._x = value

    @y.setter
    def y(self, value: float):
        self._y = value

    @width.setter
    def width(self, value: float):
        self._width = value

    @height.setter
    def height(self, value: float):
        self._height = value

    @x.getter
    def x(self) -> float:
        return self._x
    
    @y.getter
    def y(self) -> float:
        return self._y
    
    @width.getter
    def width(self) -> float:
        return self._width
    
    @height.getter
    def height(self) -> float:
        return self._height
    
class DynamicRect(Rect):
    def __init__(self, x: float, y: float, width: float, height: float):
        super().__init__(x, y, width, height)
        """Initialize velocity and acceleration for dynamic rectangles.
        """
        self.vx = 0.0
        self.vy = 0.0
        self.ax = 0.0
        self.ay = 0.0

    def update(self, dt: float):
        """Update the position of the rectangle based on its velocity and acceleration.
        """
        self.vx += self.ax * dt
        self.vy += self.ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
    
    @property
    def velocity(self) -> Tuple[float, float]:
        return (self.vx, self.vy)
    
    @property
    def acceleration(self) -> Tuple[float, float]:
        return (self.ax, self.ay)
    
    @velocity.setter
    def velocity(self, value: Tuple[float, float]):
        self.vx, self.vy = value
    
    @acceleration.setter
    def acceleration(self, value: Tuple[float, float]):
        self.ax, self.ay = value

    def get_pygame_rect(self) -> PygameRect:
        """Convert to a Pygame Rect for rendering or collision detection.
        """
        return PygameRect(int(self.x), int(self.y), int(self.width), int(self.height))
    
class StaticRect(Rect):
    def __init__(self, x: float, y: float, width: float, height: float):
        super().__init__(x, y, width, height)

    def get_pygame_rect(self) -> PygameRect:
        """Convert to a Pygame Rect for rendering or collision detection.
        """
        return PygameRect(int(self.x), int(self.y), int(self.width), int(self.height))



class KinematicRect(Rect):
    def __init__(self, x: float, y: float, width: float, height: float):
        super().__init__(x, y, width, height)
        self.vx = 0.0
        self.vy = 0.0

    def update(self, dt: float):
        """Update the position of the rectangle based on its velocity.
        """
        self.x += self.vx * dt
        self.y += self.vy * dt

    @property
    def velocity(self) -> Tuple[float, float]:
        return (self.vx, self.vy)

    @velocity.setter
    def velocity(self, value: Tuple[float, float]):
        self.vx, self.vy = value

    def get_pygame_rect(self) -> PygameRect:
        """Convert to a Pygame Rect for rendering or collision detection.
        """
        return PygameRect(int(self.x), int(self.y), int(self.width), int(self.height))

    