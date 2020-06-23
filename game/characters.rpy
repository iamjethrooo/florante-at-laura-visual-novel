init python:
    def character_thumb(thumbnail_name):
        return im.FactorScale(thumbnail_name, 0.6)
################################################################################
## Characters
################################################################################

define t = Character("Tagapagsalaysay", color="#6699cc")
define florante = Character("Florante", color="#FFFFFF")
define aladin = Character("Aladin", color="#FFFFFF")
define adolfo = Character("Adolfo", color="#FFFFFF")
define duke_briseo = Character("Duke Briseo", color="#FFFFFF")
define laura = Character("Laura", color="#FFFFFF")
define haring_linceo = Character("Haring Linceo", color="#FFFFFF")
define heneral_osmalik = Character("Heneral Osmalik", color="#FFFFFF")
define count_adolfo = Character("Count Adolfo", color="#FFFFFF")
define unknown = Character("???", color="#FFFFFF")
define flerida = Character("Flerida", color="#FFFFFF")
define sultan_ali_adab = Character("Sultan Ali-Adab", color="#FFFFFF")
define heneral = Character("Heneral", color="#FFFFFF")
define menandro = Character("Menandro", color="#FFFFFF")

################################################################################
## Images
################################################################################

## Florante
image florante = character_thumb("characters/florante.png")
image florante flip = character_thumb(im.Flip("characters/florante.png", horizontal=True))
image florante speaking = character_thumb("characters/florante speaking.png")
image florante speaking flip = character_thumb(im.Flip("characters/florante speaking.png", horizontal=True))

## Aladin
image aladin = character_thumb("characters/aladin.png")
image aladin flip = character_thumb(im.Flip("characters/aladin.png", horizontal=True))
image aladin speaking = character_thumb("characters/aladin speaking.png")
image aladin speaking flip = character_thumb(im.Flip("characters/aladin speaking.png", horizontal=True))

## Adolfo
image adolfo = character_thumb("characters/adolfo.png")
image adolfo flip = character_thumb(im.Flip("characters/adolfo.png", horizontal=True))
image adolfo speaking = character_thumb("characters/adolfo speaking.png")
image adolfo speaking flip = character_thumb(im.Flip("characters/adolfo speaking.png", horizontal=True))

## Characters
screen characters():
    tag menu

    use game_menu(_("Characters")):
        fixed:
            vpgrid:
                style_prefix "chars"
                xalign 0.5
                yalign 0.2
                cols 2
                spacing 50
                draggable True
                mousewheel True

                vbox:
                    textbutton _("Florante") action Show("character_card", dissolve, "Florante", "characters/cards/Florante.png")
                vbox:
                    textbutton _("Laura") action Show("character_card", dissolve, "Laura", "characters/cards/Laura.png")             
                vbox:
                    textbutton _("Adolfo") action Show("character_card", dissolve, "Adolfo", "characters/cards/Adolfo.png")
                vbox:
                    textbutton _("Flerida") action Show("character_card", dissolve, "Flerida", "characters/cards/Flerida.png")
                vbox:
                    textbutton _("Aladin") action Show("character_card", dissolve, "Aladin", "characters/cards/Aladin.png")

style chars_button_text:
    font "fonts/PrinceValiant.ttf"
    size 35


## Character Details
screen character_card(name, image_loc):
    tag menu

    use game_menu(name):
        fixed:
            add g.make_button(name, im.FactorScale(image_loc, 0.7))