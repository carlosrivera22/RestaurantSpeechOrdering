import abc
from classes.data_manager.speech_recognizer import SR
"""[summary]
"""
class AbstractMenu(abc.ABC):
    def initialize_menu(self,title,options):
        """[summary]

        Arguments:
            abc {[type]} -- [description]
            title {[type]} -- [description]
            options {[type]} -- [description]
        """
        self.options = options
        self.title = title
        self.menu_str = "\n" + self.title + "\n\n"
        for i in range(0,len(self.options)):
            opt = self.options[i]
            self.menu_str += str(i+1) + "." + opt.get_description() + "\n"

        self.menu_str += "\nSelect an option number using your voice:"
        # return self.menu_str

    def display_options(self):
        print(self.menu_str)
        # return self.menu_str
    
    def represents_int(self,s):
        try: 
            int(s)
            return True
        except ValueError:
            return False

    def activate(self):
        self.display_options()

        while True:
            sr = SR()
            # selection = input("> ") 
            selection = sr.get_speech_to_text()
            if(self.represents_int(selection) and int(selection) <= len(self.options)):  
                break  
            
        return self.options[int(selection)-1]

   

    # def activate(self,selection):
    #     # print(selection)
    #     # print(self.options[int(selection)-1].get_action())
    #     # print(self.options[int(selection)-1].get_description())
    #     return self.options[int(selection)-1]

    def add_option(option):
        raise NotImplementedError


    def get_selection_from_user():
        raise NotImplementedError


        
