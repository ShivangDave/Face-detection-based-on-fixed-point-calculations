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

def integral_image(width, height, matrix_one, matrix_two):
    matrix_two[0][0] = pow(matrix_two[0][0],2)
    for x in range(width):
        for y in range(height):
            if x == 0 and y != 0:
                matrix_one[x][y] += matrix_one[x][y-1]
                matrix_two[x][y] = matrix_two[x][y-1] + pow(matrix_two[x][y],2)
            elif y == 0 and x != 0:
                matrix_one[x][y] += matrix_one[x-1][y]
                matrix_two[x][y] = matrix_two[x-1][y] + pow(matrix_two[x][y],2)
            elif x != 0 and y != 0:
                matrix_one[x][y] += matrix_one[x-1][y] + matrix_one[x][y-1] - matrix_one[x-1][y-1]
                matrix_two[x][y] = matrix_two[x-1][y] + matrix_two[x][y-1] - matrix_two[x-1][y-1] + pow(matrix_two[x][y],2)
    return matrix_one, matrix_two
