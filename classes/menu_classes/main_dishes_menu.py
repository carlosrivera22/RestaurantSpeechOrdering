from interfaces.menu_interfaces.menu import AbstractMenu
from classes.menu_classes.option import Option
from classes.menu_classes.exit_action import ExitAction
from classes.menu_classes.burger_actions import *

class MainDishesMenu(AbstractMenu):
    def __init__(self):
        self.title = "MAIN DISHES"
        self.options = []
        self.options.append(Option("Beef Hamburger",BeefBurgerAction()))
        self.options.append(Option("Chicken Sandwich",ChickenBurgerAction()))
        self.options.append(Option("Back",ExitAction()))
    
        super().initialize_menu(self.title,self.options)
    
    # def display_menu(self):
    #     return super().initialize_menu(self.title,self.options)

    