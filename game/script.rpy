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
    show white at transform_white
    $ renpy.pause(1, hard=True)

    show logo at transform_logo
    $ renpy.pause(4, hard=True)

    hide logo
    $ renpy.pause(1.5, hard=True)

    hide white
    $ renpy.pause(1.5, hard=True)

    scene black with dissolve
    show text "{size=35}Urban Dino presents...{/size}" with dissolve
    $ renpy.pause(2.5)
    hide text with fade

    return

# The game starts here.

label start:
    play music "audio/forest.mp3"
    call ch01 from _call_ch01

    call ch02 from _call_ch02

    call ch03 from _call_ch03

    call ch04 from _call_ch04

    call ch05 from _call_ch05

    call ch06 from _call_ch06

    call ch07 from _call_ch07

    call ch08 from _call_ch08

    call ch09 from _call_ch09

    call ch10 from _call_ch10

    call ch11 from _call_ch11

    call ch12 from _call_ch12

    call ch13 from _call_ch13

    return

label ch01:

    scene black with dissolve
    show text "{size=50}Arko 1: Ang Paghihinagpis sa Gubat{/size}" at truecenter with fade
    $ renpy.pause(3.5)    
    show text "{size=50}Kabanata 1{/size}" at truecenter with fade
    $ renpy.pause(3)
    show text "{size=25}Paalam{/size}" at truecenter with fade
    $ renpy.pause(2)    
    hide text with dissolve

    scene forest 1 with fade
    t "Sa madilim na gubat na hindi sinisinagan ng araw dahil sa mga malalaking punongkahoy at makakapal na dahon. May mga baging na matitinik na bumabalot sa mga sanga."

    t "Maririnig din ang huni ng mga ibon na nakaaawa. Makikita rin dito ang mga hayina, ahas, leon at tigre na gumagala sa gubat."

    t "Sa gitna ng gubat, ay may isang binatang nakagapos ang mga kamay, mga paa at leeg sa isang puno ng Higera na ang kulay ng mga dahon ay kumukupas na."

    t "Ang binata ay isang adonis. Makinis ang balat, pula ang pisngi at kulay ginto ang kanyang buhok ngunit, ang kanyang mga mata ay lumuluha."

    scene higera with fade
    show florante speaking at left
    florante "O! Langit nasaan ang iyong bangis? Ang bandila ng kasamaan ay nagwawagayway sa kahariang Albanya."

    florante "Ikaw ang dahilan sa lahat! Sa korona ni Haring Linceo at ang kayamanan ng aking amang Duke."

    florante "Konde Adolfo! Ang siyang dahilan ng paglago ng  kasamaan!"

    florante "O! Langit di mo ba naririnig ang aking sigaw? Ang aking mga iyak at hiyaw? Diyos..."

    menu:
        florante "O! Langit di mo ba naririnig ang aking sigaw? Ang aking mga iyak at hiyaw? Diyos..."

        "Kung ito ang pagdurusa na iyong nais...":
            florante "Kung ito ang pagdurusa na iyong nais..."
        "Kapag ang hangad ko na ang kasamaan ay sumuko sa kabutihan ay hindi matupad...":
            florante "Kapag ang hangad ko na ang kasamaan ay sumuko sa kabutihan ay hindi matupad..."

    florante "Aking sinta... Laura, maalala mo pa ba ang pagmamahal mo sa akin... Laura, ikaw ang sanhi ng aking ligayang kay tamis..."

    florante "Laura... sa aking panaginip, ang pag-ibig natin ay mahahanap ang isa’t isa. Masakit isipin ang makita kang umiiyak."

    florante "Pero ang tadhana, napakapait kung ikaw ay nasa kamay ng iba...  Sa kamay ni Adolfo… Ang kapalaran ko ba’y kamatayan para di ko maramdaman ang sakit na ito?"
    hide florante

    t "Ang kanyang pag-iisip ay nagugulo sa pagitan ng kamalayan at pagkahimatay."

    show florante speaking at left
    florante "Laura! Hindi ba sinabi mo na hindi mo ako itataksil?"

    florante "Pinaniwalaan kita, nabulag ba ako sa iyong kagandahan?"

    florante "Naaalala mo ba...?"

    menu memories:
        florante "Naalala mo ba...?"

        "Sagisag" if not persistent.sagisag:
            florante "Noong ang ama mo'y inutusan akong makipagdigmaan sa anumang siyudad. Ihahanda mo ang aking sagisag na iniyakan mo ng luhang perlas"
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
            florante "Pahihiyasan mo ang turbante ko na pinalamutian ng mga perlas, topasyo, rubi... At ang diyamante sa aking ulo ay ang letrang 'L' sa pangalan mo"
            $ persistent.turbante = True
            jump memories
        "Bulaklak" if not persistent.bulaklak:
            florante "Pag ako'y malungkot ikaw ay namimitas ng mga magagandang bulaklak upang gawing kuwintas para sa aking leeg."
            $ persistent.bulaklak = True
            jump memories

    florante "Halina, Laura..."

    florante "Laura, walang iba ang lunas sa sakit na aking nararamdaman… Isang hawak sa iyong kamay ako’y mabubuhay muli..."

    florante "Nais kong muli, na maramdaman ang iyong pag-aaruga..."

    florante "Ngunit Laura! Wala na si Laura! Ako’y tinaksil!"

    florante "Adolfo! Kahit anong pagsubok ang ibigay mo sa akin basta hindi agawin ang puso ni Laura sa akin!"

    florante "Ama, iyong ulo ay itinapat sa kalis... Ang palambit mo’t dalangin sa langit na ako’y maligtas..."

    florante "Pananalangin mo’y di nagaganap noong nahulog ang kalis sa iyong leeg, sa bibig mong huling pangungusap."

    florante "Adiyos bunso’t buhay mo’y lumipas!"

    florante "Ama... naalala ko ang iyong madlang pag-irog at pagpapalayaw. Ikaw ang ama na sinuman walang makakadaig."

    florante "Laura! Paalam. Kahit tinaksil at kinalimutan. Ipapakasal sa iba. Aking habang-buhay na kaligayahan ay nasa sa iyo. Aking puso’y minamahal parin ikaw!"

    t "Lumapit ang dalawang leon. Mata’y gutom na gutom sa nakikitang karne na nakatali sa puno."

    florante "Paalam, Albanya!"
    hide florante

    $ persistent.ch01 = True
    return

