from utils.Clear import clear
from utils.decorators import log
from exceptions.navigation import BackToMenu,ExitApplication

class Commands:
    def __init__(self, HelpServise,logger):
        self.helpServise = HelpServise
        self.logger = logger
        
    
    def parse_command(self,text):
        
        if not text.startswith('/') or text.startswith('//'):
            return None
        
        parts = text[1:].lower().split()
        
        if not parts:
            return None

        return parts[0], parts[1:] if parts else None
    

    
    def parse_and_execute_command(self,text, context = None ):
        
        try:
            commands, args = self.parse_command(text)
            
        except Exception as ex:
            self.logger.warning(
                f" --> Commands {ex}"
            )
            return None
        
        match commands,args:
            
            case 'menu',[]:
                
                raise BackToMenu  
            
            case 'exit',['-app']:
                
                raise ExitApplication 
            
            case 'help',[]: 
                
                return self.helpServise.get_help(context= context) #
        
            case 'help',[argument]:
        
                return self.helpServise.get_help(argument= argument ) 
            case 'clear',[]:
                clear()
            
            case _:
                return 'Еу слиш такой команди нема'
        
    







