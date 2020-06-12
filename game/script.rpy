# Splashscreen
transform transform_logo:
    on show:
        alpha 0 xalign 0.5 yalign 0.5
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0

transform transform_white:
    on show:
        alpha 0 
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0
        
label splashscreen:
    scene black
    $ renpy.pause(1, hard=True)

    show white at transform_white
    $ renpy.pause(2, hard=True)

    show logo at transform_logo
    $ renpy.pause(4, hard=True)

    hide logo
    $ renpy.pause(2, hard=True)

    hide white
    $ renpy.pause(3, hard=True)

    scene black with dissolve
    show text "NETBEANS presents..." with dissolve
    $ renpy.pause(2.5)
    hide text with fade

    return

# The game starts here.

label start:
    play music "audio/forest.mp3"
    call ch01

    call ch02

    call ch03

    call ch04

    call ch05

    call ch06

    call ch07

    call ch08

    call ch09

    call ch10

    call ch11

    call ch12

    call ch13

    return

label ch01:

    scene black with dissolve
    show text "{size=50}Kabanata 1{/size}" at truecenter with fade
    $ renpy.pause(4)
    show text "{size=25}Ang Gubat{/size}" at truecenter with fade
    $ renpy.pause(4)    
    hide text with dissolve

    scene bg 1 with fade
    t "Sa isang gubat na hindi na naaabutan ng sinag ng araw dahil sa mga malalaking punongkahoy at makakapal na dahon."

    t "Mga baging na matitinik na bumabalot sa mga sanga."

    t "Maririnig rin ang huni ng mga ibon na nakalulunos."

    t "Makikita rin ang mga hiyena, sierpe, leon at tigre na gumagala."

    $ persistent.ch01 = True

    return

label ch02:

    scene black with dissolve
    show text "{size=50}Kabanata 2{/size}" at truecenter with fade
    $ renpy.pause(4)
    show text "{size=25}Ang Binatang Nakagapos{/size}" at truecenter with fade
    $ renpy.pause(4)    
    hide text with dissolve

    scene bg 2 with fade
    t "Sa gitna ng gubat ay may isang binatang nakagapos ang mga kamay, mga paa at leeg sa isang punong Higera na ang kulay ng dahon ay kumukupas na."

    t "Ang binata ay isang adonis. Makinis ang balat, pula ang pisngi at sapong ginto ang kanyang buhok."

    t "Kanyang mga mata ay lumuluha."

    show florante at left
    florante "O! Langit nasaan ang iyong bangis? Ang bandila ng kasamaan ay nagwawagayway sa kahariang Albanya."

    florante "Ikaw ang dahilan sa lahat! Sa korona ni Haring Linceo at ang kayamanan ng aking amang Duke."

    florante "Konde Adolfo! Ang dahilan ng paglago ng  kasamaan!"

    florante "O! Langit di mo ba naririnig ang aking sigaw? Ang aking mga iyak at hiyaw?"

    florante "Diyos…"
    hide florante
    $ persistent.ch02 = True

    return

label ch03:

    scene black with dissolve
    show text "{size=50}Kabanata 3{/size}" at truecenter with fade
    $ renpy.pause(4)
    show text "{size=25}Alaala ni Laura{/size}" at truecenter with fade
    $ renpy.pause(4)    
    hide text with dissolve

    scene bg 2 with fade

    show florante at left
    florante "Aking sinta… Laura, maalala mo ang pagmamahal mo sa akin… Laura ikaw ang sanhi ng aking ligayang matamis…"

    florante "Laura… sa aking panaginip, ang pag-ibig natin ay mahahanap ang isa’t isa. Masakit isipin ang makita kang umiiyak."

    florante "Pero ang tadhana, napaka-asim kung ikaw ay nasa kamay ng iba…  Sa kamay ni Adolfo… Ang kapalaran ko ba’y kamatayan para di ko maramdaman ang sakit na ito?"
    hide florante

    $ persistent.ch03 = True

    return

