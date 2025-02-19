# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image krasz=im.Scale("images/kraszhappy.png",600,1000)
image szlevy=im.Scale("images/szlevy.png",600,1000)
image tanner=im.Scale("images/tanner.png",600,1000)

define sz = Character("Szlevente",color="#39FF14")
define k = Character("Barna",color="#b5894a")
define t = Character("Tanner",color="#1E8DE1")
define m = Character("Mindenki",color="#BEEA15")



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

    sz "heh.. Szóval igaz🙄😪\nKasó tényleg pedó"

    show tanner at truecenter
    hide szlevy

    t "Ekkora sumákot😡😡😠"

    hide tanner
    show krasz at right


    k "Sziasztok😁😲 \nen Barna Krasz😀😎"
    hide krasz
    show szlevy at left

    sz "Véget kell vessünk kasó rémuralmának🥺😾"

    show tanner at truecenter
    show krasz at right
    
    m "Induljunk hát meg silly osztag😜😝"

    # This ends the game.
    
    return
    
