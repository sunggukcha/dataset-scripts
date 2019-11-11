'''
	Author: Sungguk Cha
	eMail : navinad@naver.com

	Dataloader for caltech101 dataset image classification.
'''

import os
import numpy as np
from PIL import Image
from torch.utils import data

class caltech101Classification(data.Dataset):
	'''
		caltech101 classification
	'''
	NUM_CLASSES = 101

	def __init__ (self, root, seed=3363):
		self.root	= root
		self.files = self.recursive_glob(rootdir=self.root, suffix='.jpg')
	
	def __len__(self):
		return len(self.files)

	def __getitem__(self, index):
		img_path = self.files[index].rstrip()
		_img = Image.open(img_path).convert('RGB')
#		return _img
		return np.array(_img)



	def recursive_glob (self, rootdir='.', suffix=''):
		return [os.path.join(looproot, filename)
				for looproot, _, filenames in os.walk(rootdir)
				for filename in filenames if filename[-4:] == suffix]
