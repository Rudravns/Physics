# Simplify imports for the user
from .rects import *
# Define what is exported during 'from my_package import *'
__all__ = ["DynamicRect", "StaticRect", "KinematicRect"]

__version__ = "0.1.0"
__author__ = "Rudransh Kumar"
__description__ = "A simple physics engine for 2D games"