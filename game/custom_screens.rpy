################################################################################
## Custom Screens
################################################################################

screen extras:
    tag menu

    imagemap:
        ground "gui/extras ground.png"
        
        hover "gui/extras hovered.png"
        
        hotspot (8, 8, 184, 46) action Return() # return

        hotspot (54, 182, 371, 255) action ShowMenu("coming_soon") # art

        hotspot (460, 184, 371, 254) action ShowMenu("coming_soon") # characters

        hotspot (868, 183, 370, 259) action ShowMenu("chapterpicker") # chapters


screen load_save_slot:
    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty Slot"), FileSaveName(number))
    add FileScreenshot(number) xpos 0 ypos 0
    text file_text xpos 11 ypos -24 size 15  color "#000000"

screen load:

    tag menu
    use file_picker
    add "gui/load.png"

screen save:

    tag menu
    use file_picker
    add "gui/save.png"


screen navigation:

    add "images/forest.jpg"

    imagemap:
        ground "gui/navigation ground.png"
        idle "gui/navigation idle.png"
        selected_idle "gui/navigation hover.png"
        hover "gui/navigation hover.png"
        selected_hover "gui/navigation hover.png"

        alpha False

        hotspot (103, 643, 140, 40) action Return()
        hotspot (299, 643, 92, 40) action ShowMenu("save")
        hotspot (449, 643, 93, 40) action ShowMenu("load")
        # hotspot (598, 643, 160, 40) action ShowMenu("preferences")
        hotspot (815, 643, 210, 40) action MainMenu()
        hotspot (1080, 643, 86, 40) action Quit()

screen file_picker:
    use navigation

    imagemap:
        ground "gui/filepicker ground.png"
        idle "gui/filepicker idle.png"
        selected_idle "gui/filepicker hover.png"
        hover "gui/filepicker hover.png"
        selected_hover "gui/filepicker hover.png"
        
        alpha False

        hotspot (302, 109, 40, 40) action FilePage("auto")
        hotspot (450, 109, 25, 40) action FilePage(1)
        hotspot (511, 109, 33, 40) action FilePage(2)
        hotspot (583, 109, 32, 37) action FilePage(3)
        hotspot (657, 109, 27, 40) action FilePage(4)
        hotspot (724, 109, 33, 40) action FilePage(5)
        hotspot (797, 109, 30, 40) action FilePage(6)
        hotspot (867, 109, 32, 40) action FilePage(7)
        hotspot (936, 109, 32, 40) action FilePage(8)

        hotspot (88, 191, 257, 186) action FileAction(0):
            use load_save_slot(number=0)
        hotspot (367, 191, 257, 186) action FileAction(1):
            use load_save_slot(number=1)
        hotspot (646, 191, 257, 186) action FileAction(2):
            use load_save_slot(number=2)
        hotspot (925, 191, 257, 186) action FileAction(3):
            use load_save_slot(number=3)
        hotspot (88, 392, 257, 187) action FileAction(4):
            use load_save_slot(number=4)
        hotspot (367, 392, 257, 186) action FileAction(5):
            use load_save_slot(number=5)
        hotspot (646, 392, 257, 186) action FileAction(6):
            use load_save_slot(number=6)
        hotspot (925, 392, 257, 186) action FileAction(7):
            use load_save_slot(number=7)


screen about:
    tag menu
    use navigation
    add "gui/about.png"

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    vbox:
        xalign 0.0
        xoffset 70
        yalign 0.5
        xmaximum 1230
        text "[config.name!t]":
            outlines [(2, "#000000", 0, 0)]
            xalign 0.5
            font falfont
        text _("Version [config.version!t]\n"):
            outlines [(2, "#000000", 0, 0)]
            font falfont

        ## gui.about is usually set in options.rpy.
        if gui.about:
            text "[gui.about!t]\n":
                outlines [(2, "#000000", 0, 0)]
                font falfont

        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"):
            outlines [(2, "#000000", 0, 0)]
            font falfont
  


screen chapterpicker:
    tag menu
    use navigation

    imagemap:
        ground "gui/chapterpicker1 ground.png"
        idle "gui/chapterpicker1 idle.png"
        hover "gui/chapterpicker1 hover.png"
        selected_idle "gui/chapterpicker1 hover.png"
        selected_hover "gui/chapterpicker1 hover.png"

        alpha False

        if persistent.ch01:
            hotspot (257, 90, 219, 42) action Start("ch01")
        if persistent.ch02:
            hotspot (258, 206, 229, 44) action Start("ch02")
        if persistent.ch03:
            hotspot (257, 326, 227, 43) action Start("ch03")
        if persistent.ch04:
            hotspot (259, 446, 223, 42) action Start("ch04")
        if persistent.ch05:
            hotspot (257, 563, 231, 41) action Start("ch05")
        if persistent.ch06:
            hotspot (784, 91, 236, 38) action Start("ch06")
        if persistent.ch07:
            hotspot (787, 207, 231, 48) action Start("ch07")
        if persistent.ch08:
            hotspot (787, 327, 229, 43) action Start("ch08")
        if persistent.ch09:
            hotspot (787, 447, 229, 43) action Start("ch09")
        if persistent.ch10:
            hotspot (787, 566, 241, 38) action Start("ch10")


screen characters:
    tag menu
    use navigation

    imagemap:
        ground "gui/characters ground.png"
        idle "gui/characters idle.png"
        hover "gui/characters hover.png"
        selected_idle "gui/characters hover.png"
        selected_hover "gui/characters hover.png"   

        hotspot (294, 139, 262, 70) action Show("character_details", None, "Florante", "Makisig na binatang anak ni Duke Briseo at Prinsesa Floresca.  \nSiya ang pangunahing tauhan ng awit.  \nHalal na Heneral ng hukbo ng Albanya.  \nMagiting na bayani, mandirigma at heneral ng hukbong \nmagtatanggol sa pagsalakay ng mga Persiyano at Turko.")

screen character_details(name, desc):
    tag menu
    use navigation

    text "{size=50}[name]{/size}":
        font falfont
        xpos 300
        ypos 150
        outlines [ (2, "#000000", 0, 0)]
    text "{size=25}[desc]{/size}":
        font falfont
        xpos 300
        ypos 200
        outlines [ (2, "#000000", 0, 0)]

screen coming_soon:
    tag menu
    use navigation
    add "gui/comingsoon.png"
