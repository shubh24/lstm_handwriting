from __future__ import division
from utils import *
import cPickle
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
data_file = "./data/strokes_training_data.cpkl"


def get_strokes():
	data = DataLoader()
	f = open(data_file, "r")
	strokes = cPickle.load(f)
	return strokes

def stroke_length_match(strokes):
	similar_strokes = []
	for i in range(0, len(strokes)):
		for j in range(i+1, len(strokes)):
			#print len(strokes[i]), len(strokes[j])
			if abs(len(strokes[i][0])-len(strokes[j][0]))/max(len(strokes[i][0]), len(strokes[j][0])) < 0.01:
				similar_strokes.append((strokes[i][0], strokes[j][0],strokes[i][1], strokes[j][1]))
				
	return similar_strokes

def get_pearson_coeff(similar_stroke):
	stroke1 = similar_stroke[0]
	stroke2 = similar_stroke[1]
	min_len = min(len(stroke1), len(stroke2))
	sx1 = [stroke1[i][0] for i in range(0, min_len)]
	sx2 = [stroke2[i][0] for i in range(0, min_len)]
	sy1 = [stroke1[i][1] for i in range(0, min_len)]
	sy2 = [stroke2[i][1] for i in range(0, min_len)]
	
	x_pearson = pearsonr(sx1, sy1)[0] 
	y_pearson = pearsonr(sy1, sy2)[0]

	if x_pearson > 0.5 or y_pearson > 0.5:
		print similar_stroke[2], similar_stroke[3]
		print x_pearson, y_pearson
		plt.plot(sx1, label = "Stroke 1 X Co-ordinate")
		plt.plot(sx2, label = "Stroke 2 X Co-ordinate")
		plt.plot(sy1, label = "Stroke 1 Y Co-ordinate")
		plt.plot(sy2, label = "Stroke 2 Y Co-ordinate")
		plt.legend(ncol= 2, fancybox=True)
		plt.show()


if __name__ == '__main__':
	strokes = get_strokes()
	similar_strokes = stroke_length_match(strokes)

	for s in similar_strokes:
		get_pearson_coeff(s)