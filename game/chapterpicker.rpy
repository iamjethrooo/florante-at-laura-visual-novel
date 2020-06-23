## Chapter Picker
screen chapterpicker:
    tag menu

    use game_menu(_("Chapter Picker")):

        fixed:
            style_prefix "chapterpicker"
            vbox:
                yalign 0.2
                textbutton "Ang Paghihinagpis sa Gubat" action ShowMenu("arc01")
            vbox:
                yalign 0.4
                textbutton "Ang Kwento ni Florante at Aladin" action ShowMenu("arc02")             
            vbox:
                yalign 0.6
                textbutton "Sa Pagbulog at Paglitaw ng Araw" action ShowMenu("arc03")

style chapterpicker_vbox is vbox

style chapterpicker_vbox:
    xalign 0.5

style chapterpicker_button_text:
    size 40

## Arc 1
screen arc01:
    tag menu

    use game_menu(_("Ang Paghihinagpis sa Gubat"), scroll="viewport"):

        vbox:
            xfill True
            style_prefix "arc"
            vbox:
                textbutton "Kabanata 1: Paalam" action If(persistent.ch01, Start("ch01"))
            vbox:
                textbutton "Kabanata 2: At Lumitaw si Aladin" action If(persistent.ch02, Start("ch02"))

## Arc 2
screen arc02:
    tag menu

    use game_menu(_("Ang Kwento ni Florante at Aladin"), scroll="viewport"):

        vbox:
            xfill True
            style_prefix "arc"
            vbox:
                textbutton "Kabanata 3: Bulaklak" action If(persistent.ch03, Start("ch03"))
            vbox:
                textbutton "Kabanata 4: Sa Athens" action If(persistent.ch04, Start("ch04"))
            vbox:
                textbutton "Kabanata 5: Eteocles At Polynices: Ang Dula" action If(persistent.ch05, Start("ch05"))                
            vbox:
                textbutton "Kabanata 6: Mensahe Mula sa Pinanggalingan" action If(persistent.ch06, Start("ch06"))
            vbox:
                textbutton "Kabanata 7: Pagsalakay ng Krotona" action If(persistent.ch07, Start("ch07"))
            vbox:
                textbutton "Kabanata 8: Gasuklay na Buwan sa Taas ng Albania" action If(persistent.ch08, Start("ch08"))
            vbox:
                textbutton "Kabanata 9: Tumambang" action If(persistent.ch09, Start("ch09"))
            vbox:
                textbutton "Kabanata 10: Pinalayas na Prinsipe" action If(persistent.ch10, Start("ch10"))

## Arc 2
screen arc03:
    tag menu

    use game_menu(_("Sa Pagbulog at Paglitaw ng Araw"), scroll="viewport"):

        vbox:
            xfill True
            style_prefix "arc"
            vbox:
                textbutton "Kabanata 11: Sigaw ng Isang Dalaga" action If(persistent.ch11, Jump("ch11"))
            vbox:
                textbutton "Kabanata 12: Sa Ako si Flerida" action If(persistent.ch12, Jump("ch12"))
            vbox:
                textbutton "Kabanata 13: Muling Pagsasama" action If(persistent.ch13, Jump("ch13"))                

style arc_button_text:
    size 35