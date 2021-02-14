define b = Character("{b}Bear{/b}", color="#8c3526")
define m = Character("{b}Moose{/b}", color="#8c3526")
define be = Character("{b}Beaver{/b}", color="#8c3526")

image bear = im.Scale("bear.png", 400, 600)
image moose = im.Scale("moose.png", 500, 600)
image beaver = im.Scale("beaver.png", 400, 600)

init python:
    config.has_autosave = False
    config.has_quicksave = False
    config.autosave_on_quit = False
    config.autosave_on_choice = False
    mp = MultiPersistent("demo.renpy.org")

init:
    $ timer_range = 0
    $ timer_jump = 0

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 0 at alpha_dissolve

label thisisnotaneasteregg:
    stop music
    scene black with dissolve
    "Hello curious Canadian <3"
    $ renpy.quit()

label start:
    play music "audio/nature.mp3" fadeout 1.0 fadein 1.0
    scene black with dissolve
    "..."
    scene wilderness with dissolve
    "You wake up in the Canadian wilderness."
    "You have absolutely no idea how you got here."
    play sound "audio/stomach.mp3"
    "The only thing you know for certain is that you're craving maple syrup."
    "You ponder a moment on what your next action will be."
    menu:
        "Venture deep into the forest.":
            jump forest
        "Follow the river stream.":
            jump river
        "Go back to sleep.":
            jump sleep


label forest:
    "You decide to embark on an adventure deep into the forest."
    scene black with dissolve
    "You end up walking for quite a while."
    scene mapletrees with dissolve
    "However, when you least expect it, you're surrounded by maple trees!"
    "It's your lucky day!"
    "It's a shame you don't have a tap or spile to get the maple out of these trees though..."
    play sound "audio/bush.mp3"
    "..."
    "When you least expect it, you hear a sound coming from the bushes behind you."
    show moose with dissolve
    m "Well hello there human!"
    m "I heard that you were in dire need of a tap or a spile."
    m "Well fear not young one!"
    m "I have that which your inner Canadian craves!"
    m "So what do you say we make a deal?"
    stop music
    m "{font=fonts/Papyrus.ttf}YOUR SOUL IN EXCHANGE FOR SOME TASTY CANADIAN MAPLE SYRUP.{/font}" with vpunch
    m "Now what do you say?"
    menu:
        "Hmmm... I sure do love maple syrup :D":
            jump syrup
        "Nah, I'll pass":
            jump nah

label syrup:
    play music "audio/nature.mp3" fadeout 1.0 fadein 1.0
    m "Excellent!"
    m "Pleasure doing business with you!"
    "The moose gives you a big container filled with maple syrup."
    "You have absolutely no idea how the moose was carrying this container, but you decide it would be best to not inquire about it."
    "This is definitely way better than a tap or a spile."
    "You smile and thank the moose profoundly."
    m "Well I'll be on my way now!"
    m "Enjoy the syrup."
    hide moose with dissolve
    "The moose dissolves before your eyes."
    "You hug the maple syrup container like there's no tomorrow."
    play sound "audio/bush.mp3"
    "You then proceed to gulp down all the syrup in one go."
    "You then realize that that probably wasn't the best action to take."
    scene black with dissolve
    stop music
    play sound "audio/gg.mp3"
    $ renpy.pause(3, hard=True)
    jump gameover

label nah:
    m "Shame... well I guess you leave me no choice..."
    m "{font=fonts/Papyrus.ttf}FAREWELL YOUNG ONE!{/font}" with vpunch
    play sound "audio/gg.mp3"
    $ renpy.pause(3, hard=True)
    hide moose with dissolve
    jump gameover

label river:
    "You go forth on an adventure following the river upstream."
    scene black with dissolve
    "You can't help but think of delicious Canadian maple syrup during your walk."
    scene dam with dissolve
    "You eventually stumble upon a beaver dam."
    "You decide to get a closer look."
    show beaver with dissolve
    be "STOP RIGHT THERE!"
    be "YOU SHALL NOT PASS!"
    "You immediately stop and stare directly into the beavers eyes."
    be "I WILL ONLY LET YOU PASS THIS DAM ON ONE CONDITION!"
    be "AND THAT CONDITION IS..."
    be "YOU MUST ANSWER THIS QUESTION CORRECTLY!"
    be "NOW, WHAT DO YOU SAY?"
    menu:
        "I'm up for the challenge.":
            jump fine
        "Nah, I'll head back and find another way around. Cya.":
            jump cya

label cya:
    be "WAIT!"
    be "please? :'("
    menu:
        "Ok, fine.":
            jump fine
        "Hmm... alright.":
            jump fine

label fine:
    be "YAAAAY!!" with vpunch
    be "ANYWAYS, YOUR QUESTION IS..."
    be "WHAT'S THE BEST COUNTRY OF THEM ALL?"
    $ country = renpy.input("ANSWER TRUTHFULLY! (case-sensitive)")
    $ country = country.strip()
    if country == "Canada":
        be "YES YES YES YES YES YES!!!" with vpunch
        be "YOU ARE RIGHT!!"
        be "CANADA SURE IS THE BEST COUNTRY OF THEM ALL!!"
        be "VERY WELL! YOU ARE ALLOWED TO PASS!"
        menu:
            "Thanks :)":
                jump thanks


    be "DID YOU JUST..."
    be "DID YOU JUST SAY %(country)s?!"
    be "YOU ARE WRONG! AND YOUR PUNISHMENT IS DEATH!!"
    play sound "audio/gg.mp3"
    $ renpy.pause(3, hard=True)
    hide beaver with dissolve
    jump gameover

label thanks:
    scene black with dissolve
    "You start walking in a straight direction until dawn."
    "You've gone so long without maple syrup that you simply have no idea how much longer you'll last."
    "It might even be-{nw}"
    play sound "audio/gg.mp3"
    $ renpy.pause(3, hard=True)
    hide bear with dissolve
    jump gameover

label sleep:
    scene black with dissolve
    stop music
    "You decide it would be best to go back to sleep."
    "You think that perhaps you will wake up with more energy."
    play sound "audio/roar.mp3"
    "..."
    scene wilderness with dissolve
    show bear with dissolve
    "Suddenly, you're attacked by a wild ferocious bear in your sleep."
    b "umm... I'm not a ferocious bear. I'm a friendly Canadia-{nw}"
    "The wild ferocious bear is preparing its attack against you."
    "Your fight or flight instincts activate."
    $ time = 1
    $ timer_range = 1
    $ timer_jump = 'nochoice'
    show screen countdown
    menu:
        "Attack the bear.":
            hide screen countdown
            jump nochoice
        "Run for your life.":
            hide screen countdown
            jump nochoice
label nochoice:
    "The bear does not care about your choices and ferociously attacks you."
    b "I would never do that! I'm-{nw}"
    play sound "audio/gg.mp3"
    $ renpy.pause(3, hard=True)
    hide bear with dissolve
    jump gameover


label gameover:
    scene gameover with dissolve
    play music "audio/flute.mp3"
    pause

    return
