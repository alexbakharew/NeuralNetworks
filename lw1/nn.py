import random

class Neuron(object):
    def __init__(self, input_num):
        InputNumber = input_num
        weight = [random.randrange(-10, 10) for i in range(InputNumber)]
        print(weight)

    def Learn(self, Epochs, InputList, ClassList):
        x = 4
    def Predict(Input):
        x = 2

def main():
    points = []
    classes = []
    with open("input.txt", encoding='utf-8') as input_file:
        X = input_file.readline().strip("\n").split(" ")
        Y = input_file.readline().strip("\n").split(" ")

        if len(X) != len(Y):
            print("Incorrect input data. Exit")
            exit(-1)
        for i in range(len(X)):
            points.append([float(X[i]), float(Y[i])])
    
    with open("classes.txt", encoding='utf-8') as input_class_file:
        classes = input_class_file.readline().split(" ")
        
    print(points)
    print(classes)

    neuro = Neuron(2)
    neuro.Learn(50, points, classes)


if __name__ == "__main__":
    main()

