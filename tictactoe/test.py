#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from libs.game import *
import unittest
class TestGamer(unittest.TestCase):
    """
    Test gamer.test()
    """
    def test_1(self):
        """Test"""
        gamer = Game()
        gamer.test()

if __name__ == '__main__':
    unittest.main()