label ch04:

    scene black with dissolve
    show text "{size=50}Kabanata 4{/size}" at truecenter with fade
    $ renpy.pause(4)
    show text "{size=25}Daing ng Pusong Nagdurusa{/size}" at truecenter with fade
    $ renpy.pause(4)    
    hide text with dissolve

    scene bg 2 with fade
    t "Ang kanyang pag-iisip ay nagugulo sa pagitan ng kamalayan at pagkahimatay."

    show florante at left
    florante "Laura! Hindi ba sinabi mo na hindi mo ako itataksil?"

    florante "Pinaniwalaan kita, nabulag ba ako sa iyong kagandahan?"

    florante "Naalala mo ba...?"

    menu memories:
        florante "Naalala mo ba...?"

        "Sagisag" if not persistent.sagisag:
            florante "Noong ang ama mo'y inutusan akong makipagdigmaan sa anumang siyudad."
            florante "Ihahanda mo ang aking sagisag na iniyakan mo ng luhang perlas"
            $ persistent.sagisag = True
            jump memories
        "Plumahe" if not persistent.plumahe:
            florante "Ang aking plumahe iyong itinatali parang korales."
            $ persistent.plumahe = True
            jump memories
        "Damit" if not persistent.damit:
            florante "Madalas ang aking damit ay basa dahil sa iyong pag-aalala"
            $ persistent.damit = True
            jump memories
        "Baluti at Koleto" if not persistent.baluti:
            florante "Baluti't koleto'y di mo ipapasuot saakin kung may kalawang na magdudumi sa aking suot."
            $ persistent.baluti = True
            jump memories
        "Turbante" if not persistent.turbante:
            florante "Pahihiyasan mo ang turbante ko na pinalamutian ng mga perlas, topasyo, rubi..."
            florante "At ang diyamante sa aking ulo ay ang letrang 'L' sa pangalan mo"
            $ persistent.turbante = True
            jump memories
        "Bulaklak" if not persistent.bulaklak:
            florante "Pag ako'y malungkot ikaw ay namimitas ng mga magagandang bulaklak upang gawing kuwintas para sa aking leeg."
            $ persistent.bulaklak = True
            jump memories
    hide florante
    $ persistent.ch04 = True

    return

label ch05:

    scene black with dissolve
    show text "{size=50}Kabanata 5{/size}" at truecenter with fade
    $ renpy.pause(4)
    show text "{size=25}Halina, Laura{/size}" at truecenter with fade
    $ renpy.pause(4)    
    hide text with dissolve

    scene bg 2 with fade
    show florante at left
    florante "Halina, Laura..."

    florante "Laura, walang iba ang lunas sa sakit na aking nararamdaman…"

    florante "Isang hawak sa iyong kamay ako’y mabubuhay muli…"

    florante "Nais kong muli, na maramdaman ang iyong pag-aaruga…"

    florante "Ngunit Laura! Wala na si Laura! Ako’y tinaksil!"

    florante "Adolfo! Kahit anong pagsubok ang ibigay mo sa akin basta hindi agawin ang puso ni Laura sa akin!"
    hide florante
    $ persistent.ch05 = True

    return

label ch06:

    scene black with dissolve
    show text "{size=50}Kabanata 6{/size}" at truecenter with fade
    $ renpy.pause(4)
    show text "{size=25}Ang Gererong taga Persia{/size}" at truecenter with fade
    $ renpy.pause(4)    
    hide text with dissolve

    scene bg 4 with fade
    t "Isang gererong dumating, Morong pananamit sa siyudad ng Persiya na may turbante ay kalingas-lingas."

    t "Pinigil ang lakad at nagtanaw-tanaw, binitawan ang sibat at kalasag."

    t "Kanyang mga mata ay tumingin sa itaas, parang istatwang nakatayo. Walang kibo, walang pananalita."

    t "Maya-maya siya’y umupo sa ilalim ng puno"

    show aladin at left
    aladin "O palad!"

    aladin "Aking Flerida... Tuwa ko'y wakas na..."
    hide aladin

    t "Sa sobrang galit, siya'y tumayo."

    show aladin at left
    aladin "Taksil! Ama ko’y nagtaksil saakin! Inagaw ang aking sinta, Flerida!"
    
    menu:
        "Tumahimik":
            aladin "..."
        "Sumigaw":
            aladin "AAAAAAAAAAAAA!!!"

    hide florante
    $ persistent.ch06 = True

    return

label ch07:

    scene black with dissolve
    show text "{size=50}Kabanata 7{/size}" at truecenter with fade
    $ renpy.pause(4)
    show text "{size=25}Pag-aalaala sa Ama{/size}" at truecenter with fade
    $ renpy.pause(4)    
    hide text with dissolve

    scene bg 2 with fade
    show florante at left
    florante "Ama, iyong ulo ay itinapat sa kalis… Ang palambit mo’t dalangin sa langit na ako’y maligtas..."

    florante "Pananalangin mo’y di nagaganap noong nahulog ang kalis sa iyong leeg, sa bibig mong huling pangungusap."

    florante "'Adiyos bunso’t buhay mo’y lumipas!'"

    florante "Ama… naalala ko ang iyong madlang pag-irog at pagpapalayaw. Ikaw ang ama na sinuman walang makakadaig."
    hide florante

    $ persistent.ch07 = True

    return

