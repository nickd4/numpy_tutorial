#!/usr/bin/env python3

import imageio
import numpy

orig = imageio.imread('lena256.png').astype(numpy.float)
print(orig.shape)

weight = numpy.array([.299, .587, .114], numpy.float)
test = numpy.sum(orig * weight[numpy.newaxis, numpy.newaxis, :], 2)

imageio.imsave('test.png', test.astype(numpy.uint8))
