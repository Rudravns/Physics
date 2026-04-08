from typing import *
import math
from dataclasses import dataclass
import numpy as np
from pygame import Rect as PygameRect
from .constants import *  


class Rect:
    __slots__ = ['_x', '_y', '_width', '_height']

    def __init__(self, x: float, y: float, width: float, height: float):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

        WORLD_OJECTS["WORLD 1"].append(self)  # Add this object to the world objects list

    # ---------- Properties ----------
    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float):
        self._y = value

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value

    # ---------- Utility ----------
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


class DynamicRect(Rect):
    def __init__(self, x: float, y: float, width: float, height: float, mass: float = 1.0, friction: float = FRICTION_COEFFICIENT):
        super().__init__(x, y, width, height)
        self.mass = mass
        self.friction = friction
        self.vx = 0.0
        self.vy = 0.0
        self.ax = 0.0
        self.ay = GRAVITY

    def update(self, dt: float):
        """Using fricction and force to update the velocity and position of the rectangle"""
        # Update velocity based on acceleration
        self.vx += self.ax * dt
        self.vy += self.ay * dt

        # Apply friction (simple model)
        self.vx *= (1 - self.friction * dt)
        self.vy *= (1 - self.friction * dt)

        # Update position based on velocity
        self.x += self.vx * dt
        self.y += self.vy * dt
        


    
    @property
    def velocity(self) -> Tuple[float, float]:
        return (self.vx, self.vy)
    
    @velocity.setter
    def velocity(self, value: Tuple[float, float]):
        self.vx, self.vy = value
    
    @property
    def acceleration(self) -> Tuple[float, float]:
        return (self.ax, self.ay)
    
    @acceleration.setter
    def acceleration(self, value: Tuple[float, float]):
        self.ax, self.ay = value

    def get_pygame_rect(self) -> PygameRect:
        return PygameRect(int(self.x), int(self.y), int(self.width), int(self.height))
    

class StaticRect(Rect):
    def __init__(self, x: float, y: float, width: float, height: float):
        super().__init__(x, y, width, height)

    def get_pygame_rect(self) -> PygameRect:
        return PygameRect(int(self.x), int(self.y), int(self.width), int(self.height))


class KinematicRect(Rect):
    def __init__(self, x: float, y: float, width: float, height: float):
        super().__init__(x, y, width, height)
        self.vx = 0.0
        self.vy = GRAVITY

    def update(self, dt: float):
        self.x += self.vx * dt
        self.y += self.vy * dt

    @property
    def velocity(self) -> Tuple[float, float]:
        return (self.vx, self.vy)

    @velocity.setter
    def velocity(self, value: Tuple[float, float]):
        self.vx, self.vy = value

    def get_pygame_rect(self) -> PygameRect:
        return PygameRect(int(self.x), int(self.y), int(self.width), int(self.height))