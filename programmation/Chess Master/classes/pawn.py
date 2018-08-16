#! /usr/bin/env python3
# coding: utf-8
from .piece import Piece

class Pawn(Piece):
    def type(self):
        return "t"
    def getPermutations(self):
        return [(-1,1), (1,1)] # attach only
