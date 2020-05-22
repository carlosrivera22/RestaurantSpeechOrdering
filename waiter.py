#Here goes the main function
from classes.data_manager.dm_component import DataManager
from classes.stack import Stack
from classes.menu_classes.main_menu import MainMenu
from classes.menu_classes.option import Option
class Waiter:

    if __name__ == "__main__":
        dm = DataManager()
        mstack = dm.get_menu_stack()
        mstack.push(MainMenu())
        greeting = "\nGreetings!  Welcome to Pepe's Restaurant!\n"
        print(greeting)
        while not mstack.isEmpty():
            opt = mstack.peek().activate()
            opt.get_action().execute(dm)

