"""
@author Nanami Kimoto
@date 05.09.22
@purpose 
Print the lyrics to 99 bottles of beer on the wall in python
@for The Mom Project (technical take home project)
"""

beerBottles = 99 # setting beerBottles to 99 because we start out with 99 bottles of beer
while beerBottles > 0: # while beer bottles is greater than 0, do the following
# print song lyrics
# new line for eahc lyric after beerBottles is used
   print(beerBottles, "bottles of beer on the wall")
   print(beerBottles,"bottles of beer")
   print("Take one down, pass it around")
   beerBottles = beerBottles - 1 #eveyrtime you take one down, subtract 1 from beerBottles
   print(beerBottles,"bottles of beer on the wall") #new amount of beerBottles is printed

