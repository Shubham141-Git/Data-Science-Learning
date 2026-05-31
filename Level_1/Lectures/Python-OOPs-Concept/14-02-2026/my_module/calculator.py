import time

def hello_world():
    print("hello world")

class Calulcator:
    def __init__(self):
        self.__history = []

    def add(self, *args):
        total = 0
        for i in args:
            total+=i
        
        t = time.time()

        self.__history.append({f"Add_{t}" : {str(args) : total}})
        return total
    
    def get_history(self):
        print(self.__history)

if __name__ == "__main__": #this will execute o`nly when this file is run directly, not when imported
    c = Calulcator()
    print(c.add(2, 3))
    c.get_history()
    hello_world()