label ch02:
    scene black with dissolve 
    show text "{size=50}Kabanata 2{/size}" at truecenter with fade
    $ renpy.pause(3)
    show text "{size=25}At Lumitaw Si Aladin{/size}" at truecenter with fade
    $ renpy.pause(2)    
    hide text with dissolve

    scene forest 2 with fade
    show aladin at left
    t "May isang kawal na dumating, Morong pananamit sa siyudad ng Persiya at ang kanyang turbante ay kalingas-lingas."

    t "Tumigil sa paglalakad at tumanaw, at kanyang binitawan ang sibat at kalasag. "

    t "Ang kanyang mga mata ay tumingin sa itaas na parang istatwang nakatayo. Walang kibo, walang pananalita."

    t "Maya-maya siya’y umupo sa ilalim ng puno."

    show aladin speaking at left
    aladin "O palad!"

    aladin "Aking Flerida... Tuwa ko'y wakas na..."

    hide aladin
    t "Sa sobrang galit siya'y tumayo."

    show aladin speaking at left
    aladin "Taksil! Ama ko’y nagtaksil sa akin! Inagaw ang aking sinta, Flerida!"

    menu:
        aladin "Taksil! Ama ko’y nagtaksil sa akin! Inagaw ang aking sinta, Flerida!"

        "Tumahimik":
            aladin "..."
        "Sumigaw:":
            aladin "AAAAAAAAAAAAAAAAAAHHH!!!"

    show aladin at left
    show florante speaking flip at right
    florante "Adiyos bunso't buhay mo'y lumipas!"
    show florante flip at right
    aladin "?"
    show florante speaking flip at right
    florante "Ama… naalala ko ang iyong madlang pag-irog at pagpapalayaw. Ikaw ang ama na sinuman walang makakadaig."
    show florante flip at right
    t "Sa puso ng taga-Persya ay naaawa sa mga naririnig."
    show aladin speaking at left
    aladin "Ang aking ama na inagaw ang kasintahan sa akin, ay walang pagmamahal para sa akin. Ina na 'di ko nakilala, ay maagang namatay."
    show aladin at left
    show florante speaking flip at right
    florante "Paalam, Albanya!"
    show florante flip at right
    t "Ito ang salita na umalingawngaw sa gubat."

    scene forest 1 with fade

    t "Ang Moro ay tumakbo sa direksyon kung saan nanggaling ang huling hiyaw ng lalaki."

    t "Ang kanyang sibat ay humahatak ng mga baging. "

    t "Mga paa’y inaapakan ang mga halamang nakalalason. "

    t "Ang araw ay sumisinag sa mga mata ng Moro."

    t "Gamit ang sibat, sinaksak at hiniwa ang mga leon. "

    t "Ang dalawang leon ay bumagsak. "

    scene higera with fade

    t "Pinutol ng Moro ang tali sa kamay, paa at leeg ni Florante."

    t "At bumagsak ang binata sa kanyang mga kamay."

    show florante speaking at left
    florante "Laura… Halina, mahal ko..."
    show florante at left
    hide florante with fade
    t "Nagising ang binata sa kamay ng isang Moro."

    show aladin speaking flip at right
    aladin "Ngayon ligtas ka na sa sakit."

    show florante at left
    t "Nagulat si Florante at gumapang palayo kay Aladin. "

    aladin "Huwag kang matakot—"

    aladin "Kung nasusuklam ka sa aking kandungan, nahuhusgahan akong 'di ka sasaklolohan."

    show florante speaking at left
    show aladin flip at right
    florante "Isa kang Moro... Na taga-Persya..."

    show aladin speaking flip at right
    show florante at left
    aladin "At ikaw ay isang taga Albanya..."

    aladin "Isa kang kaaway ng bayan at kapangkat ko ngunit mukhang ang ating pagkakaibigan ay itinadhana."

    aladin "Ako’y isang Moro ngunit nasasaklaw rin ng utos ng Langit, Narinig ko ang iyong iyak, ano pang magagawa ko?"

    show florante speaking at left
    show aladin flip at right
    florante "Hindi mo nalang sana ako iniligtas… Hindi ko kaya ikarga ang lubhang sakit sa aking puso. Kapag ako’y namatay, nakamit ko na ang kapayapaan."
    hide florante
    hide aladin
    t "Napaluha ang Moro, habang ang dalawa ay sinisinagan ng araw."

    t "Tumayo ang Moro."

    show aladin speaking at left
    show florante flip at right
    aladin "Mali ka! Wag mong itapon ang buhay mo ng ganto. Kinakailangan ka ng Albanya, kinakailangan ka ng mahal mo!"

    t "Tinitigan ni Florante si Aladin."
    hide florante with dissolve
    t "Muling nahimatay si Florante."

    scene aladins makeshift home with fade

    show aladin speaking at left
    aladin "Ah! Gising ka na."
    show aladin at left
    t "Mga ilang segundo ang kanyang mata’y naka titig sa langit."
    show florante speaking flip at right
    florante "Ilang araw ang lumipas?"
    show florante flip at right
    show aladin speaking at left
    aladin "Lima? Anim siguro."
    show aladin at left
    show florante speaking flip at right

    florante "Salamat sa pag-aalaga saakin."

    scene flat rock with fade
    show aladin speaking at left
    aladin "Walang anuman."

    aladin "Ako pala si Aladin."

    aladin "At ikaw?"
    show aladin at left
    show florante speaking flip at right
    florante "Florante."
    show florante flip at right
    show aladin speaking at left

    aladin "Tayong dalawa ay may sariling kwento at gusto kitang kilalanin. Sino ang mauuna?"

    $ persistent.ch02 = True
    return

