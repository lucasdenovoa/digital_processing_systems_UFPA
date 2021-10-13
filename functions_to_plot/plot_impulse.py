import numpy as np
import matplotlib.pyplot as plt

number_of_sample=np.arange(-10,11,1)

def impulse(shift, amplitude):
    delta = []
    for i in number_of_sample:
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
    impulse_set = []

    impulse_set.append(impulse(0,1))
    impulse_set.append(impulse(1,2))
    
    plt.stem(number_of_sample, sum_impulse(impulse_set))

    plt.show()

    
    
if __name__ == "__main__":
    main()
