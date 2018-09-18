#!/usr/bin/env python3

import imageio
import numpy

orig = imageio.imread('lena256.png').astype(numpy.float)
print(orig.shape)

test = .299 * orig[:, :, 0] + .587 * orig[:, :, 1] + .114 * orig[:, :, 2]

imageio.imsave('test.png', test.astype(numpy.uint8))
