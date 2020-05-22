from interfaces.menu_interfaces.menu import AbstractMenu
from classes.menu_classes.option import Option
from classes.menu_classes.exit_action import ExitAction
from classes.menu_classes.place_order_action import PlaceOrderAction
from classes.menu_classes.view_order_status_action import ViewOrderStatusAction
from classes.menu_classes.contact_information_action import ContactInfoAction

class MainMenu(AbstractMenu):

    def __init__(self):
        self.title = "MAIN MENU:"
        self.options = []
        self.options.append(Option("Make Order",PlaceOrderAction()))
        self.options.append(Option("View Order Status",ViewOrderStatusAction()))
        self.options.append(Option("Contact Information",ContactInfoAction()))
        self.options.append(Option("Cancel",ExitAction()))
    
        super().initialize_menu(self.title,self.options)

    # def display_menu(self):
    #     return super().initialize_menu(self.title,self.options)