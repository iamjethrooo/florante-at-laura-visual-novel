init python:
    def gallery_thumbnail(thumbnail_name):
        return im.FactorScale(thumbnail_name, 0.2)
    # Step 1. Create the gallery object.
    g = Gallery()
    g.transition = dissolve
    # Step 2. Add buttons and images to the gallery.

    # A button with an image that is always unlocked.
    g.button("bg1")
    g.image("bg1")
    g.condition("True")
    # A button that contains an image that automatically unlocks.
    g.button("bg2")
    g.image("bg2")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("bg3")
    g.image("bg3")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("bg4")
    g.image("bg 4")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("bg5")
    g.image("bg 5")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("bg6")
    g.image("bg 6")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("bg7")
    g.image("bg 7")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("bg8")
    g.image("bg 8")
    g.condition("True")

    # A button that contains an image that automatically unlocks.
    g.button("bg9")
    g.image("bg 9")
    g.condition("True")

    g.button("florante")
    g.unlock_image("florante")

    g_buttons_pages = [
        [
            ("bg1", "bg1", "bg1.png"),
            ("bg2", "bg2", "bg2.png"),
            ("bg3", "bg3", "bg3.png"),
            ("bg4", "bg4", "bg4.png"),
            ("bg5", "bg5", "bg5.png"),
            ("bg6", "bg6", "bg6.png")
        ],
        [
            ("bg7", "bg1", "bg1.png"),
            ("bg8", "bg2", "bg2.png"),
            ("bg9", "bg3", "bg3.png"),
            (None, None, None),
            (None, None, None),
            (None, None, None)
        ],
        [
            (None, None, None),
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