label ch03:

    scene black with dissolve 
    show text "{size=50}Arko 2: Ang Kwento ni Florante at Aladin{/size}" at truecenter with fade
    $ renpy.pause(3.5)    
    show text "{size=50}Kabanata 3{/size}" at truecenter with fade
    $ renpy.pause(3)
    show text "{size=25}Bulaklak{/size}" at truecenter with fade
    $ renpy.pause(2)    
    hide text with dissolve

    scene flat rock with fade

    t "Umupo ang dalawa sa ilalim ng puno. Unang nagkuwento si FLorante kay Aladin."

    show florante speaking at left
    florante "Ako’y ipinanganak sa pamilyang duke sa Albanya. Ama ko si Duke Briseo at ina ko si Prinsesa Floresca. Ngunit, kung ako’y ipinanganak sa pinagmulan ng aking ina, sa Krotona, mas maganda sana ang naging landas ng buhay ko."

    florante "Si Duke Briseo ang nag mistulang pangalawang pinuno ng Albanya dahil siya ang taga-payo ni Haring Linceo. Siya rin ang pinaka mabait, pinaka mapagmahal at ang pinaka.."

    menu:
        florante "Siya rin ang pinaka mabait, pinaka mapagmahal at ang pinaka.."

        "Magiting":
            florante "..magiting"
        "Maalagain":
            florante "..maalagain"
        "Maalalahanin":
            florante "..maalalahanin"

    florante "Espesyal rin ang tawag sakin ni Ama. “Nag-iisa at natatangi kong bulaklak”"
    
    florante "Iyon na ang naging palayaw ko galing sa aking mga magulang mula sa aking pagkabata. Para ko rin ako’y may nadidinig na tumatawag sa aking palayaw ngayo’t ako’y nahihirapan."
    hide florante

    t "Napahinto si Florante na parang bang napaisip ito sa sinabi."

    scene mountains with fade

    show florante speaking at left
    florante "Noong ako’y bata pa, muntik rin akong makuha ng isang buwitre. Naikwento ng aking ina na habang ako’y natutulog sa aming bahay na kinta sa bundok, may pumasok na ibon."

    florante "Dahil sa sigaw ng aking ina, na-alerto ang aking pinsan na si Menalipo na agad niyang pinana ang ibon at ito’y agad na namatay."

    florante "Meron rin naman yung araw na ako’y naiwan sa salas, hindi ko pa kayang makatayo mag-isa."

    florante "Biglang dumating ang isang arko na kinuha ang aking kupidong dyamante mula sa aking dibdib."

    florante "Siyam na taong gulang ako nang makahiligan kong mamalagi sa burol. Namamana ako ng mga ibon."

    florante "Kasisikat ng araw ay nasa gubat na ako, kasama ang mga alagad at pagdating ng tanghaling tapat, ako’y nasa parang. Dito, pinaglalaruan ko ang mga bulaklak."

    florante "Naging masaya ang aking pagkabata."

    menu:
        florante "Naging masaya ang aking pagkabata."

        "Pagpapana ng mga hayop":
            t "Tuwing nakakakita si Florante ng hayop sa kalapit na bundok, pinapana niya ito. Malinaw at matindi ang mga mata ni Florante kaya isang tira lamang at natatamaan niya agad."
        "Panonood sa unahan ng mga kasamahan":
            t "Natutuwa ang mga kasamahan ni Florante sa tuwing siya’y mapapana na hayop. Naaliw siya sa masayang pag-unahan nilang makuha ang patay na hayop, lalo na sa kanilang mga sigaw na tuwa kapag nakita na ang patay na hayop. "
        "Pakikinig sa mga Nayadas":
            t "Tuwing napagsasawaan ni Florante ang pagpapana, siya’y uupo sa tabing bukal upang pakinggan tumugtog ng lira ang mga Nayadas na siyang nakakapag-alis ng lungkot. Pati ang mga ibon, nagtitipon sa pinaka mataas na punong-kahoy upang makinig sa mga Nayadas."
    
    florante "Ngunit, hindi nagtagal itong kasiyahan."

    $ persistent.ch03 = True
    return

label ch04:

    scene black with dissolve 
    show text "{size=50}Kabanata 4{/size}" at truecenter with fade
    $ renpy.pause(3)
    show text "{size=25}Sa Athens{/size}" at truecenter with fade
    $ renpy.pause(2)    
    hide text with dissolve

    scene athens 1 with fade
    show florante speaking at left
    florante "Inutusan ako ng aking ama na umalis noong ako’y labing-isa pa lamang. Bungad daw ito ng kaniyang pagmamahal bilang ama."

    florante "Lalaking mahina ang isang tao kung kasiyahan lamang ang mararanasan. Mahirap mabuhay sa mundo. Kailangan maging matatag ang kalooban."

    florante "Maselan ang isang tao kung sanay sa kasarapan ng buhay. Hindi sila matututong harapin ang katotohanan. Mahihirapang magpatuloy."

    florante "Ito ang mga turo ng ama, kaya kahit maghinagpis ang aking ina, pinadala parin ako sa Atenas upang mag-aral at malantad sa katotohanan."

    florante "Malungkot ang aking nadama sa aking pagdating. Halos isang buwan akong di nakakain ng maayos dala ng matinding kalungkutan."

    scene athens 2 with fade
    show florante speaking at left
    florante "Ngunit nakilala ko ang aking mabait na guro na si Atenor at ang kaklase kong si Adolfo na labing-tatlong taong gulang."
    show florante at left
    t "Si Adolfo ang pinaka matalino sa klase. Halos lahat ay tinitingalaan siya. Mabait, mahinahong at huwarang tao si Adolfo, ngunit maraming lihim sa puso."

    t "Turo ng ama ni Florante na ang talino ay kasama ng pagiging mapagkumbaba. Kaya pinagtataka ng klase kung bakit hindi niya nagugustuhan ang asal ni Adolfo."
    show florante speaking at left
    florante "Hindi ko rin maintindihan sa sarili ko kung bakit ganun man ang aking nadama kay Adolfo."

    florante "Lumipas ang mga araw at pinag-aralan ko ang pilosopiya, astrolohiya, at matematika. Naging propesyonal ako sa tatlong paksa na iyon sa loob ng anim na taon."    
    
    florante "Tuluyan ko ngang nalampasan si Adolfo at ako’y naging kilala sa klase. Lumabas ang kaniyang tunay na kulay."

    menu:
        florante "Tuluyan ko ngang nalampasan si Adolfo at ako’y naging kilala sa klase. Lumabas ang kaniyang tunay na kulay."

        "Nabuking":
            florante "Sa loob-looban ay hindi talaga mabait si Adolfo."
        "Peke":
            florante "Kasinungalingan ang kaniyang pagiging mahinahon."

    florante "Lalo kong napansing ang tunay niyang budhi nang magsimula kami sa pagkanta, at sa pag-laro ng arnis."

    $ persistent.ch04 = True
    return

