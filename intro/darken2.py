#!/usr/bin/env python3

import imageio
import numpy

test = imageio.imread('lena256.png').astype(float)
print(test.shape)

test[:, :, 1] /= 2.
test[:, :, 2] /= 2.

imageio.imsave('test.png', test.astype(numpy.uint8))
