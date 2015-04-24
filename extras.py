#!/usr/bin/env python

# Author: Matthew Mole <code@gairne.co.uk>
# This program is released under the GNU General Public License Version 3

# Cards Against Humanity is a card game produced by Cards Against Humanity LLC and is released under a Creative Commons BY-NC-SA 2.0 license
# Information is available at https://cardsagainsthumanity.com/

import subprocess, os, shutil

from genCards import createCards
#createCards(inputFile, outputDir, prefix="", offset=1, verbose=False)

createCards(os.getcwd() + "/sample/extras.csv", os.getcwd() + "/generated/extras/", "extra-", 1, True)