from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
time.sleep(3)

input_text = '''Jinsei no naka de, okurimono wa shibashiba fukai omoide ya kanjō o伴ai, watashi ni totte tokubetsu na okurimono wa koi bito kara moratta pinku no kuma no nuigurumi desu. Watashi wa sore ni "Rupi" to nadete ite, Rupi o miru tabi ni koi bito to no utsukushii shunkan o omoidashimasu.

Ano hi, nagai benkyō o oete kitai to, tēburu no ue ni teinei ni tsutsuma reta hako ga oite arimashita. Pinku no hāpō-shi to kawaī ribbon ni kokoro ga odorokimashita. Hako o akeru to, kawaī kuma no nuigurumi ga araware, watashi wa ureshisa o osaekiremasen deshita. Rupi no ōkī me to akarui egao wa, watashi ni pojitibu na enerugī o ataete kuremashita.

Koi bito wa, Rupi ga kodoku ya kanashimi o kanjiru toki no aibō ni naru to tsutaete kuremashita. Kare wa, isogashii seikatsu ya kyori ga atte mo, itsumo watashi no soba ni iru koto o wasurenaide hoshii to itte kuremashita. Rupi wa tada no omocha de wa naku, kare ga watashi ni yosoru aijō to haikan no shōchō desu.

Maiban kitai to, watashi wa Rupi o daki shimeru. Nuigurumi no yawarakai ke nawa wa, watashi ni anshin kan o ataete kuremasu. Sutoresu ya fuan o kanjiru toki, watashi wa koi bito to no suteki na omoide o omoidashimasu. Romantikku na dēto kara futari dake no amai shunkan made, Rupi wa watashi no seikatsu ni kakasenu sonzai to nari, watashi no kimochi o takusasareru basho desu.

Toku ni tanjōbi ya kinenbi nado no tokubetsu na toki ni wa, Rupi wa sarani tokubetsu na imi o mochimasu. Watashi wa Rupi ni ribbon ya banā o kazari, arui wa messeeji o kaita kami o burasagete shimasu. Kono kōdō wa, koi bito e no aijō o shimesu dake de naku, Rupi o yori ikigai to sasemasu. Koi bito mo Rupi ga taisetsu ni sarete iru no o miru no ga suki de, watashi no hokori o sarani fukameru koto ni narimasu.

Okurimono wa busshitsuteki na kachi dake de naku, hakarishirenai seishinteki na kachi mo motteimasu. Rupi wa, watashitachi ga tomo ni kizuita aijō ya omoiyari, shiawase na shunkan o omoidashasete kuremasu. Rupi o daki shimeru tabi ni, koi bito no ai o atatakai daki to shite kanjite, jinsei no arayuru shiren o norikoeru chikara o moraimasu.

Rupi wa tada no nuigurumi de wa naku, watashi to koi bito ga kyōyū suru yume ya kibō, ai no shōchō desu. Sore wa, ai ga ōkina koto dake de naku, hibī no chīsana kōdō no naka ni sonzai suru koto o oshiete kuremasu.

Saigo ni, watashi wa Rupi ga kore kara mo watashi no seikatsu no ichibu de ari, yorokobi ya utsukushii omoide o motarashi, watashi to tomo ni samazama na ukishizuku o norikoete kureru koto o negatteimasu. Koi bito kara no okurimono wa watashi no kokoro ni fukai kizamare, watashitachi no ai no tabiji ni oite jūyō na ichibu to natteimasu. Rupi wa tan naru mono de wa naku, watashitachi ga tomo ni kizuita tsuyoku utsukushii kanjō o musubitsukeru kakehashi desu.'''.lower()
for char in input_text:
    
    keyboard.press(f'{char}')
    keyboard.release(f'{char}')
    time.sleep(0.07) 