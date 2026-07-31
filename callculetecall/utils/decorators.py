



def log(func):
         
    def wrapper(*args,**kwargs):
        
        
        self = args[0]   
        
        self.logger.info(f"START -> {func.__name__}")
        
        try:
            
           result = func(*args, **kwargs)
             
           self.logger.info(f"END -> {func.__name__}")
             
           return result
       
        except Exception as ex:
            
            self.logger.error(
                f"ERROR -> {func.__name__}: {ex}"
                )
            
            raise
      
    return wrapper