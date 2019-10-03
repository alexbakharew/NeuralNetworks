import random
import math
import matplotlib.pyplot as plt

class Neuron(object):
    def __init__(self, feature_num, learn_speed):
        self.feature_num = feature_num
        self.weights = [(random.randrange(1, 10)) for _ in range(feature_num + 1)]
        self.learn_speed = learn_speed
        print("RANDOM WEIGHTS = ", self.weights)

    def ActivationFunction(self, features):
        if len(features) + 1 != len(self.weights):
            exit(-1)
            
        res = float(self.weights[0])
        for i, w in zip(features, self.weights[1:]):
            res += i * w
        return 1 if res > 0 else 0

    def Learn(self, epochs, features, labels):
        if len(features) != len(labels):
            print("features list and labels list not equal")
            exit(-1)
            
        for _ in range(epochs):
            for point, label in zip(features, labels):
                pred_label = self.ActivationFunction(point)

                if pred_label == label:
                    continue
                else:
                    if pred_label > label: # 1 0
                        self.weights[0] -= self.learn_speed
                        for i in range(1, len(self.weights)):
                            self.weights[i] -= self.learn_speed * point[i - 1]
                    else: # 0 1
                        self.weights[0] += self.learn_speed
                        for i in range(1, len(self.weights)):
                            self.weights[i] += self.learn_speed * point[i - 1]
                            
        print("Weights after learning ", self.weights)

    def Predict(self, features, label):
        if len(features) + 1 != len(self.weights):
            print("Incorrect feature input")
            exit(-1)
        return self.ActivationFunction(features) 


    def ShowPlot(self, points, labels):
        x_value = []
        y_value = []

        plt.plot([-10, 10], [0, 0]) #x axis

        plt.plot([0, 0], [-50, 50]) # y axis

        i = -5
        while i <=5: # draw line between classes
            x_value.append(i)
            y_value.append(-((self.weights[0] + self.weights[1] * i) / self.weights[2]))
            i += 0.01
        plt.plot(x_value, y_value)

        #draw classes
        plt.scatter([p[0] for p in points], [p[1] for p in points], c=[c for c in labels])

        plt.show()

class NeuralNetwork(object):
    def __init__(self, neuron_count, feature_num, learn_speed):
        self.neurons = [Neuron(feature_num, learn_speed) for i in range(neuron_count)]

def ReadPoints(file_name):
    points = []
    with open(file_name, encoding='utf-8') as input_file:
        X = input_file.readline().strip("\n").split(" ")
        Y = input_file.readline().strip("\n").split(" ")

        if len(X) != len(Y):
            print("Incorrect input data. Exit")
            exit(-1)
        for i in range(len(X)):
            points.append([float(X[i]), float(Y[i])])
    return points

def ReadLabels(file_name):
    labels = []
    with open("classes.txt", encoding='utf-8') as input_class_file:
        labels = input_class_file.readline().split(" ")
    for i in range(len(labels)):
        labels[i] = int(labels[i])
    return labels

def main():
    points = ReadPoints("input.txt")
    classes = ReadLabels("classes.txt")
        
    neuro = Neuron(2, 0.1)
    neuro.Learn(50, points, classes)

    error = 0
    print("TRYING TO PREDICT TRAIN DATA")
    for point, label in zip(points, classes):
        pred_lbl = neuro.Predict(point, label)
        error += abs(pred_lbl - label)
        print("point = {}, label = {}, pred_label = {}".format(point, label, pred_lbl))
    print("error = {}".format(abs(error)))

    neuro.ShowPlot(points, classes)
    # print("TRYING TO PREDICT RANDOM DATA")

if __name__ == "__main__":
    main()

