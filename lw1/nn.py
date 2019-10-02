import random
import math

class Neuron(object):
    def __init__(self, feature_num, learn_speed):
        self.feature_num = feature_num
        # self.weights = [1 / random.randrange(-10, 10)]# define b
        self.weights = [(1 / random.randrange(1, 100)) for _ in range(feature_num + 1)]
        self.learn_speed = learn_speed
        print("RANDOM WEIGHTS = ", self.weights)

    def ActivationFunction(self, features):
        if len(features) + 1 != len(self.weights):
            exit(-1)
            
        res = float(self.weights[0])
        for i, w in zip(features, self.weights[1:]):
            res += i * w
        return 1 if res < 0 else 0

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
                        for i in range(1, len(self.weights)):
                            self.weights[i] -= self.learn_speed
                    else: # 0 1
                        for i in range(1, len(self.weights)):
                            self.weights[i] += self.learn_speed
        print("Weights after learning ", self.weights)

    def Predict(self, features, label):
        if len(features) + 1 != len(self.weights):
            print("Incorrect feature input")
            exit(-1)
        return self.ActivationFunction(features) 

        # print("point = {}, label = {}, pred_label = {}".format(features, label, predicted_label))

    # def ShowPlot(self):

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
        
    neuro = Neuron(2, 0.01)
    neuro.Learn(50, points, classes)

    error = 0
    print("TRYING TO PREDICT TRAIN DATA")
    for point, label in zip(points, classes):
        pred_lbl = neuro.Predict(point, label)
        error += pred_lbl - label
        print("point = {}, label = {}, pred_label = {}".format(point, label, pred_lbl))
    print("error = {}".format(abs(error)))

    print("TRYING TO PREDICT RANDOM DATA")

if __name__ == "__main__":
    main()

