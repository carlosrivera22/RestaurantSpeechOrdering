from interfaces.menu_interfaces.abstract_action import AbstractAction
from ..data_manager.dm_component import DataManager
from classes.menu_classes.menu_item import MenuItem

class ChipsAction(AbstractAction):

    def execute(self,arg):
        dm = arg
        dm.get_menu_stack().pop()
        dm.get_items().append(MenuItem("Chips",1.25))
        dm.display_order()

class FriesAction(AbstractAction):

    def execute(self,arg):
        dm = arg
        dm.get_menu_stack().pop()
        dm.get_items().append(MenuItem("French Fries",1.25))
        dm.display_order()

class BatatasAction(AbstractAction):

    def execute(self,arg):
        dm = arg
        dm.get_menu_stack().pop()
        dm.get_items().append(MenuItem("Onion Rings",1.25))
        dm.display_order()


