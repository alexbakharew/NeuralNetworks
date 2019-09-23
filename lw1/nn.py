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
    with open("input.txt", encoding='utf-8') as input_file:
        X = input_file.readline().split(" ")
        Y = input_file.readline().split(" ")
        print(X)
        print(Y)

        if len(X) != len(Y):
            print("Incorrect input data. Exit")
            exit(-1)
        for i in range(len(X)):
            x_raw = str(X[i])
            y_raw = str(Y[i])
            x = float(x_raw.strip("\""))
            y = float(y_raw)

            points.append([x,y])
    
    print(points)




    neuro = Neuron(2)

if __name__ == "__main__":
    main()