label ch05:

    scene black with dissolve 
    show text "{size=50}Kabanata 5{/size}" at truecenter with fade
    $ renpy.pause(3)
    show text "{size=25} Eteocles At Polynices: Ang Dula{/size}" at truecenter with fade
    $ renpy.pause(2)    
    hide text with dissolve

    scene athens stage with fade
    show florante speaking at left
    florante "Hindi nagtapos doon. Nagkaroon kami ng dula tungkol sa istorya ni Oedipus."

    florante "Gumanap akong bilang Eteocles, anak ni Oedipus. At si Adolfo ay gumanap bilang Polyneices. Ang isa ko pang kaklaseng si Menandro ay gumanap bilang ama nilang dalawa."

    florante "Bumigkas si Adolfo ng mga salitang wala sa sulat."
    show adolfo flip at right
    menu: 
        florante "Bumigkas si Adolfo ng mga salitang wala sa sulat."

        "Mang-aagaw!":
            show adolfo speaking flip at right
            adolfo "Isa kang mang-aagaw ng pansin! Dapat kang mamatay"
        "Pasikat!":
            show adolfo speaking flip at right
            adolfo "Dumating ka lang para magpasikat! Naghihintay sayo’y kamatayan! "
        "Inggit!":
            show adolfo speaking flip at right
            adolfo "Nalampasan mo lang ako dahil isa kang inggit! Ika’y aking papatayin! "
    hide adolfo
    hide florante
    t "Sumugod si Adolfo kay Florante at tatlong beses na tinangka siyang saksakin. Nahulog si Florante sa kaniyang pag-iwas at siya’y tinulungan ni Menander. Nasangga ni Menander ang susunod na tangka ni Adolfo at tumalsik ang kaniyang espada."
    show florante speaking at left
    florante "Pinauwi si Adolfo pabalik ng Albanya sa sumunod na araw. Nanatili pa ako sa Atenas ng isa pang taon."

    florante "Hinihintay ko ang utos ng ama sa aking muling pag-uwi ngunit, isang liham ang dumating."
    $ persistent.ch05 = True
    return

label ch06:

    scene black with dissolve 
    show text "{size=50}Kabanata 6{/size}" at truecenter with fade
    $ renpy.pause(3)
    show text "{size=25}Mensahe Mula Sa Pinanggalingan{/size}" at truecenter with fade
    $ renpy.pause(2)    
    hide text with dissolve

    scene athens 2 with fade
    show florante speaking at left
    florante "Ang laman ng liham ay ang balitang pumanaw na ang aking ina. Iyon ang unang pinaka matinding sakit na aking nadama."

    florante "Sa sulat na pinadala ng aking ama, naramdaman ko…"

    menu:
        florante "Sa sulat na pinadala ng aking ama, naramdaman ko…"

        "Ang pagka-gulat":
            florante "Nahimatay ako ng dalawang oras dahil sa pag-iisip at pag-aalala. Mabuti nalang at ako’y inalalayan ng mga kaklase."
        "Ang pinaka-mapait na surpresa":
            florante "Nahimatay ako ng dalawang oras dahil sa pag-iisip at pag-aalala. Mabuti nalang at ako’y inalalayan ng mga kaklase."
        "Ang kasamaan ng loob":
            florante "Nahimatay ako ng dalawang oras dahil sa pag-iisip at pag-aalala. Mabuti nalang at ako’y inalalayan ng mga kaklase."

    florante "Sa aking pag-kamalay, naramdaman ko muli ang hapdi sa aking dibdib at hindi mapigil ang aking mga luha. Nawala ang aking sensibilidad."
    hide florante
    t "Dalawang buwan dinala ni Florante ang sakit, hanggang dumating ang pangalawang liham mula sa kaniyang ama. Pinapauwi na muli siya sa Albanya."

    scene athens 3 with fade
    t "Sa kaniyang paghanda sa pag-alis ng palihim, pinalalahanan siya ng guro na  mag-ingat kay Adolfo. Siya’y lalong naghanda sa araw ng kanilang pagsalungat."

    t "Sabi ng kaniyang guro, maaring iyon na ang simula ng pinaka matinding pagsubok sa buhay ni Florante. "

    t "Ihinatid siya ni Menandro sa kaniyang pag-uwi. Naging malungkot ang kanilang pagpapaalam. Sa daungan pumalaot ang kanilang sasakyan papunta ng Atenas."

    scene albania 1 with fade

    t "Mabilis ang byahe at agad silang nagpunta sa kanilang kinta, kung saan nakilala at nag-mano si Menandro kay Duke Briseo."

    t "Pumalapot muli ang matinding kalungkutan ni Florante ng maisip ang pumanaw na ina."

    show florante speaking at left
    florante "Ay, ama!"

    duke_briseo "Ay, anak!"
    hide florante

    t "Dumating ang ambasador ng Krotona habang mahigpit na nagyayakapan ang mag-ama. Dala nito ay isang liham para kay Duke Briseo."

    t "Nakasulat sa liham na nanganganib ang Krotona at humihiling ng tulong dahil nakapaligid ang mga tauhan ni Heneral Osmalik na taga Persiya."

    show florante speaking at left
    florante "Ayon sa mga balita, pangalawa si Heneral Osmalik na tanyag at sikat ang Aladin. Kinatatakutan ng marami…"

    florante "At hinahangaan ko."
    show florante at left
    show aladin flip at right
    menu:
        florante "At hinahangaan ko."

        "Napangiti si Aladin":
            show aladin speaking flip at right
            aladin "Bihirang tama ang laman ng mga balita ngayon. Minsan kulang, minsan nadagdagan."
        "Napahanga si Aladin":
            show aladin speaking flip at right
            aladin "Bihirang tama ang laman ng mga balita ngayon. Minsan kulang, minsan nadagdagan."
        "Natuwa si Aladin":
            show aladin speaking flip at right
            aladin "Bihirang tama ang laman ng mga balita ngayon. Minsan kulang, minsan nadagdagan."

    aladin "Ang katapangan ay lumalaki sa isip ng isang duwag na kalaban. Habang nananalo ang isang gerero, lalong lumalakas ang mga kwento tungkol sa kanila kaya lalo silang kinatatakutan at iniiwasan."

    aladin "At kung maging sikat ako dahil sa katapangan, tandaan mo ring may mga pagkakataong muntik na akong maputulan ng hinga. Hindi magtatagal, mababalitaan mo ring pantay lang tayo sa kamalasan at sakit."
    show aladin flip at right
    show florante speaking at left
    florante "Sana hindi mangyari sayo ang aking kamalasan. Ayaw kong may makaranas nito ng sinuman. Kahit kalaban, ayaw ko silang magdusa."
    hide aladin
    hide florante

    t "Nagpatuloy ang kanilang usapan."

    scene albania_int 1 with fade

    t "Nang malaman ni Duke Briseo ang banta sa Krotona, agad niyang sinama si Florante kay Haring Linceo na nakadamit ng pandigma."

    t "Sinalubong ng Hari ang dalawa ng paakyat ng palasyo. Niyakap niya si Duke Briseo at kinamayan si Florante."

    haring_linceo "Ang binatang ito, kamukha niya ang gerorong magliligtas sa kaharian mula sa aking panaginip. Sino siya?"

    duke_briseo "Siya ang aking anak. Florante."

    t "Namangha si Haring Linceo at agad na ginawang Heneral ng hukbo na magtatanggol sa Krotona."

    haring_linceo "Patunayan mo ang iyong katapangan, kung ikaw nga ang gerero sa aking panaginip na magpapakita ng aking kapurihan at kapangyarihan."

    haring_linceo "Ang hari ng Krotono ay iyong ninuno, Florante. Ang dugong bughaw ay dumadaloy sa iyo. Kailangan makamit ang dangal at bunyi sa digmaan."

    t "Labag man sa kaniyang kalooban, pumayag si Duke Briseo sa kaniyang kahilingan. Sa murang edad, at sa kakulangan sa kasanayang pumatay, ipapadala niya si Florante sa digmaan."

    t "Walang nagawa si Florante."

    show florante speaking at left
    florante "Haring poo't"
    hide florante
    t "Dumapa si Florante sa paanan ng hari at ito’y hinalikan, ngunit siya’y pinatayo at muling niyakap. Nakipagkwentuhan si Florante tungkol sa naging buhay niya sa Atenas ng may mapansin siyang dalaga."

    menu:

        "Nakaramdam si Florante ng matinding kasiyahan":
            t "Para bang siya'y nasa langit na."
        "Sobra siyang namangha sa kagandahan ng dalaga":
            t "Para bang siya'y nasa langit na."
        "Nakuha ng dalaga ang lahat ng atensyon ni Florante":
            t "Para bang siya'y nasa langit na."

    show florante speaking at left

    scene flat rock with fade
    florante "Ang dalaga ay si Laura, anak ni Haring Linceo. Ang taong nagbago ng aking buhay. "

    florante "Hindi magtataksil si Laura. Ang kagandahang taglay niya ay hindi marunong magtaksil."

    florante "Kapag ika’y nasa dagat at natukso ng pagtataksil, ano ang gagawin mo kapag ang iyong dangal ay nanaig sa pagkawalan ng kagandahan?"

    florante "Hindi kaya ng karangalan ang gumawa ng masama."

    florante "Nang makita ko si Laura, sumiklab ang aking puso. Pati ang parte ng puso kong nakalaan sa aking ina, nabuhay rin."

    hide florante

    t "Naiyak muli si Florante nang maalala ang ina."

    show florante speaking at left
    florante "Ngunit, baka hindi karapat-dapat saakin ang isang kagandahang katulad ni Laura."
    hide florante

    t "Hindi na nakapag-isip ng tama si Florante. Para bang nagloloko ang kaniyang puso dahil nadama na niya ang liyab sa pag-ibig."

    t "Nagpatuloy ang usapan ng dalawa tungkol sa pagbabalik-tanaw sa buhay ni Florante."

    t "Naglaan ng tatlong araw ang hari sa pagsasalo-salo. Sa loob ng tatlong araw na iyon, hindi man lang napansin si Florante ni Laura. Hindi matumbasan ang sakit ng kaniyang nadarama."

    scene albania_int 2 with fade

    t "Sa kaswertehan, nagkaroon ng sandaling pagkakataon si Florante na makasama si Laura. Dito, inamin ni Florante ang pag-ibig."

    menu:
        t "Sa kaswertehan, nagkaroon ng sandaling pagkakataon si Florante na makasama si Laura. Dito, inamin ni Florante ang pag-ibig."

        "Aking sina, Ika'y tunay na iniibig.":
            show florante speaking at left
            florante "Aking sinta, ako’y man hindi gaanong napapansin, ngunit sa oras na ika’y nakita, nabuhay ang aking puso. Ika’y tunay na iniibig."
        "Mahal kita, Laura.":
            show florante speaking at left
            florante "Laura, ako’y sana iyong pakinggan sa aking sasabihin. Tunay kitang mahal."
        "Napukaw ako ng iyong ganda.":
            show florante speaking at left
            florante "Sa gandang ikaw lamang ang may taglay, ako’y napukaw. Hindi mo man ako napapansin, ngunit nagbigay buhay ka sa akin."
    hide florante
    t "Nanatiling tahimik si Laura. Ang puso’y niyang parang bibigay. Isang patak ng luha ang tumulo sa kaniyang mata. May sariling interpretasyon ito sa isip ni Florante."

    $ persistent.ch06 = True
    return

