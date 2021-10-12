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
        print("antes", x)
        for y in x:
            y = -y


imp1 = impulse(-2,1)
imp2 = impulse(-1,2)
imp3 = impulse(0,3)
imp4 = impulse(1,4)
imp5 = impulse(2,5)
imp6 = impulse(3,6)



todos = []

todos.append(imp1)
todos.append(imp2)
todos.append(imp3)
todos.append(imp4)
todos.append(imp5)
todos.append(imp6)


reflection_impulse(todos)


plt.stem(t, sum_impulse(todos))


plt.show()
