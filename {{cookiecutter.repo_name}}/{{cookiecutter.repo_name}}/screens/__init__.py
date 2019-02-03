from enum import Enum

from .homescreen import HomeScreen

class SCREENS(Enum):
    HOME = 1


screen_type = {
    SCREENS.HOME: HomeScreen,
}
