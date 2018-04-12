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

import parse as parse
import decimal as decimal

def detect(matrix_one,matrix_two,width, height, classifier):
    result = []
    scale, scaleFactor = 5, 2
    windowWidth, windowHeight = (int(n) for n in parse.classifier.find("size").text.split())
    while windowWidth < width and windowHeight < height:
        windowWidth = windowHeight = int(scale*20)
        step = int(scale*2.4)
        windowX = 0
        while windowX < width-scale*24:
            windowY = 0
            while windowY < height-scale*24:
                if stage(matrix_one,matrix_two,windowX,windowY,windowWidth,windowHeight,classifier,scale):
                    result.append((windowX, windowY, windowWidth, windowHeight))
                windowY += step
            windowX += step
        scale = scale * scaleFactor
    return result

def stage(matrix_one,matrix_two,windowX,windowY,windowWidth,windowHeight,classifier,scale):
    passed = True
    for stage in classifier:
        stage_threshold = stage[-1]
        stage_sum = 0
        for struct in stage[:-1]:
            struct_value = 0
            idx = 0
            while True:
                node = struct[idx]
                rect = node[0]
                node_treshold = (decimal.Decimal(node[1])).quantize(decimal.Decimal('0.0000'))
                left = node[2]
                right = node[3]
                left_node = node[4]
                right_node = node[5]
                feature_sum, inv_a, variance_norm = feature(matrix_one,matrix_two,windowX,windowY,
                              windowWidth, windowHeight,rect,scale)
                if feature_sum*inv_a < node_treshold*variance_norm:
                    if left_node is None:
                        struct_value = (decimal.Decimal(left)).quantize(decimal.Decimal('0.0000'))
                        break
                    else:
                        idx = int(left_node)
                else:
                    if right_node is None:
                        struct_value = (decimal.Decimal(right)).quantize(decimal.Decimal('0.0000'))
                        break
                    else:
                        idx = int(right_node)
            stage_sum += struct_value
        passed = stage_sum >= stage_threshold
        if not passed:
            return passed
    return passed

def feature(matrix_one,matrix_two,windowX,windowY,windowWidth,windowHeight,rect,scale):
    inv_a = 1.0/(windowWidth*windowHeight)
    feature_sum = 0
    total_weight_one = matrix_one[windowX+windowWidth][windowY+windowHeight] \
                       +matrix_one[windowX][windowY] \
                       -matrix_one[windowX+windowWidth][windowY] \
                       -matrix_one[windowX][windowY+windowHeight]
    total_weight_two = matrix_two[windowX+windowWidth][windowY+windowHeight] \
                       +matrix_two[windowX][windowY] \
                       -matrix_two[windowX+windowWidth][windowY] \
                       -matrix_two[windowX][windowY+windowHeight]
    variance_norm = total_weight_two*inv_a-pow(total_weight_one*inv_a,2)
    if variance_norm > 1:
        fix_point = int(variance_norm)*256
        variance_norm = sqr(fix_point)//256
    else:
        variance_norm = 1
    for obj in rect:
        x = int(scale*int(obj[0]))
        y = int(scale*int(obj[1]))
        w_width = int(scale*int(obj[2]))
        h_height = int(scale*int(obj[3]))
        w_weight = int((decimal.Decimal(obj[4])).quantize(decimal.Decimal('0.0000')))
        feature_sum += w_weight * \
                      (matrix_one[windowX+x+w_width][windowY+y+h_height] \
                      + matrix_one[windowX+x][windowY+y] \
                      - matrix_one[windowX+x+w_width][windowY+y] \
                      - matrix_one[windowX+x][windowY+y+h_height])
    return feature_sum, inv_a, variance_norm

def sqr(n):
    shift = 8
    x = 1 << shift
    n_shift = n << shift

    while 1:
        x_og = x
        x = (x+n_shift//x)//2
        if x == x_og:
            break
    return x