label ch08:

    scene black with dissolve
    show text "{size=50}Kabanata 8{/size}" at truecenter with fade
    $ renpy.pause(4)
    show text "{size=25}Paghahambing sa Dalawang Ama{/size}" at truecenter with fade
    $ renpy.pause(4)    
    hide text with dissolve
    
    scene cabin with fade
    t "Sa puso ng taga-Persya ay naaawa sa mga naririnig."
    show aladin at left
    aladin "Ang aking ama na inagaw ang kasintahan sa akin, ay walang pagmamahal para sa akin. Ina na 'di ko nakilala, ay maagang namatay."
    hide aladin

    show florante at left
    florante "Laura! Paalam. Kahit tinaksil at kinalimutan. Ipapakasal sa iba. Aking habang-buhay na kaligayahan ay nasa sa iyo. Aking puso’y minamahal parin ikaw!"
    hide florante
    $ persistent.ch08 = True

    return

label ch09:

    scene black with dissolve
    show text "{size=50}Kabanata 9{/size}" at truecenter with fade
    $ renpy.pause(4)
    show text "{size=25}Sa Harap ng Dalawang Leon{/size}" at truecenter with fade
    $ renpy.pause(4)    
    hide text with dissolve

    play sound "audio/lion.mp3"
    scene bg 2 with fade
    t "Lumapit ang dalawang leon. Mata’y gutom na gutom sa nakikitang karne nakatali sa puno."

    $ persistent.ch09= True

    return

label ch10:

    scene black with dissolve
    show text "{size=50}Kabanata 10{/size}" at truecenter with fade
    $ renpy.pause(4)
    show text "{size=25}Ang Pagsaklolo{/size}" at truecenter with fade
    $ renpy.pause(4)    
    hide text with dissolve

    scene bg 2 with fade
    florante "Paalam, Albanya!"
    
    scene forest with fade
    t "Mga salita na tumaginting sa gubat."

    t "Ang Moro ay tumakbo sa direksyon kung saan nanggaling ang huling hiyaw ng lalaki."

    t "Kanyang sibat naghahatak-hatak ng mga baging."

    t "Inaapakan ng mga paa ang mga halamang bunga'y nagbibigay sakit."

    t "Ang araw ay sumisinag sa mga mata ng Moro."
    $ persistent.ch10 = True

    return

label ch11:

    scene black with dissolve
    show text "{size=50}Kabanata 12{/size}" at truecenter with fade
    $ renpy.pause(4)
    show text "{size=25}Mabuting Kaibigan{/size}" at truecenter with fade
    $ renpy.pause(4)    
    hide text with dissolve

    t "Gamit ang sibat, sinaksak at hiniwa ang mga leon."

    t "Ang dalawang leon ay bumagsak."

    t "Pinutol ng Moro ang tali sa kamay, paa at leeg ni Florante."

    t "Bumagsak ang binata sa kanyang mga kamay."

    florante "Laura… Halina, mahal ko…"

    return

label ch12:

    scene black with dissolve
    show text "{size=50}Kabanata 12{/size}" at truecenter with fade
    $ renpy.pause(4)
    show text "{size=25}Batas ng Lahat ng Relihiyon{/size}" at truecenter with fade
    $ renpy.pause(4)    
    hide text with dissolve

    t "Nagisin ang binata sa kamay ng isang Moro."

    aladin "Ngayon ligtas ka na sa sakit."

    t "Nagulat si Florante at gumapang palayo kay Aladin."

    aladin "Huwag kang matakot."

    aladin "Kung nasusuklam ka sa aking kandungan, nahuhusgahan akong 'di ka sasaklolohan."

    florante "Isa kang Moro… Na taga-Persya…"

    aladin "At ikaw ay isang taga Albanya…"

    aladin "Isa kang kaaway ng bayan at kapangkat ko ngunit mukhang ang ating pagkakaibigan ay itinadhana."

    aladin "Ako’y isang Moro ngunit nasasaklaw rin ng utos ng Langit, Narinig ko ang iyong iyak, ano pang magagawa ko?"

    florante "Hindi mo nalang sana ako iniligtas… Hindi ko kaya ikarga ang lubhang sakit sa aking puso. Kapag ako’y namatay, nakamit ko na ang kapayapaan."

    return

label ch13:

    scene black with dissolve
    show text "{size=50}Kabanata 13{/size}" at truecenter with fade
    $ renpy.pause(4)
    show text "{size=25}Ang Magkaibigan{/size}" at truecenter with fade
    $ renpy.pause(4)    
    hide text with dissolve

    t "Napaluha ang Moro, habang ang dalawa ay sinisinagan ng araw."

    return
