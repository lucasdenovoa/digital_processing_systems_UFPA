import numpy as np
import matplotlib.pyplot as plt

t=np.arange(-10,11,1)

def impulse(shift, amplitude):
    delta = []
    for i in t:
        if i==shift:
            delta.append(amplitude*1)
        else:
            delta.append(0)

    return delta

def sum_impulse(array_of_impulses):
    return [sum(x) for x in zip(*array_of_impulses)]

def reflection_impulse(array_of_impulses):
    for x in array_of_impulses:
        for y in x:
            y = -y




def main():
    imp1 = impulse(0,1)
    imp2 = impulse(1,2)

    todos.append(imp1)
    todos.append(imp2)
    
    plt.stem(t, sum_impulse(todos))

    plt.show()

    
    
if __name__ == "__main__":
    main()
