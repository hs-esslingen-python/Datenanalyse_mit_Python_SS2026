# This is a sample Python script.


from src import inc_dec
from src import inc 

def print_hi(name):
    print(f'Hi, {name}')  

def run_my_function():
    print("Running my functions...")
    
    print(f"inc_dec.increment(5): {inc_dec.increment(5)}")
    print(f"inc_dec.decrement(3): {inc_dec.decrement(3)}")
    print(f"inc.inc(7): {inc.inc(7)}")


if __name__ == '__main__':
    print_hi('VSCode and Pytest')

    run_my_function()


