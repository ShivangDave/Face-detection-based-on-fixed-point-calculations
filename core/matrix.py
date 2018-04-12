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

def create_one(pixels, width, height):
    return_matrix = []
    for y in range(width):
        arr = []
        for x in range(height):
            temp = int((30*pixels[y,x][0]+59*pixels[y,x][1]+11*pixels[y,x][2])/100)
            arr.append(temp)
        return_matrix.append(arr)
    return return_matrix

def create_two(matrix_one, width, height):
    return_matrix = []
    for y in range(width):
        arr = []
        for x in range(height):
            temp = matrix_one[y][x]
            arr.append(temp)
        return_matrix.append(arr)
    return return_matrix
