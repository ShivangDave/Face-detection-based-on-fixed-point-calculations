# Copyright (C) 2018 Shivang Dave <mail@shivangdave.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, see <http://www.gnu.org/licenses/>.

import os, sys, math, time, decimal
from PIL import Image
import time
from core import parse as parse
from core import integral as integral
from core import detect as detector
from core import draw as draw
from core import matrix as matrix

def exec_(image_name):
    start_t = time.time()
    input_image = Image.open(image_name)
    width, height = input_image.size
    pixels = input_image.load()

    matrix_one = []
    matrix_two = []

    matrix_one = matrix.create_one(pixels, width, height)
    matrix_two = matrix.create_two(matrix_one, width, height)

    matrix_one, matrix_two = integral.integral_image(width, height, matrix_one, matrix_two)
    classifier = parse.get_classifier()

    result = detector.detect(matrix_one,matrix_two,width,height,classifier)
    list_output = draw.draw(input_image,result)
    print('\nTotal Faces detected in %s: %d'%(image_name,len(list_output)))
    print('Total time: %s' %(round(time.time() - start_t,2)))

if len(sys.argv) != 2:
    for i in range(1,6):
        im_name = "img/" + str(i)+ ".jpg"
        exec_(im_name)
else:
    exec_("img/"+str(sys.argv[1]))
