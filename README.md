# pyCAH
A python program that generates high quality Cards Against Humanity cards that can be used for printing.

# Author: Matthew Mole <code@gairne.co.uk>
# This program is released under the GNU General Public License Version 3

# Cards Against Humanity is a card game produced by Cards Against Humanity LLC and is released under a Creative Commons BY-NC-SA 2.0 license
# Information is available at https://cardsagainsthumanity.com/

-------------
Installation:
-------------

1) Install ImageMagick and Python
2) Obtain the HelveticaNeueBold font (typically HelveticaNeueBold.ttf) and place in the fonts directory.
   This is the font used on the official cards.

---------------
Usage examples:
---------------

  ./genCard.py -h
  ./genCard.py -i icon/icon-tabletop.png -b background/front-white.png -f fonts/HelveticaNeue-Bold.ttf -t "This is the card text" -o custom001.png
  ./genCard.py -b background/front-white-sloth.png -o slothCard.png
 
-----
ToDo:
-----

1) Icons for official expansions 1-6, reject pack, box expansion, various holiday expansions and science expansion. This is a low priority as these expansions are readily for sale. Research into whether AU or CA versions have icons.
2) Adding n / m numbers to cards, used by some of the PAX expansions. Note that the black-pick2 from pax east has the n / m text in a different place.
3) Batch card creation support.
4) Full reject card support - ladle icon, ink blot, author portraits.

------
Notes:
------

1) The cards produced are slightly larger than the 2.5" x 3.5" official cards, to allow for bleeding during the print process.
2) If you add backgrounds, add a 3300x4500 pixel background to ensure card quality and allow for bleeding.
3) Icons should be 140x140. The software automatically rotates icons to fit in the lower left logo's rightmost box.