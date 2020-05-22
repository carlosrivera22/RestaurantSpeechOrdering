from interfaces.menu_interfaces.menu import AbstractMenu
from classes.menu_classes.exit_action import ExitAction
from classes.menu_classes.option import Option
from classes.menu_classes.order_drink_action import *
class DrinkMenu(AbstractMenu):

    def __init__(self):
        self.title = "DRINKS:"
        self.options = []
        self.options.append(Option("Coca Cola",CocaColaAction()))
        self.options.append(Option("Sprite",SpriteAction()))
        self.options.append(Option("Water",WaterAction()))
        self.options.append(Option("Back",ExitAction()))

        super().initialize_menu(self.title,self.options)

    