label ch07:

    scene black with dissolve 
    show text "{size=50}Kabanata 7{/size}" at truecenter with fade
    $ renpy.pause(3)
    show text "{size=25}Pagsalakay ng Krotona{/size}" at truecenter with fade
    $ renpy.pause(2)    
    hide text with dissolve

    scene albania 2 with fade

    t "Dumating ang araw ng pag-alis ni Florante, dala ang sakit sa kanyang kalooban. Inaalala na lamang niya ang pag-panaw ng kaniyang ina bilang kosuelo."

    t "Sa isip ni Florante, “Mayroon pa bang mas hihigit sa sakit ng pagkawalay sa minamahal?”"

    t "Nag-alay si Florante ng isang mabangong insenso sa altar ni Kupido, habang hinihiling na sana madinig ang kaniyang pangungulila kay Laura."

    show florante speaking at left
    florante "Kung hindi pumatak ang luha ni Laura, namatay na sana ako bago ko maramdaman ang matinding sakit, hanggang sa umabot ako sa giyera."
    hide florante

    scene croton_ext 1 with fade
    t "Mukhang bibigay na ang mga pader nang dumating si Florante sa kaharian ng Krotona. Inatake niya ang mga tauhang nakapaligid sa siyudad."

    t "Naging madugo ang labanan at halos napagod ang mga dyos ng kamatayan sa pagkuha sa mga lumipas."

    scene croton_ext 2 with fade

    t "Nakita ni Heneral Osmalik kung paano pinatay ni Florante ang pitong miyembro ng mga tropa ng Moro. Napatay naman ni Heneral Osmalik ang mga katropa ni Florante sa kaliwa’t kanan at nagkaroon ng hamunan sa kanilang pagitan."

    heneral_osmalik "Halika..."

    menu:
        heneral_osmalik "Halika..."

        "At ika'y aking tatalunin":
            t "Limang oras ang tinagal ng kanilang paglalaban. Napagod ang heneral at tuluyang napatay ni Florante."
        "Dudurigin kita":
            t "Limang oras ang tinagal ng kanilang paglalaban. Napagod ang heneral at tuluyang napatay ni Florante."
        "Ika'y aking papatayin":
            t "Limang oras ang tinagal ng kanilang paglalaban. Napagod ang heneral at tuluyang napatay ni Florante."

    t "Natakot ang mga natirang Moro sa lakas ng espada ni Menander at nakuha nila Florante ang mga kampo. Wagi ang bumati sa kanila."

    t "Naglaho sa takot ang mga natirang kalaban ni Florante. Naseguridad ang panalo. Naglaho narin ang mga takot sa kamatayan ang binuksan ang pinto ng kaharian."

    t "Marami ang nagpugay sa pagkapanalo ni Florante. Nilapitan siya para lang mahalikan ang kaniyang damit."

    t "“Mabuhay!” at “Salamat sa tanggol namin!” ang naging sigaw ng mga tao. Nadagdagan ang kanilang tuwa nang mabalitaan nilang isang apo ng Hari si Florante. Napaiyak sa tuwa ang hari."

    t "Tumungo sila sa palasyo upang magpahinga. Tatlong araw ang lumipas ng halos hindi matulog ang siyudad."

    scene croton_int 1 with fade

    t "Sa kabila ng kanilang umaapaw na kasiyahan, muling naramdaman ni Florante ang sakit mula sa alaala ng pumanaw na ina."

    t "Napagtanto ni Florante ni kailanma’y hindi mabubuo ang kaligayahan. Laging kasunod ang kalungkutan sa kaunting ligaya. Makapitong beses man o hanggang matapos."

    $ persistent.ch07 = True
    return

