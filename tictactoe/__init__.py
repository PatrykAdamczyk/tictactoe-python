#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SYNOPSIS

    tictactoe

DESCRIPTION

    Gra w kółko i krzyżyk

AUTHOR

    Patryk Adamczyk <patrykadamczyk@paip.com.pl>

LICENSE

    PAiP Open Source License

VERSION

    v.1.0.0.0
"""
import sys
from tictactoe.libs.game import *

def main(args):
	"""Główna Funkcja Programu"""
	gamer = Game()
	gamer.run()
	sys.exit()

if __name__ == '__main__':  # pragma: no cover
	sys.exit(main(sys.argv))