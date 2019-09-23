import random

class Neuron(object):
    def __init__(self, input_num):
        InputNumber = input_num
        weight = [random.randrange(-10, 10) for i in range(InputNumber)]
        print(weight)

    def Learn(Epochs, InputList, ClassList):
        x = 4
    def Predict(Input):
        x = 2

def main():
    points = []
    with open("input.txt") as input_file:
        arr = input_file.readline()
    
    print(points)




    neuro = Neuron(2)

if __name__ == "__main__":
    main()

