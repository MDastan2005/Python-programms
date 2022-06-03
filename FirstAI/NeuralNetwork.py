import numpy as np


class NeuralNetwork:

    def __init__(self, sizes, learning_rate, bias=False, moment=0):
        if len(sizes) < 2:
            raise Exception('At least two layers needed!')
        self.sizes = sizes
        self.learning_rate = learning_rate
        self.bias = bias
        self.moment = moment
        self.numLayers = len(sizes)
        self.neurons = []
        self.clear_neurons()
        self.weights = []
        self.clear_weights()
        self.randomize_weights()
        self.deltas = []
        self.clear_deltas()
        self.delta_weights = []
        self.clear_delta_weights()

    def clear_neurons(self):
        self.neurons = [[0 for _ in range(sz)] for sz in self.sizes]
        if self.bias:
            for i in range(self.numLayers - 1):
                self.neurons[i][-1] = 1

    def clear_weights(self):
        for i in range(self.numLayers - 1):
            self.weights.append([
                [
                    0 for _ in range(self.sizes[i + 1])
                ] for _ in range(self.sizes[i])
            ])

    def clear_delta_weights(self):
        for i in range(self.numLayers - 1):
            self.delta_weights.append([
                [
                    0 for _ in range(self.sizes[i + 1])
                ] for _ in range(self.sizes[i])
            ])

    def randomize_weights(self):
        for idx in range(self.numLayers - 1):
            self.weights[idx] = np.random.random((self.sizes[idx], self.sizes[idx + 1])).tolist()

    def set_weights(self, weights):
        bad = False
        if len(weights) != self.numLayers - 1:
            bad = True
        for w1, w2 in zip(weights, self.weights):
            if len(w1) != len(w2):
                bad = True
            for ww1, ww2 in zip(w1, w2):
                if len(ww1) != len(ww2):
                    bad = True
        if bad:
            raise Exception('Incorrect size of weights list')
        self.weights = weights

    def clear_deltas(self):
        self.deltas = [[0 for _ in range(sz)] for sz in self.sizes]

    def set_input(self, input_data):
        if len(self.neurons[0]) - self.bias != len(input_data):
            raise Exception('Number of inputs not match!')
        for idx, val in enumerate(input_data):
            self.neurons[0][idx] = val
        for idx in range(self.sizes[0]):
            self.neurons[0][idx] = self.sigmoid(self.neurons[0][idx])

    def get_output(self):
        return self.neurons[-1]

    def calculate_result(self):
        self.forward_propagation()

    def get_error_mse(self, correct_answer):
        output = self.get_output()
        if len(output) != len(correct_answer):
            raise Exception('Number of responses not match!')
        result = 0
        for real_answer, nn_answer in zip(correct_answer, output):
            diff = real_answer - nn_answer
            result += diff ** 2
        return result / len(output)

    def forward_propagation(self):
        for layer_idx in range(self.numLayers - 1):
            currentLayer = self.neurons[layer_idx]
            nextLayer = self.neurons[layer_idx + 1]
            for i, v in enumerate(nextLayer):
                x = 0
                for idx, val in enumerate(currentLayer):
                    x += self.weights[layer_idx][idx][i] * val
                nextLayer[i] = self.sigmoid(x)

    def back_propagation(self, correct_answer):
        if len(self.neurons[-1]) != len(correct_answer):
            raise Exception('Number of outputs not match!')
        output = self.neurons[-1]
        for layer_idx in range(self.numLayers - 1, 0, -1):
            for current_layer_idx in range(self.sizes[layer_idx]):
                if layer_idx == self.numLayers - 1:
                    self.deltas[layer_idx][current_layer_idx] = (correct_answer[current_layer_idx] - output[
                        current_layer_idx]) * \
                                                                self.sigmoid(output[current_layer_idx], deriv=True)
                else:
                    self.deltas[layer_idx][current_layer_idx] = self.sigmoid(self.neurons[layer_idx][current_layer_idx],
                                                                             deriv=True) * \
                                                                np.dot(self.weights[layer_idx][current_layer_idx],
                                                                       self.deltas[layer_idx + 1])
                for prev_layer_idx in range(self.sizes[layer_idx - 1]):
                    grad = self.neurons[layer_idx - 1][prev_layer_idx] * self.deltas[layer_idx][current_layer_idx]
                    self.delta_weights[layer_idx - 1][prev_layer_idx][current_layer_idx] = self.learning_rate * grad + self.moment * self.delta_weights[layer_idx - 1][prev_layer_idx][current_layer_idx]
                    self.weights[layer_idx - 1][prev_layer_idx][current_layer_idx] += self.delta_weights[layer_idx - 1][prev_layer_idx][current_layer_idx]

    @staticmethod
    def sigmoid(x, deriv=False):
        if deriv:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def tanh(x, deriv=False):
        if deriv:
            return 1 - x ** 2
        return (np.exp(x + x) - 1) / (np.exp(x + x) + 1)
