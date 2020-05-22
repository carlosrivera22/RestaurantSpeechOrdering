from interfaces.menu_interfaces.menu import AbstractMenu
from classes.menu_classes.option import Option
from classes.menu_classes.exit_action import ExitAction
from classes.menu_classes.side_action import SideAction
from classes.menu_classes.main_dishes_action import MainDishesAction
from classes.menu_classes.drink_action import DrinkAction
from classes.menu_classes.submit_action import SubmitAction
class PlaceOrderMenu(AbstractMenu):

    def __init__(self):
        self.title = "MAKE ORDER:"
        self.options = []
        self.options.append(Option("Select Main Dish",MainDishesAction()))
        self.options.append(Option("Select Sides",SideAction()))
        self.options.append(Option("Select Drinks",DrinkAction()))
        self.options.append(Option("Submit Order",SubmitAction()))
        self.options.append(Option("Back to Main Menu",ExitAction()))

        super().initialize_menu(self.title,self.options)

    # def display_menu(self):
    #     return super().initialize_menu(self.title,self.options)
    