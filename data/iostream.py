from termcolor import colored
class iostream:
    def out(content, color, backgroundColor, attrs=[]):
        print(colored(content, color, backgroundColor, attrs))