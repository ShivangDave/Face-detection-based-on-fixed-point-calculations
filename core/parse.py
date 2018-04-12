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

from lxml import etree

classifier = etree.parse("haarcascade_frontalface_alt2.xml").getroot() \
                .find("haarcascade_frontalface_alt2")

def get_classifier():
    new_classifier = parse(classifier)
    return new_classifier

def noneCheck(node,entity):
    temp = 0.0
    if not node.find(entity) is None:
        temp = float(node.find(entity).text)
    else:
        temp = node.find(entity)
    return temp

def parse(classifier) :
    stages = classifier.find("stages")
    haar_cascade = []

    for stage in stages :
        stageList = []
        trees = stage.find("trees")
        stageThreshold = float(stage.find("stage_threshold").text)

        for tree in trees:
            treeArray = []
            for idx in range(2) :
                nodeList = []
                rectsList = ()
                node = tree[idx+1]
                feature = node.find("feature")
                rects = feature.find("rects")

                for rect in rects :
                    rectTextSplit = rect.text.split()
                    rectsList += (rectTextSplit,)
                nodeList.append(rectsList)

                nodeThreshold = noneCheck(node,"threshold")
                nodeList.append(nodeThreshold)

                left_val = noneCheck(node,"left_val")
                nodeList.append(left_val)

                right_val = noneCheck(node,"right_val")
                nodeList.append(right_val)

                left_node = noneCheck(node,"left_node")
                nodeList.append(left_node)

                right_node = noneCheck(node,"right_node")
                nodeList.append(right_node)

                treeArray.append(nodeList)
            stageList.append(treeArray)
        stageList.append(stageThreshold)
        haar_cascade.append(stageList)
    return haar_cascade
