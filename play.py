from music21 import *

'''
needs:
 - map of instrument-type => array of musical sections
 - max-playthroughs limit for each section
 - limitation that you can't be more than "n" sections behind or ahead of anyone else

 other considerations that could tank this approach:
 - this is to be played with musescore I guess? Does music21 provide any other interface to playing arrangements? Should we switch to mingus?
 - if it's to be run with musescore, do I need to dynamically generate a score each time, and run them multi-threaded? or incorporate all n pieces into one score?
 - does musescore even have an API to programatically access score generation, via python or other?
 - being able to save a generated performance is a crucial feature
'''

# random tutorial stuff

s = corpus.parse('bach/bwv250.mxl')
# Now s represents an entire score of a chorale by J.S. Bach. Type “s.analyze('key')” to see what music21’s best guess as to its key is:

s.analyze('key')
#  <music21.key.Key of a minor>
# Now let’s see if you can see scores with music21. If this doesn’t work, you can skip ahead to Chapter 8: Installing a MusicXML reader or just work through the tutorial until you get there without seeing scores. Type “s.show(). Assuming your installation and configuration went as expected, your MusicXML reader should launch and display the chorale, looking something like what we see here:

s.show()
