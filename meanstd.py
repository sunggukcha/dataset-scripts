'''
	Author: Sungguk Cha
	eMail : navinad@naver.com

	Given a dataset, it calculates RGB mean & std.
'''

import os
import numpy as np
from caltech import caltech101Classification as cal
from torch.utils.data import DataLoader


dataset = cal(root="./caltech101/101_ObjectCategories")
loader = DataLoader(
    dataset,
    batch_size=1,
    num_workers=1,
    shuffle=False
)


mean = [0., 0., 0.]
std = [0., 0., 0.]
nb_samples = len(loader)
print(nb_samples)
for data in loader:
	image = np.array(data[0]).astype(float)
	x = image.mean(axis=(0,1))/255
	y = image.std(axis=(0,1))/255
	mean += x
	std += y

mean /= nb_samples
std /= nb_samples

print("mean: {}\nstd: {}".format(mean, std))
