#!/usr/bin/env python

# Author: Matthew Mole <code@gairne.co.uk>
# This program is released under the GNU General Public License Version 3

# Cards Against Humanity is a card game produced by Cards Against Humanity LLC and is released under a Creative Commons BY-NC-SA 2.0 license
# Information is available at https://cardsagainsthumanity.com/

import subprocess, os, shutil

from genCards import createCards
#createCards(inputFile, outputDir, prefix="", offset=1, verbose=False)

createCards(os.getcwd() + "/sample/pax-east-2013.csv", os.getcwd() + "/generated/pax/east2013/", "PAX-east-2013-", 1, False)
shutil.copy(os.getcwd() + "/sample/PAX-east-2013-030.png", os.getcwd() + "/generated/pax/east2013/PAX-east-2013-030.png")
#shutil.copy(os.getcwd() + "/background/back-black.png", os.getcwd() + "/generated/pax/east2013/PAX-east-2013-030back.png")
createCards(os.getcwd() + "/sample/pax-prime-2013.csv", os.getcwd() + "/generated/pax/prime2013/", "PAX-prime-2013-", 1, False)
createCards(os.getcwd() + "/sample/pax-east-2014.csv", os.getcwd() + "/generated/pax/east2014/", "PAX-east-2014-", 1, False)
createCards(os.getcwd() + "/sample/pax-east-2014-panel.csv", os.getcwd() + "/generated/pax/east2014panel/", "PAX-east-2014-panel-", 1, False)
createCards(os.getcwd() + "/sample/pax-prime-2014-panel.csv", os.getcwd() + "/generated/pax/prime2014panel/", "PAX-prime-2014-panel-", 1, False)