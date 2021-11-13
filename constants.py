TOKEN = '80624ac5f0a5b0eb5a8272322ec75a54ff9b65051350bb288a81b72af5509e31f2fb940b3917606f794b7'
INFO = open('info.txt', mode='r', encoding='utf-8').readlines()
WORDS_ORTHOEPY = {{'августовский': {'correct': 'а́вгустовский', 'variants': ['а́вгустовский', 'августо́вский']},
                   'агент': {'correct': 'аге́нт', 'variants': ['а́гент', 'аге́нт']},
                   'агентство': {'correct': 'аге́нтство', 'variants': ['а́гентство', 'аге́нтство']},
                   'агония': {'correct': 'аго́ния', 'variants': ['аго́ния', 'агони́я']},
                   'алкоголь': {'correct': 'алкого́ль', 'variants': ['алко́голь', 'алкого́ль']},
                   'алфавит': {'correct': 'алфави́т', 'variants': ['а́лфавит', 'алфави́т']},
                   'анатом': {'correct': 'ана́том', 'variants': ['анато́м', 'ана́том']},
                   'антитеза': {'correct': 'антите́за', 'variants': ['анти́теза', 'антите́за']},
                   'апостроф': {'correct': 'апостро́ф', 'variants': ['апо́строф', 'апостро́ф']},
                   'арбуз': {'correct': 'арбу́з', 'variants': ['а́рбуз', 'арбу́з']},
                   'аргумент': {'correct': 'аргуме́нт', 'variants': ['аргу́мент', 'аргуме́нт']},
                   'арест': {'correct': 'аре́ст', 'variants': ['а́рест', 'аре́ст']},
                   'аристократия': {'correct': 'аристокра́тия', 'variants': ['аристокра́тия', 'аристократи́я']},
                   'асимметрия': {'correct': 'асимметри́я', 'variants': ['асимме́трия', 'асимметри́я']},
                   'астроном': {'correct': 'астроно́м', 'variants': ['астроно́м', 'астро́ном']},
                   'атлас (география)': {'correct': 'а́тлас', 'variants': ['а́тлас', 'атла́с']},
                   'атлас (ткань)': {'correct': 'атла́с', 'variants': ['а́тлас', 'атла́с']},
                   'афера': {'correct': 'афе́ра', 'variants': ['афе́ра', 'афёра']},
                   'аэропорты': {'correct': 'аэропо́рты', 'variants': ['аэропо́рты', 'аэропорты́']},
                   'баллотировать': {'correct': 'баллоти́ровать', 'variants': ['баллоти́ровать', 'баллотирова́ть']},
                   'балованный': {'correct': 'бало́ванный', 'variants': ['бало́ванный', 'ба́лованный']},
                   'баловать': {'correct': 'балова́ть', 'variants': ['балова́ть', 'ба́ловать']},
                   'баловник': {'correct': 'баловни́к', 'variants': ['баловни́к', 'ба́ловник']},
                   'балуясь': {'correct': 'балу́ясь', 'variants': ['балу́ясь', 'ба́луясь']},
                   'банты': {'correct': 'ба́нты', 'variants': ['ба́нты', 'банты́']},
                   'банта': {'correct': 'ба́нта', 'variants': ['ба́нта', 'банта́']},
                   'бармен': {'correct': 'ба́рмен', 'variants': ['ба́рмен', 'барме́н']},
                   'безудержный': {'correct': 'безу́держный', 'variants': ['безу́держный', 'безуде́ржный']},
                   'береста': {'correct': ['береста́', 'берёста'], 'variants': ['береста́', 'берёста']},
                   'благовест': {'correct': 'бла́говест', 'variants': ['бла́говест', 'благове́ст']},
                   'благоволить': {'correct': 'благоволи́ть', 'variants': ['благоволи́ть', 'благово́лить']},
                   'борода': {'correct': 'борода́', 'variants': ['борода́', 'бо́рода']},
                   'бороду': {'correct': 'бо́роду', 'variants': ['бо́роду', 'бороду́']},
                   'бочковый': {'correct': 'бо́чковый', 'variants': ['бо́чковый', 'бочко́вый']},
                   'брала': {'correct': 'брала́', 'variants': ['брала́', 'бра́ла']},
                   'браться': {'correct': 'бра́ться', 'variants': ['бра́ться', 'браться́']},
                   'бралась': {'correct': 'брала́сь', 'variants': ['брала́сь', 'бра́ла́сь']},
                   'бредовой': {'correct': 'бредово́й', 'variants': ['бредово́й', 'бредо́вой']},
                   'бредовый': {'correct': 'бредо́вый', 'variants': ['бредо́вый', 'бре́довый']},
                   'броня (запись на мероприятие)': {'correct': 'бро́ня', 'variants': ['бро́ня', 'броня́']},
                   'броня (защита)': {'correct': 'броня́', 'variants': ['броня́', 'бро́ня']},
                   'булочная': {'correct': 'бу́лочная', 'variants': ['бу́лочная', 'булочна́я']},
                   'буржуазия': {'correct': 'буржуази́я', 'variants': ['буржуази́я', 'буржуа́зия']},
                   'бутерброд': {'correct': 'бутербро́д', 'variants': ['бутербро́д', 'буте́рброд']},
                   'бухгалтер': {'correct': 'бухга́лтер', 'variants': ['бухга́лтер', 'бухгалте́р']},
                   'бухгалтеров': {'correct': 'бухга́лтеров', 'variants': ['бухга́лтеров', 'бухгалтеро́в']},
                   'валовой': {'correct': 'валово́й', 'variants': ['валово́й', 'ва́ловой']},
                   'варить': {'correct': 'вари́ть', 'variants': ['вари́ть', 'ва́рить']},
                   'варит': {'correct': 'ва́рит', 'variants': ['вари́т', 'ва́рит']},
                   'варишь': {'correct': 'ва́ришь', 'variants': ['ва́ришь', 'вари́шь']},
                   'варят': {'correct': 'ва́рят', 'variants': ['ва́рят', 'варя́т']},
                   'варящийся': {'correct': 'варя́щийся', 'variants': ['варя́щийся', 'ва́рящийся']},
                   'вахтер': {'correct': 'вахтёр', 'variants': ['вахтёр', 'ва́хтер']},
                   'верба': {'correct': 'ве́рба', 'variants': ['ве́рба', 'верба́']},
                   'верна': {'correct': 'верна́', 'variants': ['верна́', 'ве́рна']},
                   'вероисповедание': {'correct': 'вероиспове́дание', 'variants': ['вероиспове́дание', 'вероисповеда́ние']},
                   'взбешённый': {'correct': 'взбешённый', 'variants': ['взбешённый', 'взбе́шенный']},
                   'взяла': {'correct': 'взяла́', 'variants': ['взя́ла', 'взяла́']},
                   'взялась': {'correct': 'взяла́сь', 'variants': ['взяла́сь', 'взя́лась']},
                   'взяться': {'correct': 'взя́ться', 'variants': ['взя́ться', 'взяться́']},
                   'включенный': {'correct': 'включённый', 'variants': ['включённый', 'вклю́ченный']},
                   'включен': {'correct': 'включён', 'variants': ['включён', 'вклю́чен']},
                   'включишь': {'correct': 'включи́шь', 'variants': ['включи́шь', 'вклю́чишь']},
                   'включит': {'correct': 'включи́т', 'variants': ['включи́т', 'вклю́чит']},
                   'включим': {'correct': 'включи́м', 'variants': ['включи́м', 'вклю́чим']},
                   'влиться': {'correct': 'вли́ться', 'variants': ['вли́ться', 'влиться́']},
                   'влилась': {'correct': 'влила́сь', 'variants': ['влила́сь', 'вли́лась']},
                   'вовремя': {'correct': 'во́время', 'variants': ['во́время', 'вовре́мя']},
                   'водопровод': {'correct': 'водопрово́д', 'variants': ['водопрово́д', 'водопро́вод']},
                   'волгодонский (г. Волгодонск)': {'correct': 'волгодо́нский', 'variants': ['волгодо́нский', 'волго́донский']},
                   'волка': {'correct': 'во́лка', 'variants': ['во́лка', 'волка́']},
                   'волки': {'correct': 'во́лки', 'variants': ['во́лки', 'волки́']},
                   'волков': {'correct': 'волко́в', 'variants': ['волко́в', 'во́лков']},
                   'вора': {'correct': 'во́ра', 'variants': ['во́ра', 'вора́']},
                   'воры': {'correct': 'во́ры', 'variants': ['во́ры', 'воры́']},
                   'воров': {'correct': 'воро́в', 'variants': ['воро́в', 'во́ров']},
                   'ворам': {'correct': 'вора́м', 'variants': ['вора́м', 'во́рам']},
                   '(о) ворах': {'correct': 'вора́х', 'variants': ['вора́х', 'во́рах']},
                   'ворвалась': {'correct': 'ворвала́сь', 'variants': ['ворвала́сь', 'ворва́лась']},
                   'воспринять': {'correct': 'восприня́ть', 'variants': ['восприня́ть', 'воспри́нять']},
                   'восприняла': {'correct': 'восприняла́', 'variants': ['восприняла́', 'воспри́няла']},
                   'воссоздала': {'correct': 'воссоздала́', 'variants': ['воссоздала́', 'воссо́здала']},
                   'вручить': {'correct': 'вручи́ть', 'variants': ['вручи́ть', 'вру́чить']},
                   'вручит': {'correct': 'вручи́т', 'variants': ['вручи́т', 'вру́чит']},
                   'газопровод': {'correct': 'газопрово́д', 'variants': ['газопрово́д', 'газопро́вод']},
                   'гастрономия': {'correct': 'гастроно́мия', 'variants': ['гастроно́мия', 'гастрономи́я']},
                   'гектар': {'correct': 'гекта́р', 'variants': ['гекта́р', 'ге́ктар']},
                   'генезис': {'correct': 'ге́незис', 'variants': ['ге́незис', 'гене́зис']},
                   'гладкошёрстный': {'correct': 'гладкошёрстный', 'variants': ['гладкошёрстный', 'гладкоше́рстный']},
                   'гнала': {'correct': 'гнала́', 'variants': ['гнала́', 'гна́ла']},
                   'гналась': {'correct': 'гнала́сь', 'variants': ['гна́лась', 'гнала́сь']},
                   'гравер': {'correct': 'гравёр', 'variants': ['гравёр', 'гра́вер']},
                   'гражданство': {'correct': 'гражда́нство', 'variants': ['гражда́нство', 'гра́жданство']},
                   'гренадер': {'correct': 'гренадёр', 'variants': ['гренадёр', 'грена́дер']},
                   'грушевый': {'correct': 'гру́шевый', 'variants': ['гру́шевый', 'груше́вый']},
                    а́ о́ у́ ы́ э́ я́ ё ю́ и́ е́
                   'давнишний': {'correct': 'давни́шний', 'variants': ['давни́шний', 'да́внишний']},
                   'девичий': {'correct': 'де́вичий', 'variants': ['де́вичий', 'деви́чий']},
                   'демократия': {'correct': 'демокра́тия', 'variants': ['демокра́тия', 'демократи́я']},
                   'деспот': {'correct': 'де́спот', 'variants': ['де́спот', 'деспо́т']},
                   'дефИс': {},
                   'диАгноз': {},
                   'диалОг': {},
                   'диспансЕр': {},
                   'добелА': {},
                   'добралА': {},
                   'добралАсь': {},
                   'добЫча': {},
                   'довезЁнный': {},
                   'дОверху': {},
                   'дОгмат': {},
                    договОр
                    договорЁнность
                    договОрный
                    дождАться - дождалАсь
                    дозвонИться - дозвонИтся, дозвонЯтся.
                    дозИровать
                    докумЕнт
                    донЕльзя
                    дОнизу
                    досУг
                    дОсуха
                    дочернА
                    драматургИя
                    дремОта
                    духовнИк

                    Е

                    еретИк

                    Ж

                    жалюзИ
                    ждАть - ждалА
                    жЁлоб
                    житиЕ
                    жИться - жилОсь

                    З

                    забронИровать (закрепить что-нибудь за кем-нибудь)
                    забронировАть (покрыть броней)
                    завИдно
                    заворожЁнный
                    зАговор (тайное соглашение)
                    зАгодя
                    зАгнутый
                    задОлго
                    заЁм
                    заИндеветь (и допуст. заиндевЕть)
                    закУпорить, закУпорив
                    закУпорка
                    занятОй (человек)
                    зАнятый (кем-нибудь или чем-нибудь) - занятА.
                    занЯть - зАнял, занялА, зАняло, зАняли
                    заперЕться - заперлАсь
                    зАпертый-запертА
                    заржавЕть и заржАветь
                    зАсветло
                    заселЁнный - заселенА
                    зАтемно
                    звонИть (звонИшь, звонИт, звонЯт)
                    зимОвщик
                    злОба
                    знАмение
                    знАхарство
                    знАхарка и допуст. знахАрка
                    знАчимость
                    знАчимый
                    зубчАтый

                    И

                    Игрище
                    иерОглиф
                    избалОванный
                    Издавна
                    изобретЕние
                    Изредка
                    Иконопись
                    Иксы
                    индустрИя (устар. индУстрия)
                    инструмент
                    инсУльт
                    информИровать
                    исключИть — исключИт
                    Искра
                    Исстари
                    исчЕрпать

                    К

                    каталОг
                    кАтарсис
                    катастрофа
                    каучУк
                    кАшлянуть
                    квартАл
                    кедрОвый
                    киломЕтр
                    кинематогрАфия
                    класть — клАла
                    клЕенный (прич.)
                    клеЁный (прил.)
                    клЕить
                    кожЕвенный
                    коклЮш
                    кОлледж
                    коллЕж
                    колОсс
                    кОмпас
                    кОнус, кОнусы
                    кормЯщий
                    корЫсть
                    крАны
                    крапИва
                    красИвее, красИвейший
                    крАсться — кралАсь
                    кремЕнь, кремнЯ кровоточАщий. кровоточИть
                    кУхонный

                    Л

                    лгать — лгалА
                    лЕктор, лЕкторов
                    лить — лилАсь
                    ловкА
                    ломОта
                    ломОть
                    лОскут (отходы, остатки)
                    лоскУт (кусочек ткани)
                    лососЁвый
                    лубОчный
                    лыжнЯ

                    М

                    мастерскИ и допуст. мАстерски
                    мастерствО
                    медикамЕнты
                    мЕльком
                    мЕстностей
                    металлургИя (и допуст. устар. металлУргия)
                    мещанИн
                    мИзерный и мизЕрный
                    мозаИчный
                    молодЁжь
                    молОчник [допуст. шн]
                    молЯщий
                    монолОг
                    мусоропровОд
                    мытАрство

                    Н

                    нАбело и допуст. устар. набелО
                    навЕрх
                    наврАть — навралА
                    надОлго
                    нАголо и допуст. наголО
                    нагнУтый
                    наделИть — наделИт
                    надОлго
                    надорвАться — надорвалАсь
                    нажИвший
                    нАжитый — нажитА
                    назвАться — назвалАсь
                    накренИться — накренИтся
                    налИть — налилА, налИвший, налитА
                    намЕрение
                    нанЯвший
                    нарвАть — нарвалА
                    нарОст
                    насорИть - насорИт
                    начАть — нАчал, началА,нАчали, начАвший, начАв, начАвшись, нАчатый
                    недоИмка
                    нЕдруг
                    недУг
                    некролОг
                    нЕнависть
                    ненадОлго
                    неподалЁку
                    непревзойдЁнный
                    неприхотлИвый
                    нефтепровОд
                    низведЁнный - низведЁн
                    никчЁмный
                    новорождЁнный
                    нОвости, новостЕй
                    нОготь, нОгтя

                    О

                    обзвонИть — обзвонИт
                    обеспЕчение
                    облегчИть — облегчИт
                    облИться — облилАсь
                    обнЯться — обнялАсь
                    обогнАть — обогналА
                    ободрАть — ободралА
                    ободрИть,
                    ободрЁнный — ободрЁн, ободренА ободрИться — ободрИшься
                    обострЁнный
                    обострИть
                    одЕсский [д'е]
                    одноимЁнный
                    одолжИть — одолжИт
                    озлОбить
                    озлОбленный
                    оклЕить
                    окружИть — окружИт
                    оперИться
                    опломбировАть
                    опОшлить — опОшлят
                    определЁнный — определЁн
                    оптОвый
                    освЕдомить — освЕдомишь
                    остриЁ осуждЁнный
                    отбелЁнный
                    отбЫть — отбылА
                    отдАть — отдалА, отдАв
                    отключЁнный
                    откУпорить
                    отозвАть — отозвалА
                    отозвАться — отозвалАсь
                    Отрочество
                    отчАсти
                    отымЁнный

                    П

                    паралИч
                    партЕр
                    патриархИя и допуст. патриАрхия
                    пАхота
                    пепелИще
                    перезвонИть — перезвонИт
                    перелИть — перелилА
                    пЕрчить и допуст. перчИть
                    пЕтля и петлЯ
                    плАнер и допуст. планЁр
                    плЕсневеть
                    плодоносИть
                    повАренная соль
                    повторить — повторИт, повторЁнный
                    поделЁнный
                    поднЯв
                    позвАть — позвалА
                    позвонИть — позвонИшь, позвонИт
                    полИть — полилА
                    положИть — положИл
                    понЯть — понялА, понЯвший, понЯв
                    портфЕль
                    пОручни
                    послАть — послАла
                    постамЕнт
                    пОхороны (похорОн, На похоронАх)
                    предрЕкший
                    премИнуть
                    премировАть
                    прибЫть — прИбыл, прибылА, прИбыло, прибЫв
                    привнесЁнный
                    приговОр
                    придАное
                    призЫв
                    призывнИк
                    призывнОй (пункт, возраст)
                    призЫвный (зовущий)
                    принУдить
                    принЯть - прИнял, прИняли, прИнятый
                    прИнцип
                    приобретЕние
                    прирОст
                    приручЁнный
                    прожИвший
                    прозорлИвый
                    простынЯ
                    процЕнт
                    псевдонИм
                    пулОвер

                    Р

                    рАкурс и допуст. устар. ракУрс
                    ракУшка и допуст. рАкушка
                    рассердиться - рассердИлся
                    рвать — рвалА
                    ревЕнь
                    ремЕнь
                    ржАветь и ржавЕть
                    рОвен (но: нерОвен и неровЁн час)
                    рУсло


                    С

                    санитарИя
                    сантимЕтр
                    свЕдущий
                    сверлИть — сверлИшь, сверлИт
                    свЁкла
                    свИтер [тэ]
                    сечь — сЁк, секлА
                    сИлос
                    симмЕтрия и симметрИя
                    сиротА (мн. ч. сирОты)
                    скАнер [нэ]
                    скворЕчник [шн]
                    слУчай
                    снять — снялА, снЯтый
                    соболЕзнование
                    сОгнутый
                    создАть — создалА
                    созЫв
                    соплемЕнный
                    сорвАть — сорвалА
                    сорИть — сорИт
                    сосредотОчение
                    срЕдство {мн. ч. срЕдства)
                    стАтус
                    статУт
                    стАтуя
                    стеногрАфия
                    столЯр
                    сУдно
                    стресс допуст. [рэ]

                    Т

                    тамОжня
                    танцОвщица
                    темп [тэ]
                    тендЕнция [тэ, дэ]
                    тЕндер [тэ, дэ]
                    тЕплиться
                    тОрты
                    трИптих
                    тУфля

                    У

                    убрАть — убралА
                    убыстрИть
                    Угольный (от уголь)
                    угОльный (от угол)
                    углубИть
                    украИнский
                    укрепИть — укрепИт
                    улУчшить — улУчшенный
                    усугубИть и допуст. устар. усугУбить

                    Ф

                    факсИмиле
                    фарфОр
                    фенОмен (научн. термин)
                    фенОмен (редкое явление) и допуст. феномЕн
                    фетИш
                    филИстер
                    флЕйтовый
                    флюорогрАфия
                    фОрзац
                    формировАть

                    X

                    хАос (в древнегреческой мифологии)
                    хАос и допуст. устар. хаОс (беспорядок)
                    характЕрный (типичный)
                    харАктерный (актёр)
                    хлОпок, хлОпковый
                    ходАтайствовать
                    хозЯин (мн. ч. хозЯева)
                    хОленный (прич.)
                    хОленый и допуст. холЁный (прил.)
                    хОлодность
                    христианИн
                    христопродАвец

                    Ц

                    цемЕнт
                    цЕнтнер
                    цепОчка
                    цыгАн

                    Ч

                    чЕрпать
                    чИстильщик

                    Ш

                    шассИ
                    шарф, шАрфа, мн. ч. шАрфы
                    шАхтинский (к шАхты) - шАхтинцы
                    щемИть — щемИт
                    шинЕль [н'е]
                    шофЁр
                    шпрИцы

                    Щ

                    щавЕль
                    щЕбень
                    щегольскОй
                    щепА
                    щепОтка
                    щЁлка
                    щЁлкать

                    Э

                    Экскурс
                    экспЕрт — экспЕртный
                    Экспорт
                    эпилОг

                    Ю

                    Юркнуть и юркнУть
                    юрОдивый

                    Я

                    языковОй (относящийся к словесному выражению мыслей человека)
                    языкОвый (относящийся к органу полости рта)
                    яИчница [шн]
                    яИчный допуст. [шн]}