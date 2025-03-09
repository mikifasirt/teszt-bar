# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
##############################################################################
# InvItem class




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
define mea= Character("Mysterious elvállt apuka", color="#E31C86")
# The game starts here.

label start:

    python:
        # disable rollback during battle
        battling = False
        renpy.suspend_rollback(battling)

        # battle stats
        playerLV = 1
        playerMAXHP = HPvalues[1]
        playerHP = HPvalues[1]
        playerATK = ATKvalues[1]
        playerDEF = DEFvalues[1]
        playerLUC = LUCvalues[1]
        playerEXP = 0

        # calculate exp to next level
        nextEXP = round( 0.04 * (playerLV ** 3) + 0.8 * (playerLV ** 2) + 2 * playerLV)
        # this formula is from disgaea, apparently!
        # http://howtomakeanrpg.com/a/how-to-make-an-rpg-levels.html

        # enemy defaults
        enemyHP = 1
        seen_enemies = []
    ##

    ## copy this block into your own game
    python:
        gold = 20 #starting amount
        inv = []
        seen_items = []

        # crafting
        known_recipes = []
        seen_recipes = []
        made_recipes = []
        newitem = ""

        # shop inventory
        market = []

        # quests
        new_quests = []
        active_quests = []
        completed_quests = []

    ## CRAFT/SHOP SETUP
    $ known_recipes = ["item_sugar", "item_sucker"]
    $ market = [ "item_water", "item_paper", "item_beet" ]

    ## INVENTORY SETUP
    $ InvItem(*item_sugar).pickup(3)
    $ InvItem(*item_water).pickup(2)
    # $ InvItem(*item_sucker).pickup(1)
    # $ InvItem(*item_beet).pickup(200)

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

    call pre_battle

    scene bg flott
    with fade 
    
    show krasz at right
    k "Ez a hely tele van kasóval😠😡😡"

    hide krasz
    show bolcs miki at right
    mea "Vigyázzanak fiuk nagyon sok erre a pedofil mostanában"
    mea "Ez mind az incidens óta van így"
    mea "Minden 2009. Október 29.-én kezdődött...."

    hide bolcs miki

    show tanner at truecenter

    t "Hallgasson maga sumák!"

    hide tanner
    show szlevy at left

    sz "De tényleg faszi kit érdekel" #itt lehet h kiagazik h mit mondasz de akko szlevy a protagonist

    hide szlevy
    show bolcs miki at right

    mea "Vigyázz mögötted!!"

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
    