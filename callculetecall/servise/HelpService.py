
class HelpService:
    
    def __init__(self, path):
        
        self.path = path
        self.lines = self._load_file()
        
        self.help_args = {
            "-all" : "basecInfo"
        }
        
        
        

    def _load_file(self):
        
        with open(f"{self.path}/Help.txt", 'r', encoding="utf-8") as file:
            
            return file.readlines()


    def get_section(self, section):
        
        start = f"[{section}]"
        end = f"[\{section}]"
        
        result = []
        reading = False
        
        
        for line in self.lines:
            
            if line.strip() == start:
                reading = True
                continue
            
            if line.strip() == end:
                reading =False
                break
            
            if reading:
                result.append(line)
        
        return "".join(result)
            
    
    
    def get_help(self, context = None, argument = None):
        
        
        
        if context:
            section = context
            
        elif argument in self.help_args:
            section = self.help_args[argument]
            
        else:
            return "Help not found"
       
        return self.get_section(section)
            
        
        
                

