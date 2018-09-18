#!/usr/bin/env python3

import imageio
import numpy

test = imageio.imread('lena256.png').astype(float)
print(test.shape)

for i in range(256):
  for j in range(256):
    for k in range(3):
      test[i, j, k] /= 2.

imageio.imsave('test.png', test.astype(numpy.uint8))
