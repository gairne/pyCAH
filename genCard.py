#!/usr/bin/env python

# Author: Matthew Mole <code@gairne.co.uk>
# This program is released under the GNU General Public License Version 3

# Cards Against Humanity is a card game produced by Cards Against Humanity LLC and is released under a Creative Commons BY-NC-SA 2.0 license
# Information is available at https://cardsagainsthumanity.com/

import argparse, subprocess, sys, os, os.path

parser = argparse.ArgumentParser(description='Produce a custom card for Cards Against Humanity in PNG format.')
parser.add_argument("-i", "--icon", action='store', type=str, help="Optional. A filename for the icon in the logo towards the bottom of the card. If not supplied, no icon is used. An icon should be 140 pixels by 140 pixels.", required=False, dest="icon", metavar="icon.png")
parser.add_argument("-b", "--background", action='store', type=str, help="A filename for the card background. A white card is typically 'background/white.png', black cards 'background/black.png' and pick 2 black cards are 'black_pick2.png'. To generate high quality cards, the background must be 3300 by 4500.", required=True, metavar="background")
parser.add_argument("-t", "--text", action='store', type=str, help="Optional. The main card text. To create cards without text, such as the sloth card, do not supply this option.", required=False, dest="text", nargs="+")
parser.add_argument("-f", "--font", action='store', type=str, help="Optional. The font (file) to use for the card text. The official cards use Helvetica Neue Bold.", required=False, dest="font", metavar="HelveticaNeueBold.ttf")
parser.add_argument("-o", "--output", action='store', type=str, help="The output image filename.", required=True)

def perform(commandString, verbose=False):
    if verbose:
        print "Executing: " + str(commandString)
    process = subprocess.Popen(str(commandString), shell=True, stdout=subprocess.PIPE)
    (stdout, stderr) = process.communicate()
    return (stdout, stderr)

def createCard(outputFn, background, font=None, icon=None, text=None):
    cardTextBg = ""
    cardTextFg = ""
    
    # Check that imagemagick installed.
    stdout, stderr = perform("convert -version")
    if (not "Version: ImageMagick " in stdout):
        print "Error: ImageMagick is not installed."
        sys.exit(1)
    stdout, stderr = perform("identify -version")
    if (not "Version: ImageMagick " in stdout):
        print "Error: ImageMagick is not installed."
        sys.exit(1)
    
    # Check that the background exists
    if (not (os.path.exists(background) and os.path.isfile(background))):
        print "Error: The supplied background does not exist. File not found: " + background
        sys.exit(1)
    
    # Check that the background is the correct size. The background is a 3300 by 4500 image.
    # Height is calculated as 3.75 (3.5 inch card height plus 0.25 inch bleed) * 1200 pixels per inch.
    # Width is calculated the same; 2.75 * 1200 pixels per inch.
    stdout, stderr = perform("identify " + background)
    _, _, size, _, _, _, _, _, _ = stdout.split()
    bgWidth, bgHeight = size.split("x")
    
    try:
        bgWidth = int(bgWidth)
        bgHeight = int(bgHeight)
    except:
        bgWidth = -1
        bgHeight = -1
    
    if (bgWidth != 3300 or bgHeight != 4500):
        print "Error: For good quality card generation, the background image must be 3300 pixels by 4500 pixels."
        sys.exit(1)
    
    # Check that we can determine text colours from the background filename.
    if ("white" in background and not "black" in background):
        cardTextBg = "white"
        cardTextFg = "black"
    elif ("black" in background and not "white" in background):
        cardTextBg = "black"
        cardTextFg = "white"
    else:
        print "Error: The background filename must either contain the word 'white' or 'black', but not both. This indicates to " + sys.argv[0] + " which colour the card text should be."
        sys.exit(1)
        
    # Check that the icon exists, if an icon is used.
    if ((icon != "" and icon != None) and not (os.path.exists(icon) and os.path.isfile(icon))):
        print "Error: The supplied icon does not exist. File not found: " + icon
        sys.exit(1)
    
    # Check that the icon is the correct size. The icon is a 140 by 140 image.
    # This is not a fatal error, but may produce odd looking cards.
    if (icon != "" and icon != None):
        stdout, stderr = perform("identify " + icon)
        _, _, size, _, _, _, _, _, _ = stdout.split()
        iconWidth, iconHeight = size.split("x")
    
        try:
            iconWidth = int(iconWidth)
            iconHeight = int(iconHeight)
        except:
            iconWidth = -1
            iconHeight = -1
    
        if (iconWidth != 140 or iconHeight != 140):
            print "Warning: An icon that is not 140x140 may produce odd results. The icon should be 140 pixels by 140 pixels."
    
    # Check that the font exists.
    if (font != None and not (os.path.exists(font) and os.path.isfile(font))):
        print "Warning: The supplied font file does not exist. The card text will be styled in an unknown font. File not found: " + font
        font = None
    
    if (font == None):
        # Allow ImageMagick to attempt to use an installed font. This is not be guaranteed to work.
        font = "HelveticaNeueBold"

    # Perform the card creation.
    stdout, stderr = perform("convert \( -page +0+0 " + background + " \)" + (" -page +605+3865 -background none \( " + icon + " -rotate 17 \)" if (icon != "" and icon != None) else "") + (" -page +444+444 -units PixelsPerInch -background " + cardTextBg + " -fill " + cardTextFg + " -font " + font + " -pointsize 15 -kerning -1 -density 1200 -size 2450x caption:\"" + text + "\"" if (text != "" and text != None) else "") + " -layers merge " + outputFn)

######

args = parser.parse_args()
createCard(args.output, args.background, args.font, args.icon, " ".join(args.text) if args.text != None else None)