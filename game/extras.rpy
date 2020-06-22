## Extras
screen extras:
    tag menu

    use game_menu(_("Extras")):

        fixed:
            style_prefix "extras"
            vbox:
                yalign 0.2
                textbutton "Art Gallery" action ShowMenu("gallery")
            vbox:
                yalign 0.4
                textbutton "Chapter Picker" action ShowMenu("chapterpicker")             
            vbox:
                yalign 0.6
                textbutton "Characters" action ShowMenu("characters")

style extras_vbox is vbox

style extras_vbox:
    xalign 0.5

style extras_button_text:
    #xalign 0.5
    #font "fonts/PrinceValiant.ttf"
    size 40