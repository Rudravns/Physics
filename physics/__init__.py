# Simplify imports for the user
from .rects import *
from .constants import *
# Define what is exported during 'from my_package import *'
__all__ = ["DynamicRect", "StaticRect", "KinematicRect",
            "GRAVITY", "AIR_DENSITY", "FRICTION_COEFFICIENT", "WORLD_OJECTS"
            
            ]

__version__ = "0.1.0"
__author__ = "Rudransh Kumar"
__description__ = "A simple physics engine for 2D games"