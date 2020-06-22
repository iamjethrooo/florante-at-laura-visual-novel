init python:
    def gallery_thumbnail(thumbnail_name):
        return im.FactorScale(thumbnail_name, 0.2)
    # Step 1. Create the gallery object.
    g = Gallery()
    g.transition = dissolve
    # Step 2. Add buttons and images to the gallery.

    # A button with an image that is always unlocked.
    g.button("Forest 1")
    g.image("Forest 1")
    g.condition("True")
    # A button that contains an image that automatically unlocks.
    g.button("Higera")
    g.image("Higera")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("Forest 2")
    g.image("Forest 2")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("Aladin's Makeshift home")
    g.image("Aladin's Makeshift home")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("Flat Rock")
    g.image("Flat Rock")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("Mountains")
    g.image("Mountains")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("Athens 1")
    g.image("Athens 1")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("Athens 2")
    g.image("Athens 2")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("Athens Stage")
    g.image("Athens Stage")
    g.condition("True")

    g.button("Athens 3")
    g.image("Athens 3")
    g.condition("True")

    g.button("Albania 1")
    g.image("Albania 1")
    g.condition("True")

    g.button("Albania Interior 1")
    g.image("Albania Interior 1")
    g.condition("True")

    g.button("Albania Interior 2")
    g.image("Albania Interior 2")
    g.condition("True")

    g.button("Albania 2")
    g.image("Albania 2")
    g.condition("True")

    g.button("Croton Exterior 1")
    g.image("Croton Exterior 1")
    g.condition("True")

    g.button("Croton Exterior 2")
    g.image("Croton Exterior 2")
    g.condition("True")

    g.button("Croton Interior 1")
    g.image("Croton Interior 1")
    g.condition("True")

    g.button("Aetolia")
    g.image("Aetolia")
    g.condition("True")

    g.button("Forest 2 Night")
    g.image("Forest 2 Night")
    g.condition("True")

    g.button("Albania 2 Night")
    g.image("Albania 2 Night")
    g.condition("True")

    g.button("Persia 1")
    g.image("Persia 1")
    g.condition("True")

    g.button("Persia 2")
    g.image("Persia 2")
    g.condition("True")

    g.button("Persia Interior 2")
    g.image("Persia Interior 2")
    g.condition("True")

    g.button("Persia Interior 1 Night")
    g.image("Persia Interior 1 Night")
    g.condition("True")

    g.button("Persia 1 Night")
    g.image("Persia 1 Night")
    g.condition("True")

    g.button("Florante")
    g.image("characters/cards/Florante.png")
    g.condition("True")

    g.button("Laura")
    g.image("characters/cards/Laura.png")
    g.condition("True")

    g.button("Adolfo")
    g.image("characters/cards/Adolfo.png")
    g.condition("True")

    g.button("Flerida")
    g.image("characters/cards/Flerida.png")
    g.condition("True")

    g.button("Aladin")
    g.image("characters/cards/Aladin.png")
    g.condition("True")

    g_buttons_pages = [
        [
            ("Forest 1", "Forest 1", "forest1.png"),
            ("Higera", "Higera", "Higera.png"),
            ("Forest 2", "Forest 2", "Forest 2.png"),
            ("Aladin's Makeshift Home", "Aladin's Makeshift Home", "Aladin's Makeshift Home.png"),
            ("Flat Rock", "Flat Rock", "Flat Rock.png"),
            ("Mountains", "Mountains", "Mountains.png")
        ],
        [
            ("Athens 1", "Athens 1", "Athens 1.png"),
            ("Athens 2", "Athens 2", "Athens 2.png"),
            ("Athens Stage", "Athens Stage", "Athens Stage.png"),
            ("Athens 3", "Athens 3", "Athens 3.png"),
            ("Albania 1", "Albania 1", "Albania 1.png"),
            ("Albania Interior 1", "Albania Interior 1", "albania int 1.png")
        ],
        [
            ("Albania Interior 2", "Albania Interior 2", "albania int 1.png"),
            ("Albania 2", "Albania 2", "Albania 2.png"),
            ("Croton Exterior 1", "Croton Exterior 1", "Croton Ext 2.png"),
            ("Croton Exterior 2", "Croton Exterior 2", "Croton Ext 2.png"),
            ("Croton Interior 1", "Croton Interior 1", "Croton Ext 2.png"),
            ("Aetolia","Aetolia", "aetolia.png")
        ],
        [
            ("Forest 2 Night", "Forest 2 Night", "Forest 2.png"),
            ("Albania 2 Night", "Albania 2 Night", "Albania 2.png"),
            ("Persia 1", "Persia 1", "Persia Ext 1.png"),
            ("Persia 2", "Persia 2", "Persia Ext 2.png"),
            ("Persia Interior 2", "Persia Interior 2", "Persia Ext 2.png"),
            ("Persia Interior 1 Night", "Persia Interior 1 Night", "Persia Ext 2.png")
        ],
        [
            ("Persia 1 Night", "Persia 1 Night", "Persia Ext 1.png"),
            (None, None, None),
            (None, None, None),
            (None, None, None),
            (None, None, None),
            (None, None, None)
        ]
    ]

screen gallery_buttons(data):
    for (name, title, thumbnail) in data:
        if name:
            vbox:
                $ the_button = g.make_button(name, gallery_thumbnail(thumbnail))
                add the_button
                if g.buttons[name].check_unlock():
                    text title
                else:
                    text ""
        else:
            text ""

# Step 3. The gallery screen we use.
screen gallery:
    default page = 1
    # Ensure this replaces the main menu.
    tag menu

    # The background.
    #add "Cabin1.png"

    # A grid of buttons.
    use game_menu(_("Gallery"), scroll="viewport"):

        style_prefix "gallery"    
        vbox:
            xsize 940
            ysize 500

            label "Page [page]":
                xalign 0.5
                bottom_margin 10

            grid 3 2:
                style_prefix "gallery_slot"

                xalign 0.5
                yalign 0.5

                xspacing 30
                yspacing 20
                
                use gallery_buttons(g_buttons_pages[page-1])

            hbox:
                style_prefix "page"

                anchor (0.5, 0.0)
                pos (0.5, 1.0)

                spacing gui.page_spacing

                if page > 1:
                    textbutton "<" action SetScreenVariable("page", page-1)
                else:
                    textbutton "<" action NullAction()

                for i in range(1, len(g_buttons_pages) + 1):
                    textbutton "[i]" action SetScreenVariable("page", i)

                if page < len(g_buttons_pages):
                    textbutton _(">") action SetScreenVariable("page", page + 1)
                else:
                    textbutton  _(">") action NullAction()

style gallery_slot_text:
    size 18
    xalign 0.5
    yalign 0.0

style gallery_button is button:
    hover_background "#fff"

style gallery_button_text:
    size 24
    bold True
    color "#fff"
    hover_color "#000"
    underline True

style gallery_button_current is button
style gallery_button_current_text is gallery_button_text:
    underline False
    hover_color "#fff"
