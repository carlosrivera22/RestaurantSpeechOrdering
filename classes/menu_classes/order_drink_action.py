from interfaces.menu_interfaces.abstract_action import AbstractAction
from ..data_manager.dm_component import DataManager
from classes.menu_classes.menu_item import MenuItem

class CocaColaAction(AbstractAction):
    def execute(self,arg):
        dm = arg
        dm.get_menu_stack().pop()
        dm.get_items().append(MenuItem("Coca Cola",1.25))
        dm.display_order()

class SpriteAction(AbstractAction):
    def execute(self,arg):
        dm = arg
        dm.get_menu_stack().pop()
        dm.get_items().append(MenuItem("Sprite",1.25))
        dm.display_order()


class WaterAction(AbstractAction):
    def execute(self,arg):
        dm = arg
        dm.get_menu_stack().pop()
        dm.get_items().append(MenuItem("Water",1.25))
        dm.display_order()