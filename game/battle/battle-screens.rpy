init offset = -1

##############################################################################
## battle menu

screen battle_menu():

    # this flag decides whether to show the main battle menu, or items menu
    default showbattlemenu = True

    tag menu
    style_prefix "battle"

    hbox:
        xalign .5
        yalign .9
        spacing 40

        if showbattlemenu:
            textbutton _("Attack"):
                action Jump("battle_attack")
                tooltip _("Fight! Beat the enemy into submission!")

            textbutton _("Guard"):
                action Jump("battle_defend")
                tooltip _("Protect yourself! Halves incoming damage.")

            textbutton _("Duma"):
                action Jump("battle_duma")
     
    $ tooltip = GetTooltip()

    if tooltip:
        text "[tooltip!t]" xalign .2 yalign .99

default turn = 0
default atkbuff = 0
default defbuff = 0

##############################################################################
## battle overlay

screen battleoverlay():
    zorder 99

    label _("BATTLE!") style "battle_label" align (.5,.05)

    # HP bars
    bar value playerHP range playerMAXHP style "battle_bar" at battle_party1
    bar value enemyHP range enemy.MAXHP style "battle_bar" at battle_enemy1

    frame:
        style_group "battleinfo"
        xalign .1
        yalign 0.5
        vbox:
            hbox:
                xfill True
                label _("Syrup")
                text _("Lv [playerLV]") style "battleHP_text" xalign 1.0

            if not playerHP < playerMAXHP/3:
                text _("HP: [playerHP] / [playerMAXHP]") style "battleHP_text"
            else:
                text _("HP: [playerHP] / [playerMAXHP]") style "battleLOWHP_text"



    frame:
        style_group "battleinfo"
        xalign .9
        yalign 0.5
        vbox:
            label "[enemy.name!t]"
            hbox:
                if enemy.boss:
                    add "bosscrown" yalign .5
                text _("HP: [enemyHP] / [enemy.MAXHP]") style "battleHP_text"
         
            null height 8
            

style battle_label_text:
    size 60
    color "#FFF"
    outlines [(6,"#A51F63",1,1)]

image hp full:
    "gui/bar/left.png"
    nearest True
image hp empty:
    "gui/bar/right.png"
    nearest True
style battle_bar:
    left_bar "hp full"
    right_bar "hp empty"
    xsize 120
    ysize 10
    yoffset 110

style battleinfo_frame:
    xsize 350
    ysize 200
    yalign .7
    padding (16,16)
style battleinfo_vbox:
    spacing 6
style battleinfo_stat_frame:
    background "#ffe0ed"
    xfill True
    padding (10,6)

style battleinfo_label_text:
    color "#FFF"
    outlines [(2,"#525252",0,0),(3,"#525252",1,1)]

style battleinfo_text:
    color "#333"

style battleHP_text:
    color "#FFF"
    outlines [(2,"#5d5d5d",0,0)]
style battleLOWHP_text is battleHP_text:
    outlines [(2,"#bd2c47",0,0)]

style battle_button:
    #background "[prefix_]battle"
    xysize (100,200)
    size_group "battle"
style battle_button_text:
    xalign .7
    idle_color "#31bd2c"
    size gui.label_text_size


##############################################################################
## show damage/crit/heal/miss

## DAMAGE NUMBERS
default damage = 0

screen showdamage(target):
    zorder 100
    style_prefix "damage"

    if target=="player":
        text "[damage]" at battle_party1, playerdamage_appear
    else:
        text "[damage]" at battle_enemy1, damage_appear

    timer .1 action Hide('showdamage')

style damage_text:
    bold True
    color "#FFF"
    outlines [(2,"#000",0,0)]

transform damage_appear:
    on show:
        alpha 1 yoffset -10 xoffset 0
        easeout .05 yoffset -20
    on hide:
        easeout .5 alpha 0 yoffset 100 xoffset 10
transform playerdamage_appear:
    on show:
        alpha 1 yoffset -10 xoffset 0
        easeout .05 yoffset -20
    on hide:
        easeout .5 alpha 0 yoffset 100 xoffset -10

screen showcrit():
    zorder 100
    style_prefix "damage"

    text "[damage]" color "#ff3939" size 36 at battle_enemy1, damage_appear

    timer .1 action Hide('showcrit')

screen showheal():
    zorder 100
    style_prefix "damage"

    # on "show" action Play("sound", audio.heal)

    text "[damage]" color "#53ff55" at battle_party1, heal_appear

    timer .1 action Hide('showheal')

transform heal_appear:
    on show:
        alpha 0 yoffset -10 xoffset 15
        easeout .1 alpha 1
    on hide:
        easeout .6 alpha 0 yoffset -60

screen showmiss():
    zorder 100
    style_prefix "damage"

    text _("MISS") at battle_enemy1, miss_appear

    timer .1 action Hide('showmiss')

transform miss_appear:
    on show:
        alpha 0 yoffset -10
        easeout .1 alpha 1
    on hide:
        easeout .6 alpha 0 yoffset 50
