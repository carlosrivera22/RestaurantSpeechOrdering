from interfaces.menu_interfaces.abstract_action import AbstractAction
from classes.menu_classes.place_order_menu import PlaceOrderMenu
from ..data_manager.dm_component import DataManager

class PlaceOrderAction(AbstractAction):

    def execute(self,arg):
        dm = arg
        dm.get_menu_stack().push(PlaceOrderMenu())