label ch08:

    scene black with dissolve 
    show text "{size=50}Kabanata 8{/size}" at truecenter with fade
    $ renpy.pause(3)
    show text "{size=25}Gasuklay na Buwan sa Taas ng Albania{/size}" at truecenter with fade
    $ renpy.pause(2)    
    hide text with dissolve

    scene croton_int 1 with fade

    t "Lumipas ang limang buwan ang pananatili ni Florante sa Krotona.  Higit ang kagustuhan niyang bumalik sa Albanya. Nais niyang makita muli si Laura."

    scene croton_ext 1 with fade

    t "Naglakad sila papuntang Albanya. Sa pagkainip ni Florante ay naisip niya na sana’y siya’y makalipad ng parang ibon. Natanaw nila ang mga moog, at tila bumilis ang kutog ng kaniyang dibdib."

    scene albania 2 with fade

    t "Isang bandera ng Krisenteng Buwan ng mga Kristiyano ang kanilang nakita imbes ang bandila ng Persya. Nasakon na ni Aladin ang siyudad."

    t "Napahinto si Florante at ang kaniyang mga hukbo sa paa ng isang bundok nang makita nila ang mga moro na nagma-martsa."

    t "Kasama nila’y isang babaeng nakagapos ang mga kamay at tila siya’y dadalhin sa lugar kung saan siya’y pupugutan. Natakot si Florante nang maisip ang kaniyang sintang si Laura."

    t "Nangibabaw ang galit sa kalooban ni Florante at kaniyang sinugod ang mga morong malapit sa babae. Tumakbo palayo ang mga moro."

    t "Inalis ni Florante ang takip mula sa mukha ng babae. Tumindig sa kaniya ay ang pamilyar na mukha ni Laura."
    show laura at left
    menu:
        t "Inalis ni Florante ang takip mula sa mukha ng babae. Tumindig sa kaniya ay ang pamilyar na mukha ni Laura."

        "Lalong magalit":
            show laura speaking at left
            laura "Ako’y nahatulan ng kamatayan dahil isang asal-hayop na Emir ng siyudad ang aking nasampal dahil hindi ako pumayag na mahalay niya."
        "Mapalitan ng sakit ang nadadama":
            show laura speaking at left
            laura "Ako’y nahatulan ng kamatayan dahil isang asal-hayop na Emir ng siyudad ang aking nasampal dahil hindi ako pumayag na mahalay niya."
    hide laura

    t "Agad agarang inalis ni Florante ang mga gapos ni Laura nang dahan-dahan upang hindi mahawakan ang kaniyang mga balat."
    
    t "Nakita ni Florante ang titig ni Laura at hinigop ng hilom ang kaniyang naghihirap na puso."

    show laura speaking at left
    laura "Sintang Florante..."

    show florante speaking flip at right
    florante "Anong nangyare, sintang Laura?"

    laura "Binihag ang aking amang si Haring Linceo, pati rin ang iyong amang si Duke Briseo."

    scene albania_int 1 with fade
    t "Agarang ipinag-utos ni Florante sa kaniyang mga hukbo ng bawaiin ang mga nabihag na ama at huwag sila titigil hanggang sa ito’y hindi nangyayari."

    t "Pinasok nila ang kaharian ng Albanya at unang tinungo ni Florante ay ang bilangguan kung saan naroroon ang hari at ang duke. Pinalaya niya sila at sa pagiging maginoo ni Florante, kahit si Adolfo ay kaniyang pinalaya din."

    t "Naging matagumpay at nagsaya ang lahat. Ngunit inggit ang namuo sa kalooban ni Adolfo sa bawat papuri na natatanggap ni Florante."

    t "Tinawag na Tagapagtanggol ng Siyudad si Florante at lalong nagdiwang ang hari sa palasyo na lalo pang ikina-inggit ni Adolfo."

    t "Sa matinding kagustuhan na mapunta sa kaniya ang korona ng kaharian ng Albanya, binalak niyang pakasalan si Laura, ngunit napagtanto niyang may pagmamahalang nabubuo sa pagitan ni Florante at Laura. Lalong nangibabaw ang inggit ni Adolfo."

    menu:

        "Nagsimula na ang kasamaan ni Adolfo":
            t "Gagawin niya ang lahat, kahit mapatay pa si Florante."
        "Nagbalak na siya ng madilim na laban kay Florante":
            t "Gagawin niya ang lahat, kahit mapatay pa si Florante."

    $ persistent.ch08 = True
    return

