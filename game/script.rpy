# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image krasz=im.Scale("images/kraszhappy.png",600,1000)
image szlevy=im.Scale("images/szlevy.png",600,1000)
image tanner=im.Scale("images/tanner.png",600,1000)
image gyula=im.Scale("images/gyula.png",600,1000)
image edvin=im.Scale("images/edvin.png",600,1000)
image csongor=im.Scale("images/csongor.png",600,1000)
image bolcs miki=im.Scale("images/bolcsmiki.png",600,1000)

define sz = Character("Szlevente",color="#39FF14")
define k = Character("Barna",color="#b5894a")
define t = Character("Tanner",color="#1E8DE1")
define mindenki = Character("Mindenki",color="#BEEA15")
define m = Character("Miki Móka", color="#E31C22")
define gyula = Character("Gyula", color="#E31C22")
define edvin= Character("Edvin", color="#BEEA15")
define csongor= Character("Csongor", color="#27D8C5")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene bg petofront
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show szlevy at left

    # These display lines of dialogue.

    sz "heh.. Szóval igaz a hír🙄😪"
    sz "Kasó tényleg pedó😣😰"

    show tanner at truecenter
    hide szlevy

    t "Ekkora sumákot😡😡😠"

    hide tanner
    show krasz at right


    k "Sziasztok😁😲 \nen Barna Krasz😀😎"
    hide krasz
    show szlevy at left

    sz "Véget kell vessünk kasó rémuralmának🤠😾"

    show tanner at truecenter
    show krasz at right
    
    mindenki "Induljunk hát meg silly osztag😜😝🤪"

    menu: 
        sz "Hova a manoba indulunk?"

        "Az ovodába":
            jump ovoda
        "A flott majdnem nonstop abc és dohányboltba":
            jump flott
        "Haza":
            jump haza

label flott:  

    scene bg flott
    with fade 

    show krasz at right
    k "Ez a hely tele van kasóval😠😡😡"

    hide krasz
    show bolcs miki at right
    "mysterious elvállt apuka" "Vigyázzanak fiuk nagyon sok erre a pedofil mostanában"
    "mysterious elvállt apuka" "Ez mint az incidens óta van így"
    "mysterious elvállt apuka" "Minden 2009. Október 29.-én kezdődött...."

    hide bolcs miki

    show tanner at truecenter

    t "Hallgasson maga sumák!"

    hide tanner
    show szlevy at left

    sz "De tényleg faszi kit érdekel" #itt lehet h kiagazik h mit mondasz de akko szlevy a protagonist

    hide szlevy
    show bolcs miki at right

    "mysterious elvállt apuka" "Vigyázz mögötted!!"

    hide bolcs miki
    show krasz at right
    k"Dehogy öttem mög xddd"

    "Barnát eltalálja egy kalapács"

    hide krasz 
    show gyula at right

    gyula "Ez tiszta resident evil"

    hide gyula 
    show edvin at left
    edvin "TISZTELETTT"

    hide edvin
    show csongor at top
    csongor "Kussolj már gyula"




    # This ends the game.
    
    return
    