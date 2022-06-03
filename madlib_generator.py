#akshit-g
#import modules
from tkinter import *

# initialize window
win = Tk()
win.geometry("300x350")
win.title("Mad Libs Game Generator")
Label(win, text= "Mad Libs Generator", font = "Allura 20 bold").pack()
Label(win, text = "Click Any One:", font = "Arial 15 bold").place(x=40, y=80)


#madlib functions
def madlib1():
    animals = input("Enter an animal name:\t")
    profession = input("Enter an profession:\t")
    cloth = input("Enter a type of cloth:\t")
    things = input("Enter a thing:\t")
    name = input("Enter a name:\t")
    place = input("Enter a location:\t")
    verb = input("Enter a verb:\t")
    food = input("Enter the name of a food article:\t")
    print("Say " + food + "! the photographer said as the camera flashed! " + name + " and I had gone to " + place + " to get our photos taken today. The first photo we really wanted was a picture of us dressed as " + animals + " pretending to be a " + profession + ". When we saw the second photo, it was exactly what I wanted. We both looked like " + things + " wearing " + cloth + " and " + verb + "")



def madlib2():
    adjective = input("Enter an adjective:\t")
    color = input("Enter a colour:\t")
    thing = input("Enter an object:\t")
    place = input("Enter a location:\t")
    person = input("Enter a name:\t")
    adjective1 = input("Enter another adjective:\t")
    insect = input("Enter an insect:\t")
    food = input("Enter the name of a food article:\t")
    verb = input("Enter a verb (ing form):\t")

    print("Last night I dreamed I was a " + adjective + " butterfly with " + color + " patches that looked like " + thing + ". I flew to " + place + " with my bestfriend and " + person + " who was a " + adjective1 + " " + insect + " . We ate some " + food + " when we got there and then decided to " + verb + " and the dream ended when I said, Lets " + verb + ".")
    


def madlib3():
    person = input("Enter a name:\t")
    color = input("Enter a colour:\t")
    foods = input("Enter the name of a food article:\t")
    adjective = input("Enter an adjective:\t")
    thing = input("Enter an object:\t")
    place = input("Enter a location:\t")
    verb = input("Enter a verb (ing form):\t")
    adverb = input("Enter an adverb:\t")
    food = input("Enter the name of a food article:\t")
    things = input("Enter an object:\t")

    print("Today we picked up apples from" + person + "'s Orchard. I had no idea that there were so many different varieties of apples. I ate " + color + " apples straight off the tree that tasted like " + foods + ". Then there was a " + adjective + " apple that looked like a " + thing + ".When our bag were full, we went on a free hay ride to " + place + " and back. It ended at a hay pile where we got to " + verb + " " + adverb + ". I can hardly wait to get home and cook with the apples. We are going to make appple" + food + " and " + things + " pies!")  



#GUI with button options
Button(win, text="The Photographer", font ="Arial", command=madlib1, bg ="white").place(x = 60, y = 120)
Button(win, text="Apple & Apple", font="Arial", command=madlib3 , bg="white").place(x = 70, y = 180)
Button(win, text="The Butterfly", font="Arial", command=madlib2, bg="white").place(x = 80, y = 240)

win.mainloop()
