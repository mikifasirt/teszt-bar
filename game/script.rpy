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
#image griddy

define sz = Character("Szlevente",color="#39FF14")
define k = Character("Barna",color="#b5894a")
define t = Character("Tanner",color="#1E8DE1")
define mindenki = Character("Mindenki",color="#BEEA15")
define m = Character("Miki Móka", color="#E31C22")
define gyula = Character("Gyula", color="#E31C22")
define edvin= Character("Edvin", color="#BEEA15")
define csongor= Character("Csongor", color="#27D8C5")
define mea= Character("Mysterious elvállt apuka", color="#E31C86")
define griddy = Character("Griddy", color="#184888")
define any = Character("2 gyerekes elvállt anyuka", color="#DC1CE3")
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


    scene bg flott
    with fade 
    
    show krasz at right
    k "Ez a hely tele van kasóval😠😡😡"

    hide krasz
    show bolcs miki at right
    mea "Vigyázzanak fiúk😣 nagyon sok erre a pedofil mostanában🤕"
    mea "Ez mind az incidens óta van így🤓☝️"
    mea "Minden 2009. Október 29.-én kezdődött{cps=5}....{/cps}🥸"

    hide bolcs miki

    show tanner at truecenter

    t "Hallgasson maga sumák!🤬😡🤬"

    hide tanner
    show szlevy at left

    menu:
        "szólj bele":
            jump szolbel
        "ne szólj bele":
            jump neszol
        "üsd meg a griddyt":
            jump griddy

    label griddy:
        show szlevy at left
        sz "Na jó, de ha már itt vagyunk, akkor csináljunk valamit🤓☝️"
        show griddy at right
        griddy "légyszi Szlevente József, ne verj meg léccike fr👉👈"
        hide szlevy
        show tanner at truecenter
        t"a légy nem is szives😢🙁"
        hide tanner
        show szlevy at left
        sz"Késő már griddy úrfi😡"
        "Megüti a griddyt😞"
        #animacio stickfigure szlevy griddy
        $ renpy.notify("Griddy emlékezni fog erre")
        sz "Hát ez nem volt valami okos döntés😨"
        sz "😤De mindegy, most már úgysem számit{cps=2}....{/cps}"
        "Lehajtott fejjel a flott majdnem nonstop abc és dohányboltba megy a gang"
        jump flottben

    label szolbel:
        show szlevy at left
        show bolcs miki at right
        sz"igaza van a kurva anyád te igénytelen palkó😠🥺"
        show tanner at truecenter
        t "nekem mindig az van fiam😎😎"
        hide tanner
        hide szlevy
        mea "jo de amugy van aprotok haversracok"
        show szlevy at left
        sz"nem tudom de a kasóval nem szívesen találkoznék"
        mea "mi a manorol dumalsz faszilada"
        "megdobja majonézzel"
        mea "akkor menjetek a herembe kinda..."
        sz" ez nem is volt olyan rossz"
        hide szlevy
        show gyula at left:
            xzoom -1
        gyula "itt van 13 forint de csak ha feher monsterre költöd"
        gyula "Mentsük meg európát"
        mea " ohh... >_<"
        "hagyjátok szenvedni" #lehet itt is menu
        "Befáradtok a flott majdnem nonstop abc és dohányboltba"
        jump flottben
    label neszol:
        "Nem szólsz bele"
        $ renpy.notify("Tanner emlékezni fog erre")
        hide szlevy
        "Kínos csend"
        "{cps=2}.....{/cps}"
        show bolcs miki at right

        mea "Vigyazz mogotted!!"

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
    return

    label flottben:
        show bg petofront
        with fade
        show tanner at truecenter
        t "Na most már elég volt a hülyeségekből"
        hide tanner
        show bolcs miki at right
        mea "A kasó nem fogja megölni magát"
        hide bolcs miki
        show krasz at right
        k "Dehogy fogja"
        hide krasz 
        show edvin at left
        edvin "TISZTELETTT"
        hide edvin
        show gyula at right
        gyula "Ez tiszta resident evil"
        hide gyula
    

    