#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Matthew Mole <code@gairne.co.uk>
# This program is released under the GNU General Public License Version 3

# Cards Against Humanity is a card game produced by Cards Against Humanity LLC and is released under a Creative Commons BY-NC-SA 2.0 license
# Information is available at https://cardsagainsthumanity.com/

import argparse, subprocess, sys, os, os.path

from genCard import createCard
# createCard(outputFn, background, font=None, icon=None, text=None, numberText=None, verbose=False)

def printFileInfo():
    print \
"""
Your file should be a comma separated value file, one card per line, with the following columns:
Background,Icon,NumberText,CardText
    
Card Text can contain commas, just like in the example below. NumberText cannot.
Empty values are permissable - merely insert the next comma immediately after the prior one.
Use \\n for a new line in card text.
For background and icon, either specify the path to a file or specify the name of a file either in
the background/ or icon/ directories (with or without file extension).
    
Example:
front-white,,,The Rev. Dr. Martin Luther King, Jr.
front-black-pick2-houseofcards,icon-houseofcards,,Corruption. Betrayal. __________. Coming soon to Netflix, “House of __________.”
front-white,icon-PAX,1 / 44,Blah Blah Blah
backgrounds/front-white-sloth.png,,,
front-white,,,A super-soaker™ full of cat pee.
front-white.png,icon-PAX,1 / 44,Assumes front-white.png is in background directory.
~/pyCAH/backgrounds/front-white.png,icons/icon-PAX.png,1 / 44,Path to background example.
"""

def createCards(inputFile, outputDir, prefix="", offset=1, verbose=False):
    # Check outputDir either doesn't exist (then create it) or if it does exist, check it's a dir. Check if empty. If not, warn. Prompt user if they want to continue.
    # Check offset is a number
    # Check prefix is a string
    # Load file and check
    # Check that input and output exist
    # Allow file to specify the card number and prefix? If so warn command line flags are overriden if supplied.
    print (inputFile, outputDir, prefix, offset, verbose)
    
    
    # Check parameters
    ifh = open(inputFile, "r")
    
    n = offset
    for line in ifh.readlines():
        cols = line.strip().split(",")
        if len(cols) < 4:
            print "Error on line %d, expected at least 3 commas. Skipping: %s" % (offset-n+1, line)
            n += 1
            continue
            
        outputFn = prefix + "%03d" % (offset,) + ".png"
        background = cols[0]
        font = "font/HelveticaNeueBold.ttf"
        icon = cols[1]
        numberText = cols[2]
        cardText = ",".join(cols[3:])
        
        createCard(outputFn, background, font, icon, cardText, numberText, verbose)
        n += 1

######

def main():
    parser = argparse.ArgumentParser(description='Produce custom cards for Cards Against Humanity in PNG format.')
    parser.add_argument("-i", "--info", action="store_true", help="Print out some information about the input file format this program accepts.")
    parser.add_argument("-f", "--input", action='store', type=str, help="The input file which describes which cards to produce.", dest="input")
    parser.add_argument("-p", "--prefix", action='store', type=str, help="Optional. Add a prefix to the images created. By default, no prefix is added. For example, a prefix 'HOC-' would mean the first and second cards generated would have the filenames HOC-001.png and HOC-002.png. Without a prefix, the filenames would be 001.png and 002.png", dest='prefix', metavar="HouseOfCards-")
    parser.add_argument("-s", "--offset", action='store', type=int, help="Rather than starting from 001, start naming cards from this number.", dest="offset")
    parser.add_argument("-o", "--output", action='store', type=str, help="The output directory.", dest="output")
    parser.add_argument("-v", "--verbose", action='store_true', help="Turn on verbose mode. Any shell commands executed (and their results) are printed.", dest="verbose")
    args = parser.parse_args()
    
    if args.info:
        printFileInfo()
        sys.exit(0)
    
    if (args.input == None or args.input == ""):
        print "Error: Supply an input file."
        sys.exit(1)
        
    if (args.output == None or args.output == ""):
        args.output = os.getcwd() + "/"
    
    if (args.offset != None and args.offset <= 0):
        print "Error: Offset should be 1 or greater."
        sys.exit(1)
    
    createCards(args.input, args.output, "" if args.prefix == None else args.prefix, 1 if args.offset == None else args.offset, args.verbose)

if __name__ == '__main__':
    main()