label ch09:

    scene black with dissolve 
    show text "{size=50}Kabanata 9{/size}" at truecenter with fade
    $ renpy.pause(3)
    show text "{size=25}Tumambang{/size}" at truecenter with fade
    $ renpy.pause(2)    
    hide text with dissolve

    scene albania 2 with fade

    t "Hindi nagtagal ang pagdidiwang sa kalayaan. Isang hukbo nanaman ang sumalakay sa Turkiya."

    t "Nalungkot ang marami. Tila ang takot ang pag-aalala ni Laura kay Florante na baka siya’y mapatay sa mga giyera."

    t "Hinirang ng hari na maging heneral si Florante laban sa mga Moro na siyang nagpatibay sa loob ng taumbayan. Hindi ito kinatuwa ni Adolfo."

    t "Hinayaan ng langit na magtagumpay si Florante laban kay Miramolin, isang morong kinakatukutan nang matagal ng Albanya."

    scene mountains with fade
    show florante speaking at left
    florante "Dumating ang maraming digmaan, at sunod-sunod ang aking tagumpay. Nakuha ko ang respeto at galang ng mga labing-pitong hari."

    scene aetolia with fade
    show florante speaking at left
    florante " Isang araw mula sa aking pagdidigimaan sa Etolia, nakatanggap ako ng liham mula kay Haring Linceo. Laman nito ang kautusang bumalik sa Albanya."

    florante "Ipinagbahala ko muna kay Menandro ang pagmamahala sa mga hukbo sa Etolia at dali-dali akong umalis."

    scene forest 2 night
    show florante speaking at left
    florante "Gitna ng kadiliman nung ako’y pumasok sa Albanya. Payapa ang aking loob, wala akong naiisip na masama."

    scene albania 2 night
    t "Dumating si Florante sa Albanya, at sa kaniyang gulat, siya’y pinaligiran ng tatlumpu’t libong sundalo."

    t "Hindi nagkaroon ng pagkakataong mabunot ang espada at manlaban si Florante nang agad siyang tinali at tinapon sa bilangguan."

    t "Lalong nasurpresa at nalungkot si Florante nang kaniyang malaman ang kamatayan ni Haring Linceo at Duke Briseo sa kamay ni Konde Aldolfo."

    t "Nagawa ni Adolfo ang madugong kataksilan dahil sa mga matinding kagustuhan."

    menu:
        t "Nagawa ni Adolfo ang madugong kataksilan dahil sa mga matinding kagustuhan."

        "Kasikatan":
            t "Uhaw na uhaw si Adolfo sa kasikatan, kahit noong pagkabata pa."
        "Kamatayan":
            t "Nais niyang mamatay si Florante, ang tao kinuha sa kaniya ang lahat."
        "Kayamanan":
            t "Gusto niyang mapunta sa kaniya ang kaharian ng Albanya. Ganun na nga ang kaniyang katakawan sa kayamanan."

    t "Napakalungkot at napakasama ng nangyari sa Albanya."

    show florante speaking at left
    florante "Lalo pang naging kaawa-awa ang Albanya sa ilalim ng isang lider na bobo at masama. Ang haring mahilig sa yaman ay parang parusa ng Langit sa bayan."

    florante "Tunay nga akong malas at nagpaloko sa pag-ibig."
    hide florante

    t "Nabalitaan ni Florante na nangakong magpapakasal  si Laura sa taksil at mapagkunwaring Konde Adolfo."

    t "Lalong sumama ang loob ni Florante. Naisip niya, “Nais ko nang mamatay, magbalik sa pinakasimula, kung saan ako’y hindi pa nabubuhay.”"

    scene flat rock with fade

    show florante speaking at left
    show aladin flip at right
    florante "Sa aking pagkabilanggo ng labingwalong araw, nainip ako sa paghintay kay kamatayan. Kinagabihan, kinuha ako mula sa bilangguan at dinala sa gubat. Doon, ako’y tinali sa isang puno."
    hide florante

    scene aladins makeshift home with fade
    show aladin speaking at left
    aladin "Ako’y nagmula sa Persiya at ako’y anak ni Sultan Ali-Adib."

    t "Sinubukan ni Aladin na ipahayag ang tungkol sa ama, at ang mahal niyang si Flerida, ngunit pinangunahan siya ng kaniyang mga luha. “Ay Ama ko! Bakit..?”, “Ay Fleridang sinta!”"

    aladin "Parehas tayong naghintay ng katapusan sa ating malas na buhay dito sa gubat."
    hide aladin

    t "Hindi na muli nagbahagi si Aladin at limang buwan silang namalagi sa loob ng kagubatan."

    t "Sakanilang pag-iikot, nagsimula na muling magkwento si Aladin."

    $ persistent.ch09= True
    return

label ch10:

    scene black with dissolve 
    show text "{size=50}Kabanata 10{/size}" at truecenter with fade
    $ renpy.pause(3)
    show text "{size=25}Pinalayas na Prinsipe{/size}" at truecenter with fade
    $ renpy.pause(2)    
    hide text with dissolve

    scene aladins makeshift home with fade
    show aladin speaking at left
    aladin "Marami na akong naranasang giyera, ngunit ang aking lubos na pagkahirap ay nagmula kay Flerida."

    aladin "Ang prinsesang si Flerida ay..."

    menu: 
        aladin "Ang prinsesang si Flerida ay..."

        "Diyosa":
            aladin "Parang si Diana, dyosa ng mga mangangaso sa gitna ng mga diwata."
        "Magandang Berhen":
            aladin "Isang houri, o isang magandang berhen na kasama sa paraiso ng mga Muslim."

    aladin "Ako nga’y pinalad at naging matagumpay ang aking panliligaw. Kami’y nagmahalan."

    aladin "Ngunit, pumasok sa eksena ang aking ama. Doon na nga nagsimula ang aking matinding paghihirap."

    scene persia 1 with fade
    aladin "Ako’y naging matagumpay sa labanan sa Albanya, ngunit nang ako’y umuwi sa Persiya, para ba akong bilanggo."

    aladin "Ayon sa sabi-sabi, iniwan ko ang aking mga tropa ng walang pahintulot sa aking ama. At dahil nabawi mo ang Albanya, dapat akong pugutan."

    aladin "Isang gabi bago ang araw ng aking kamatayan, dumating ang isang heneral sa aking kulungan. Dala niya ang isang balitang mas masaklap sa kamatayan."

    aladin "Hindi na nga ako mapupugutan, ngunit ako’y nangangailangang umalis bago pa ako masikatan ng araw."

    aladin "Ngunit mas gugustuhin kong maputulan ng ulo, kaysa sa malaman na ang aking pinakamamahal ay nasa piling na ng sariling kong ama."

    scene forest 2 with fade
    aladin "May anim na taon akong nagpalaboy-laboy--"
    hide aladin

    t "Napatigil sa pagkuwento si Aladin. May narinig silang mga boses sa gubat."

    $ persistent.ch10 = True
    return

