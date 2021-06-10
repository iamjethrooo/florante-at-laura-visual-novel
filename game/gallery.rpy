init python:
    def gallery_thumbnail(thumbnail_name):
        return im.FactorScale(thumbnail_name, 0.2)
    # Step 1. Create the gallery object.
    g = Gallery()
    g.transition = dissolve
    # Step 2. Add buttons and images to the gallery.

    # A button with an image that is always unlocked.
    g.button("Forest")
    g.image("forest 1.png")
    g.image("forest 2.png")
    g.image("forest 2 night.png")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("Higera")
    g.image("higera.png")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("Aladin's Makeshift Home")
    g.image("aladin makeshift home.png")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("Flat Rock")
    g.image("flat rock.png")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("Mountains")
    g.image("mountains.png")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("Athens")
    g.image("athens 1.png")
    g.image("athens 2.png")
    g.image("athens 3.png")
    g.image("athens stage.png")
    g.condition("True")

    g.button("Albania")
    g.image("albania 1.png")
    g.image("albania int 1.png")
    g.image("albania int 2.png")
    g.image("albania 2.png")
    g.image("albania 2 night.png")
    g.condition("True")

    g.button("Croton")
    g.image("croton ext 1.png")
    g.image("croton ext 2.png")
    g.image("croton int 1.png")
    g.condition("True")

    g.button("Aetolia")
    g.image("aetolia.png")
    g.condition("True")

    g.button("Persia")
    g.image("persia ext 1.png")
    g.image("persia ext 2.png")
    g.image("persia int 2.png")
    g.image("persia int 1 night.png")
    g.image("persia ext 1 night.png")
    g.condition("True")


    ## Character Cards
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
            ("Forest", "Forest", "forest 1.png"),
            ("Higera", "Higera", "higera.png"),
            ("Aladin's Makeshift Home", "Aladin's Makeshift Home", "aladin makeshift home.png"),
            ("Flat Rock", "Flat Rock", "flat rock.png"),
            ("Mountains", "Mountains", "mountains.png"),
            ("Athens", "Athens", "athens 1.png")
        ],
        [
            ("Albania", "Albania", "albania 1.png"),
            ("Croton", "Croton", "croton Ext 2.png"),
            ("Aetolia","Aetolia", "aetolia.png"),
            ("Persia", "Persia", "persia ext 1.png"),
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
screen gallery():
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
