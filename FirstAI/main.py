from NeuralNetwork import NeuralNetwork
from numpy import round


nn = NeuralNetwork([5, 7, 3], learning_rate=0.1, moment=0.8, bias=True)
with open("data/iris.data", 'r') as f:
	data = [list(map(float, line[:-1].split(',')[:-1])) for line in f]
iris_dict = {
	"Iris-setosa": [1, 0, 0],
	"Iris-versicolor": [0, 1, 0],
	"Iris-virginica": [0, 0, 1]
}
with open("data/iris.data", 'r') as f:
	answers = [iris_dict[line[:-1].split(',')[-1]] for line in f]


def convert_result(result):
	result = round(result)
	result = result.tolist()
	pos = result.index(max(result))
	if pos == 0:
		return "Iris-setosa"
	elif pos == 1:
		return "Iris-versicolor"
	elif pos == 2:
		return "Iris-virginica"


def teaching():
	for epoch in range(1000):
		error = 0
		for iteration, current_data in enumerate(data):
			nn.set_input(current_data)
			nn.calculate_result()
			nn.back_propagation(answers[iteration])
			error += nn.get_error_mse(answers[iteration])
		error *= 100 / len(data)
		print(f"Обучена на {epoch / 10}%\nСребняя ошибка {error}%")
	print("Обучение Закончено!!!")
	print(nn.weights)


def main():
	weights = [[[1.0959763108362626, 4.843334557382084, 1.4981059070981368, -1.750812775104477, -1.887697271015474, -4.064119122219002, 4.5585997196316805], [1.0059614797054972, 7.368227563652704, 3.1504258833272067, -2.732261239484511, -2.858661450980662, -4.9330689367102085, 5.935650347519191], [0.3272123939156327, -7.739457250232159, -2.0666557070663587, 0.25235868398884503, 2.5027202570920064, -0.6188512653275394, -0.015153078007983628], [-0.2042675776015268, -11.486412077697223, -4.922039521841628, 6.1701143990781615, 3.8980819372772095, 13.331795209578862, -15.450393818698702], [0.286790967600778, 3.778970482634988, 1.7027216785507973, -1.058373065619696, -0.524575765622526, -2.313226194333711, 3.559207938823636]], [[-2.7447721346293497, -0.42188408730346616, -0.8573855442510225], [7.423843949465299, -12.05506788645719, -9.645178679737787], [1.4969204264593587, -0.6089242168032117, -5.423540361113544], [-4.768914324414693, -1.9631915482792681, 4.355794048617173], [-4.993692638403371, 0.8688706592607887, 4.568458599327902], [-5.738974628191784, -7.51676200575733, 5.818750453942311], [3.2053074733116924, 8.194719912949898, -7.421501193376383]]]

	nn.set_weights(weights)
	correct = 0
	num = len(data)
	for iteration, current_data in enumerate(data):
		nn.set_input(current_data)
		nn.calculate_result()
		output = convert_result(nn.get_output())
		needed_output = convert_result(answers[iteration])
		error = nn.get_error_mse(answers[iteration])
		print(f"Iteration: {iteration}\nOutput: {output}\nAnswer: {needed_output}\nError: {error}")
		if needed_output == output:
			correct += 1
		else:
			print("______________________________")
	print(f"Correct {correct} from {num}")


if __name__ == "__main__":
	teaching()
	# main()