label ch11:

    scene black with dissolve
    show text "{size=50}Arko 3: Sa Paglubog at Paglitaw ng Araw{/size}" at truecenter with fade
    $ renpy.pause(3.5)    
    show text "{size=50}Kabanata 11{/size}" at truecenter with fade
    $ renpy.pause(3)
    show text "{size=25}Sigaw ng Isang Dalaga{/size}" at truecenter with fade
    $ renpy.pause(2)    
    hide text with dissolve

    scene forest 1 with fade
    show laura speaking at left
    laura "Pakawalan mo ako!"

    menu:
        laura "Pakawalan mo ako!"

        "Sumigaw lang":
            count_adolfo "Tumahimik ka!"
        "Kagatin ang kanyang braso":
            count_adolfo "Masakit! Ikaw na hangal!"
        "Sipain siya":
            count_adolfo "Hangal na dalaga!"

    hide laura

    t "Sumisigaw si Laura at pilit siyang nahihirapang tumakas sa mahigpit na pagkakahawak sa kanya ni Adolfo."
    
    show laura speaking at left
    laura "Baboy ka! Tanggapin mo nalang ang iyong pagkakatalo! Mahahanap ka rin ni Menadro, at ikaw ay kanyang papatayin!"
    hide laura

    t "Ang mga braso ni Adolfo ay nakapiit kay Laura. Nakababalisang malapit si Adolfo kay Laura, at nararamdaman nito ang paghinga ni Adolfo sa kanyang mga tainga. “Siya ay nakadidiri,” tugon ni Laura sa kanyang isipan."

    count_adolfo "ARGH!"

    t "Ni pulgada, ay hindi makagalaw si Adolfo at ang pagkakapiit nito kay Laura ay lumuwag. Si Laura ay lumingon sa takot."

    t "Ang dibdib ni Adolfo ay dumudugo. May palaso na tumagos sa dibdib ni Adolfo. Siya ay natumba at nakaratay sa lupa."

    t "Si Laura ay nanginginig at dahan-dahang lumakad palayo,  ngunit may nabangga siyang tao. Kaya’t bumagsak ang puso ni Laura sa takot. At may kamay ng hindi kilalang tao ang nakahandusay sa balikat ni Laura."

    unknown "Ayos ka lang ba, binibini?"

    show laura speaking at left
    laura "Sino ka?"
    $ persistent.ch11 = True
    return

label ch12:

    scene black with dissolve 
    show text "{size=50}Kabanata 12{/size}" at truecenter with fade
    $ renpy.pause(3)
    show text "{size=25}Ako si Flerida{/size}" at truecenter with fade
    $ renpy.pause(2)    
    hide text with dissolve

    scene persia 2 with fade

    flerida "At nakatakas ako sa palasyo kung saan ako ay kinulong ni Sultan Ali-Adab."

    flerida "Siya ay may anak na lalaki. Isang sutil na prinsipe na hindi tumatanggap ng sagot na “hindi”. Bawat pagsulong niya ay aking tinatanggihan ngunit.. napaibig na ako sa kanya."

    flerida "Pinag-uusapan namin ang tungkol sa lahat. At palagi kong nararamdaman na nagkakaintindihan kami sa isa’t isa."

    flerida "Siya ay umalis upang makipagdigmaan kasama si Heneral Osmalik. At nang siya ay bumalik..."

    scene persia_int 2 with fade

    sultan_ali_adab "TRAYDOR!"

    flerida "Hindi makatarungan ang pagkakakulong sa kanya, sa kadahilanang siya ay nagtaksil. Araw-araw, hinihingi ng Sultan ang aking kamay sa pakikipagkasal at araw-araw ko rin itong tinatanggihan … hanggang sa narinig ko ang balak  niyang ipapatay ang kanyang sariling anak. Nagmakaawa akong huwag niya itong gawin… Kapalit ng kalayaan ng prinsipe, ako ay magpapakasal sa kanya. At siya ay sumang-ayon."

    scene persia_int 1 night

    flerida "Isang gabi... Pinaplano kong makita muli si Aladin..."

    heneral "Pinalalayas ka, ayon sa kautusan ng Sulatan. At huwag ka nang magpapakita ritong muli."

    flerida "May Heneral sa tabi ng pintuan ng kulungan, hinatid siya nito palabas. Ipinangako ko sa aking sarili na siya ay aking hahanapin."

    scene persia 1 night with fade

    flerida "Sa isa pang gabi kung saan natitiyak kong natutulog na ang lahat, palihim akong umalis. Nagpanggap ako bilang isang sundalo at gamit ang isang pana. Tumakas ako, palayo."

    scene forest 1 with fade

    flerida "At narito na ako ngayon… Umaasang makikita ko siya muli."

    show laura speaking at left
    laura "Napakagiting ang iyong kalooban."
    hide laura

    t "Ngumiti si Laura kay Flerida sa gubat. At si Flerida'y namula."

    t "Ang dalawa’y nakarinig ng kaluskos sa kanilang likod. Inihanda ni Flerida ang kanyang pana habang si Laura ay nakatayo sa kangyang tabi."


    $ persistent.ch12 = True
    return

label ch13:

    scene black with dissolve 
    show text "{size=50}Kabanata 13{/size}" at truecenter with fade
    $ renpy.pause(3)
    show text "{size=25}Muling Pagsasama{/size}" at truecenter with fade
    $ renpy.pause(2)    
    hide text with dissolve

    scene forest 1 with fade
    t "Lumitaw sa harap nila sila Aladin at Florante."

    t "Nagulat ang dalawang babae ngunit mas labis ang kanilang kasiyahan sa kanilang nakita."

    t "Tumakbo si Laura patungo kay Florante at ito’y kangyang niyakap."

    show laura speaking at left
    laura "Buhay ka! Salamat sa Diyos!"
    hide laura
    t "Napaluha ang mga mata ni Laura."

    t "Sa kabilang banda, lumapit si Fleridad kay Aladin. Ang pakiramdam ni Aladin ay nanambik sa mga kamay ni Fleridad na humahawak sa kanyang mga pisngi. At ang dalawa’y labis na lumuha habang sila ay magkayakap sa isa’t isa."

    menandro "FLORANTE! LAURA!"

    t "Lumitaw sila Menandro at ang kanyang mga kasamahan. Siya ay ngumiti at niyakap din si Florante."

    scene albania 1 with fade

    t "Isinama ni Menandro ang apat sa Albania upang magdiwang."

    scene persia 1 with fade

    t "Si Sultan Ali-Adab ay namatay sa labis na kalungkutan sa paglaho ni Fleridad sa palasyo."

    scene mountains with fade 

    t "Isang bagong araw ang muling sumalubong, at ang kapayapaan ang nanalo at nangasiwa sa dalawang kaharian."

    $ persistent.ch13 = True
    return