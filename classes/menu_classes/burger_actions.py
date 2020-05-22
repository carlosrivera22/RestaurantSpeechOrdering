from interfaces.menu_interfaces.abstract_action import AbstractAction
from ..data_manager.dm_component import DataManager
from classes.menu_classes.menu_item import MenuItem

class BeefBurgerAction(AbstractAction):

    def execute(self,arg):
        dm = arg
        dm.get_menu_stack().pop()
        dm.get_items().append(MenuItem("Beef Burger",5.25))
        dm.display_order()



class ChickenBurgerAction(AbstractAction):

    def execute(self,arg):
        dm = arg
        dm.get_menu_stack().pop()
        dm.get_items().append(MenuItem("Chicken Sandwich",5.25))
        dm.display_order()
