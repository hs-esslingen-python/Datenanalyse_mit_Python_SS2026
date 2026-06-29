# Dies ist ein Python-Skript.


from src import inc_dec
#from _30_Verschiedenes.VSCode_Pytest_example.src import add 
from src import add

def run_my_function():
    print("Hallo - Dies ist die Funktion run_my_function:.")
    
    print(f"inc_dec.increment(5): {inc_dec.increment(5)}")
    print(f"inc_dec.decrement(3): {inc_dec.decrement(3)}")
    print(f"add.addition(7, 3): {add.addition(7, 3)}")


if __name__ == '__main__':
    print('VSCode and Pytest')
    print(f"__name__ = {__name__} - Dies ist die main.py Datei.")

    run_my_function()


