from interfaces.menu_interfaces.menu import AbstractMenu
from classes.menu_classes.option import Option
from classes.menu_classes.exit_action import ExitAction
from classes.menu_classes.side_order_action import *

class SideMenu(AbstractMenu):

    def __init__(self):
        self.title = "SIDES:"
        self.options = []
        self.options.append(Option("French Fries",FriesAction()))
        self.options.append(Option("Onion Rings",BatatasAction()))
        self.options.append(Option("Chips",ChipsAction()))
        self.options.append(Option('Back',ExitAction()))

        super().initialize_menu(self.title,self.options)


    # def display_menu(self):
    #     return super().initialize_menu(self.title,self.options)

        