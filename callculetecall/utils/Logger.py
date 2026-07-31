import os

class Logger:
    
    def __init__(self):
        if not os.path.exists("callculetecall/loggs.txt"):
            with open("callculetecall/loggs.txt", 'w') as file:
                pass
    
    def _write(self,level, messeg):
        
        with open("callculetecall/loggs.txt", 'a') as file:
                    
            file.write(f'\n{level} {messeg}\n')
    
    def info(self,log):
        
       self._write('INFO',log)
        
    def error(self,log):
        
       self._write('ERROR',log)
        
    def warning(self,log):
        
       self._write('WARNING',log)
        
      
    
       
            












