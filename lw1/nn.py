import random
import math
import matplotlib.pyplot as plt

class Neuron(object):
    def __init__(self, feature_num):
        self.weights = [(random.randrange(1, 10)) / 100 for _ in range(feature_num + 1)]
        print("RANDOM WEIGHTS = ", self.weights)

    def ActivationFunction(self, feature):
        if len(feature) + 1 != len(self.weights):
            exit(-1)
            
        res = float(self.weights[0])
        for i, w in zip(feature, self.weights[1:]):
            res += i * w
        return 1 if res > 0 else 0

    def Learn(self, point, label, learn_speed):
        pred_label = self.ActivationFunction(point)
        if pred_label == label:
            return
        else:
            if pred_label > label: # 1 0
                self.weights[0] -= learn_speed
                for i in range(1, len(self.weights)):
                    self.weights[i] -= learn_speed * point[i - 1]
            else: # 0 1
                self.weights[0] += learn_speed
                for i in range(1, len(self.weights)):
                    self.weights[i] += learn_speed * point[i - 1]
                            
    def Predict(self, feature):
        if len(feature) + 1 != len(self.weights):
            print("Incorrect feature input")
            exit(-1)
        return self.ActivationFunction(feature) 


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
        self.neurons = [Neuron(feature_num) for i in range(neuron_count)]
        self.learn_speed = learn_speed
    
    def Train(self, points, labels, epochs=50):
        for _ in range(epochs):
            for point, label in zip(points, labels):
                for neuron, label_val in zip(self.neurons, label):
                    neuron.Learn(point, label_val, self.learn_speed)
    
    def Predict(self, point):
        result = []
        for neuron in self.neurons:
            result.append(neuron.Predict(point))
        return result
    
    def ShowPlot(self, points, labels):
        plt.plot([-10, 10], [0, 0]) #x axis
        plt.plot([0, 0], [-50, 50]) # y axis

        for neuron in self.neurons:
            x_value = []
            y_value = []
            i = -5
            while i <=5: # draw line between classes
                x_value.append(i)
                y_value.append(-((neuron.weights[0] + neuron.weights[1] * i) / neuron.weights[2]))
                i += 0.01
            plt.plot(x_value, y_value)

        #draw classes
        def get_color(label):
            color = 0
            for i in range(0, len(label)):
                color += (2 ** i) * label[i]
            return color

        plt.scatter([p[0] for p in points], [p[1] for p in points], c=[get_color(l) for l in labels])

        plt.show()

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
    with open(file_name, encoding='utf-8') as input_class_file:
        data = input_class_file.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip("\n").split(" ")

    labels_num = len(data[0])
    labels = [[] for _ in range(labels_num)]

    for i in range(len(data)):
        for j in range(labels_num):
            labels[j].append(int(data[i][j]))
    return labels

def GenRandomPoints(num):
    points = []
    for _ in range(num):
        random.seed()
        x = random.randrange(-5, 5)
        y = random.randrange(-5, 5)
        points.append([x, y])
    return points


def FirstTask():
    points = ReadPoints("input_1.txt")
    classes = ReadLabels("classes_1.txt")

    nn = NeuralNetwork(1, 2, 0.01)
    nn.Train(points, classes, epochs=50)
    for point, label in zip(points, classes):
        res = nn.Predict(point)
        print("point = {}, label = {}, pred_label = {}".format(point, label, res))
    
    # nn.ShowPlot(points, classes)

    print("----------------------------")

    validation_points = GenRandomPoints(3)
    val_labels = []
    for val_point in validation_points:
        res = nn.Predict(val_point)
        print("point = {}, pred_label = {}".format(val_point, res))
        val_labels.append(res)

    # nn.ShowPlot(validation_points, val_labels)

    print("----------------------------")

    random.shuffle(points)
    random.shuffle(classes)
    pred_labels = []
    for point, label in zip(points, classes):
        res = nn.Predict(point)
        print("point = {}, label = {}, pred_label = {}".format(point, label, res))
        pred_labels.append(res)
    nn.ShowPlot(points, classes)

def SecondTask():
    points = ReadPoints("input_2.txt")
    classes = ReadLabels("classes_2.txt")

    nn = NeuralNetwork(2, 2, 0.01)
    nn.Train(points, classes, epochs=50)
    for point, label in zip(points, classes):
        res = nn.Predict(point)
        print("point = {}, label = {}, pred_label = {}".format(point, label, res))
    nn.ShowPlot(points, classes)

    print("----------------------------")

    validation_points = GenRandomPoints(5)
    val_labels = []
    for val_point in validation_points:
        res = nn.Predict(val_point)
        print("point = {}, pred_label = {}".format(val_point, res))
        val_labels.append(res)
    nn.ShowPlot(validation_points, val_labels)


def main():

    FirstTask()
    SecondTask()


if __name__ == "__main__":
    main()

