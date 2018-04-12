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

def sqr(n,shift=8):
    x = 1 << shift
    n_one = n << shift

    while 1:
        x_old = x
        x = (x+n_one//x)//2
        if x == x_old:
            break
    return x

a = 1
fp_a = int(a*256)
ans = sqr(fp_a)//256

print(ans)
