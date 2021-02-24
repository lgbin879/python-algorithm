#!usr/bin/env python3
#-*- coding:utf-8 -*-
__author__ = 'guibinli@gmail.com'

import pytest
import allure
from practice1_SingleList import SingleLinkList
from practice2_CircleList import CircleLinkList
from practice3_DLinkList import DLinkList


@allure.feature("test algorithm")
class TestAlgorithm():
    def setup_class(self):
        print("test setup")

    @allure.story("SingleList")
    @allure.title("SingleList")
    def test_SingleList(self):
        l = SingleLinkList()
        # print(l.length())
        # l.travel()

        l.append(0)
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)

        # print(l.length())
        l.travel()

        l.reverseList()
        l.travel()

        # l.add(9)
        # l.travel()

        # l.insert(5, 8)
        # l.travel()

        # l.search(3)
        # l.search(99)

        l.removeNthFromEnd(2)
        l.travel()

    @allure.story("CircleLinkList")
    @allure.title("CircleLinkList")
    def test_CircleLinkList(self):
        l = CircleLinkList()
        print(l.length())
        l.travel()

        l.append(0)
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)

        print(l.length())
        l.travel()

        l.add(9)
        l.append(7)
        l.travel()

        l.insert(5, 8)
        l.travel()

        l.search(3)
        l.search(99)

        l.remove(8)
        l.travel()

        #l.removeNthFromEnd(2)
        #l.travel()

    @allure.story("DLinkList")
    @allure.title("DLinkList")
    def test_DLinkList(self):
        l = DLinkList()
        print(l.length())
        l.travel()

        l.append(0)
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)

        print(l.length())
        l.travel()

        l.add(9)
        l.append(7)
        l.travel()

        l.insert(5, 8)
        l.travel()

        l.search(3)
        l.search(99)

        l.remove(8)
        l.travel()


    def teardown_class(self):
        print("teardown_class")


if __name__ == '__main__':
	pytest.main(["-vs", "./test_python_algorithm.py", "--alluredir", "allure_results"])
