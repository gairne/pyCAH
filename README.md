# pyCAH

A python program that generates high quality Cards Against Humanity cards that can be used for printing.

Author: Matthew Mole <code@gairne.co.uk>

This program is released under the GNU General Public License Version 3

Cards Against Humanity is a card game produced by Cards Against Humanity LLC and is released under a Creative Commons BY-NC-SA 2.0 license.
Information is available at https://cardsagainsthumanity.com/

-------------
Dependencies:
-------------

1. ImageMagick and Python (developed with python v2.* in mind).
2. Obtain the HelveticaNeueBold font (typically HelveticaNeueBold.ttf) and place in the font/ directory.
   This is the font used on the official cards.

---------------
Usage examples:
---------------

- ./genCard.py -h
- ./genCard.py -i icon/icon-tabletop.png -b background/front-white.png -f fonts/HelveticaNeue-Bold.ttf -t "This is the card text" -n "1 / 44" -o custom001.png
- ./genCard.py -b background/front-white-sloth.png -o slothCard.png
- ./genCards.py -h
- ./genCards.py -i
- ./genCards.py -f sample/house-of-cards.csv.csv -p "HoC-" -s 1 -v -o generated/HOC/
  
Automated CAH expansion generation:
- ./extras.py
- ./house-of-cards.py
- ./pax.py
- ./reject.py
- ./retail.py
- ./tabletop.py
  
GenCard generates a single card, whilst GenCards generates multiple cards with instructions from an input file.
Check the files in the sample/ directory for inspiration on how to create an input file for GenCards.
 
-----
ToDo:
-----

1. Icons for official expansions 1-6, box expansion, various holiday expansions and science expansion. This is a low priority as these expansions are readily for sale. Research into whether AU or CA versions have icons.
2. Improvements to the reject card backgrounds and ladel card. Additionally, improvements to expansion icons and ensuring placement of text is accurate. This program tries to make cards as similar to the originals as possible, but this is not possible in some places (such as the reject pack).

------
Notes:
------

1. The cards produced are slightly larger than the 2.5" x 3.5" official cards, to allow for bleeding during the print process. The actual size generated is 2.75" x 3.75". Cards are generated at 1200 PPI.
2. If you add backgrounds, add a 3300x4500 pixel background to ensure card quality and allow for bleeding.
3. Icons should be 140x140. The software automatically rotates icons to fit in the lower left logo's rightmost box.
