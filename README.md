# Prisoners and Boxes

This program simulates the solution to the "Prisoners and Boxes"-riddle

# The problem

There are 100 prisoners living in solitary cells in a prison. 
The warden wants to give them a chance to earn their freedom by «solving» a puzzle 
with potentially extreme outcomes:

Each prisoner is given their own unique number ranging from 1-100, and each number 
is written down on its own individual note. 
The collection of notes then gets distributed randomly throughout 
100 chronologically numbered boxes with each box containing one note.
The boxes are placed in a room with one entrance and one exit.
One prisoner can enter the room at a time, and their objective is to locate their unique number in one of the boxes.
They get to check 50 boxes before they have to exit the room, 
leaving it in the exact same state as it was when they entered (meaning that the room and the boxes looks 
the same to all prisoners).

If all of the prisoners manage to find their number they all walk free, but if as much as one 
fails they are all executed.

What is the best strategy the prisoners can apply?

# Solution

The best strategy is for each prisoner to start by opening the box corresponding to their own number, 
and then let the notes dictate which box to open next.
So Prisoner  X starts by opening box  X. If the note in box  X says «Y», then box nr. Y is the next box to be opened.
This leads the prisoner on to a loop, where they are essentially looking for the note that leads them back to box X

# Example:

Box 2 (note 4) —> Box 4 (note 9) —> Box 9 (note 2)

This is a loop of 3.

If the prisoner encounters a loop that is bigger than 50, they will not be able to get to the end of the loop 
and neither will the other prisoners with numbers existing in the same loop.

So the probability of all the prisoners succeeding is exactly the same as 
the probability of a random arrangement of 100 numbers containing no loops that stretches longer than 50

The probability of there being a loop longer than 50 is: 

1/51 + 1/52 + 1/53……….+1/100 = 0.69

Nice.
This means that there is a 31% of success
