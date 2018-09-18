#!/usr/bin/env python3

import imageio
import numpy

orig = imageio.imread('lena256.png').astype(numpy.float)
print(orig.shape)

test = numpy.zeros((256, 256), numpy.float)
for i in range(256):
  for j in range(256):
    test[i, j] = (orig[i, j, 0] + orig[i, j, 1] + orig[i, j, 2]) / 3.

imageio.imsave('test.png', test.astype(numpy.uint8))
