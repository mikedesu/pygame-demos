# pygame-demos

I decided to start doing this for \#100daysofcode.

Will be blogging about it here. 

Hit me up: 

- [twitter: \@therealdarkmage](https://m.twitter.com/therealdarkmage)
- [codementor.io: \@mikebell66](https://www.codementor.io/mikebell66)

-----

- Day 1 - 6/28/2019: demo1.py: A simple 4-panel color display. A lot of this was ripped out of a previous project template, but is organized well enough that it can be grafted onto easily.
- Day 2 - 6/29/2019: demo2.py: Renders a randomly-colored 20x20 square that follows the mouse cursor. When clicked, cycles thru other random-colors.
    - *9:12pm*: I have an idea that I'm gonna add onto this right now! Will blog when done...
    - *10:35pm*: Squares of different sizes and colors will spawn on the right and move left on the screen. The player can collide with them. If the player's color matches the enemy square color, you get points. If not, you lose points.
    - [Video](https://www.youtube.com/watch?v=48Bou6GnWFM)
- Day 3 - 6/30/2019: Tutoring workday! If I have energy later, will be doing code for these demos eventually... 
    - Student 1: C++ student, optimizing a 5-loop filter system that applies filters to bmp files, day 2 of that project
    - Student 2: Intro CS with Java, basic binary arithmetic
    - Student 3: Intro CS with Python, anaconda setup
    - kinda dead atm and lacking the focus, but I can consider that I did "code" today, blargh! :E 
- Day 4 - 7/1/2019: Tutoring workday! I ended up messing with another Python project for bug bounties last night via requests but I'll have to re-name this repo etc before I can add in my work there to here. I mistakenly thought I'd only be self-coding pygame stuff but here we are.
    - Student 1: C++ and BSTs, really classic stuff. Node pointers, tree traversals, recursion!
    - Student 2: C++ and Arduino, implementing a beeper system. Today is a lot of digital UI stuff. Input handling. Menu display.
    - Student 3: Python. Showed student my work from day1 and day 2 line-by-line. 
    - Student 4: C++. Near-1000-line rpg project.
- Day 5 - 7/2/2019: Tutoring workday! 
    - Student 1: This is not a programming student. Dude needs help writing his Cybersecurity Master's "Capstone" project. Normally, I'm not an English teacher or tutor, but this dude needed the help, and I need the money.
    - Student 2: Java. Valid identifiers. 
    - Student 3: Python. Student was not prepared and we decided to reconvene later.

```
 public class HelloWorld {
    public static void main(String[] args) {
        //int 4Bfort$;
        int B_Fort$;
        int $_4;
        //int B-b34;
        //int For Honor;
    }
}   
```

- Day 6 - 7/3/2019: Tutoring workday!
    - Student 1: Python.
    - Student 2: Web dev. This was...well, lets say I may have a lot less adhd that this guy.
- Day 7 - 7/4/2019: Happy Independence Day!
    - No coding today (oh no!) but as it is a holiday I am not counting this against me and continuing the next day.
- Day 8 - 7/5/2019: Tutoring workday!
    - Student 1: Java. EE student in intro CS.
        - loops
        - arrays
        - if-else statements
        - methods
        - searching
        - sorting
        - exception-handling
    - Student 2: Java.
    - Student 3: Infosec.
- Day 9 - 7/6/2019: Tutoring workday!
    - Student 1: C and forking and pipes! Fun stuff!
    - Student 2: Basic C++. File IO, frequency charts, histograms.
- Day 10 - 7/7/2019: Tutoring workday!
    - Student 1: C++.
    - Student 2: Infosec.
    - Student 3: Java.
- Day 11 - 7/8/2019: Tutoring workday!
    - Student 1: Python
    - Student 2: C++.
- Day 12 - 7/9/2019: Tutoring workday!
    - Student 1: C++.
    - Student 2: Infosec.
    - Student 3: C.
    - Student 4: C++.
- Day 13 - 7/10/2019: Tutoring workday!
    - Student 1: C++.
    - Student 2: C++. 
    - demo3.py: Turns out I had a bug in my demo1.py and demo2.py that caused the game loop to hang/freeze when you pressed the 'q' key to quit, but I've sinced built this "bare-bones" skeleton code for new projects in pygame, complete with a debug-panel built in already!
- Day 14 - 7/11/2019: Tutoring workday!
    - Student 1: Java.
    - Student 2: Python. 
    - Student 3: C++. 
- Day 15 - 7/12/2019: Tutoring workday! Also TGIF!
    - Student 1: C++. "Duck typing". 
- Day 16 - 7/13/2019: Tutoring workday!
    - Student 1: Java.
- Day 17 - 7/14/2019: Tutoring workday!
    - Student 1: Java.
    - Student 2: Security.
- Day 18 - 7/15/2019: Tutoring workday!
    - Student 1: C++.
    - Student 2: C++.
    - Student 3: C++.
    - Finally got to work on actually animating and moving sprites! Really basic, just cycles in a loop, but next step would be to incorporate spritesheeds and different animation contexts.
- Day 19 - 7/16/2019: Tutoring workday!
    - Student 1: Java.
    - Student 2: Java.
    - Student 3: C++.
- Day 20 - 7/17/2019: Day off!!
- Day 21 - 7/18/2019: Tutoring workday! Since I did no coding yesterday, I am still on day 20.
    - Student 1: Java. 
    - Student 2: C++.
    - demo5.py: I've fixed a sprite clipping problem at the same time as implemented animation spritesheets! The animation is still simple, but I have the groundwork to dig into animating multiple contexts such as movement or attacking.
- Day 22 - 7/19/2019: I was hospitalized this day for a GERD-related incident (damn you, sesame chicken from Lucky Wok!) so no coding this day...
- Day 23 - 7/20/2019: Recovery day...will make these days up
- Day 24 - 7/21/2019: Tutoring workday!
    - Student 1: Infosec.
    - Student 2: Java.
- Day 25 - 7/22/2019: Tutoring workday!
    - Student 1: Infosec.
    - Student 2: C++.
    - Student 3: C++.
- Day 26 - 7/23/2019: Tutoring workday!
    - Student 1: Java.
    - Student 2: C++.
    - I have time before my students, so I'll be working on a few things in a new file today: demo6.py
        - Simpler movement
        - Multiple animation contexts per sprite
    - Todo still:
        - Fire a blast
        - Generate an enemy
        - Collision

