from utils.Clear import clear
from utils.commandsExcept import BackToMenu,ExitApplication
COMMANDS = frozenset({
    'help'
    'menu'
    'exit'
    'clear'
})


def parse_command(text):
    
    if not text.startswith('/') or text.startswith('//'):
        return None
    
    parts = text[1:].lower().split()
    
    if not parts:
        return None

    return parts[0], parts[1:]



def parse_and_execute_command(text):
    
    try:
        commands, args = parse_command(text)
    except:
        return None
    
    match commands,args:
        
        case 'menu',[]:
            raise BackToMenu  #еще не создано
        case 'exit',['-app']:
            raise ExitApplication #еще не создано
        case 'help',[]: #а как нам передать сюда название функции? можно заставить пользователя ввести ее название как аргумент или есть способ как в декораторе func.__name__ или чтото подобное
            return serviseHelp() #еще не создано, стоит реализовать как утилиту или добавит как сервис
        case 'help',['-all']:
            return serviseHelp(str(args)) # идея такова что когда ми пишем хелп и префикс то ми передаем его в сервисХелп а тот откривает собствений тхт файл в котором написано все о всем, но перед етим он находит Ид нужной строки а конкретно с помощю словаря в котором ето хранится по аналогии с бд продуктам. но в етом случаи хранится 2 значения 1 ето начало 2 конец тоисть 2 номера строк с которой читать а на которой остановится, после чего возвращает иту инфу
        case 'clear',[]:
            clear()
    
    







