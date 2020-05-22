from interfaces.menu_interfaces.abstract_action import AbstractAction
from classes.menu_classes.side_menu import SideMenu
from ..data_manager.dm_component import DataManager

class SideAction(AbstractAction):

    def execute(self,arg):
        dm = arg
        dm.get_menu_stack().push(SideMenu())
