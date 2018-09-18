#!/usr/bin/env python3

import imageio
import numpy

orig = imageio.imread('lena256.png').astype(numpy.float)
print(orig.shape)

weight = numpy.zeros((256, 256, 3), numpy.float)
weight[:, :, 0] = .299
weight[:, :, 1] = .587
weight[:, :, 2] = .114

test = numpy.sum(orig * weight, 2)

imageio.imsave('test.png', test.astype(numpy.uint8))
