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
from PIL import ImageDraw

def draw(input_image,result):
    list_output = remove_duplicates(result)
    for obj in list_output:
        X,Y,W,H = obj
        draw_context = ImageDraw.Draw(input_image)
        draw_context.line((X,Y,X,Y+H),(0,255,0,255),1)
        draw_context.line((X,Y+1/2,X+W,Y+1/2),(0,255,0,255),1)
        draw_context.line((X+W,Y,X+W,Y+H),(0,255,0,255),1)
        draw_context.line((X,Y+H-1/2,X+W,Y+H-1/2),(0,255,0,255),1)
        del draw_context
    input_image.show()
    return list_output

def remove_duplicates(result):
    unique = []
    if len(result)>0:
        center = []
        X, Y, W, H = result[0]
        center.append((X + W/2, Y + H/2))
        unique.append((result[0]))

        for obj in result:
            x, y, w, h = obj
            for c in center:
                cx, cy = c
                if x < cx < x+w and y < cy < y+h:
                    break
                elif x+w<X or X+W<x or y+h<Y or Y+H<y:
                    X=x
                    Y=y
                    W=w
                    H=h
                    unique.append((obj))
                    center.append((X+W/2,Y+H/2))
        return unique
    else:
        return []
