import json

TOKEN = '80624ac5f0a5b0eb5a8272322ec75a54ff9b65051350bb288a81b72af5509e31f2fb940b3917606f794b7'
INFO = open('info.txt', mode='r', encoding='utf-8').readlines()
WORDS_ORTHOEPY = json.dumps(
    {'августовский': {'correct': 'а́вгустовский', 'variants': ['а́вгустовский', 'августо́вский']},
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
     'вероисповедание': {'correct': 'вероиспове́дание',
                         'variants': ['вероиспове́дание', 'вероисповеда́ние']},
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
     'волгодонский (г. Волгодонск)': {'correct': 'волгодо́нский',
                                      'variants': ['волгодо́нский', 'волго́донский']},
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
     'давнишний': {'correct': 'давни́шний', 'variants': ['давни́шний', 'да́внишний']},
     'девичий': {'correct': 'де́вичий', 'variants': ['де́вичий', 'деви́чий']},
     'демократия': {'correct': 'демокра́тия', 'variants': ['демокра́тия', 'демократи́я']},
     'деспот': {'correct': 'де́спот', 'variants': ['де́спот', 'деспо́т']},
     'дефис': {'correct': 'дефи́с', 'variants': ['дефи́с', 'де́фис']},
     'диагноз': {'correct': 'диа́гноз', 'variants': ['диа́гноз', 'диагно́з']},
     'диалог': {'correct': 'диало́г', 'variants': ['диало́г', 'диа́лог']},
     'диспансер': {'correct': 'диспансе́р', 'variants': ['диспансе́р', 'диспа́нсер']},
     'добела': {'correct': 'добела́', 'variants': ['до́бела', 'добела́']},
     'добрала': {'correct': 'добрала́', 'variants': ['добрала́', 'добра́ла']},
     'добралась': {'correct': 'добрала́сь', 'variants': ['добрала́сь', 'добра́лась']},
     'добыча': {'correct': 'добы́ча', 'variants': ['добы́ча', 'до́быча']},
     'доверху': {'correct': 'до́верху', 'variants': ['дове́рху', 'до́верху']},
     'догмат': {'correct': 'до́гмат', 'variants': ['до́гмат', 'догма́т']},
     'договор': {'correct': 'догово́р', 'variants': ['до́говор', 'догово́р']},
     'договоренность': {'correct': 'договорённость', 'variants': ['договорённость', 'догово́ренность']},
     'договорный': {'correct': 'догово́рный', 'variants': ['догово́рный', 'до́говорный']},
     'дождалась': {'correct': 'дождала́сь', 'variants': ['дождала́сь', 'дожда́лась']},
     'дозвонится': {'correct': 'дозвони́тся', 'variants': ['дозвони́тся', 'дозво́нится']},
     'дозвонятся': {'correct': 'дозвоня́тся', 'variants': ['дозвоня́тся', 'дозво́нятся']},
     'дозировать': {'correct': 'дози́ровать', 'variants': ['дози́ровать', 'дозирова́ть']},
     'документ': {'correct': 'докуме́нт', 'variants': ['докуме́нт', 'доку́мент']},
     'донельзя': {'correct': 'доне́льзя', 'variants': ['доне́льзя', 'до́нельзя']},
     'донизу': {'correct': 'до́низу', 'variants': ['до́низу', 'дони́зу']},
     'досуг': {'correct': 'досу́г', 'variants': ['досу́г', 'до́суг']},
     'досуха': {'correct': 'до́суха', 'variants': ['до́суха', 'досу́ха']},
     'дочерна': {'correct': 'дочерна́', 'variants': ['дочерна́', 'до́черна']},
     'драматургия': {'correct': 'драматурги́я', 'variants': ['драматурги́я', 'драмату́ргия']},
     'дремота': {'correct': 'дремо́та', 'variants': ['дремо́та', 'дремота́']},
     'духовник': {'correct': 'духовни́к', 'variants': ['духовни́к', 'духо́вник']},
     'еретик': {'correct': 'ерети́к', 'variants': ['ерети́к', 'ере́тик']},
     'жалюзи': {'correct': 'жалюзи́', 'variants': ['жалюзи́', 'жа́люзи']},
     'ждала': {'correct': 'ждала́', 'variants': ['ждала́', 'жда́ла']},
     'желоб': {'correct': 'жёлоб', 'variants': ['жёлоб', 'же́лоб']},
     'житие': {'correct': 'житие́', 'variants': ['житие́', 'жи́тие']},
     'житься': {'correct': 'жи́ться', 'variants': ['жи́ться', 'житься́']},
     'жилось': {'correct': 'жило́сь', 'variants': ['жило́сь', 'жи́лось']},
     'забронировать (записать)': {'correct': 'заброни́ровать',
                                  'variants': ['заброни́ровать', 'забронирова́ть']},
     'забронировать (покрыть броней)': {'correct': 'забронирова́ть',
                                        'variants': ['забронирова́ть', 'заброни́ровать']},
     'завидно': {'correct': 'зави́дно', 'variants': ['зави́дно', 'за́видно']},
     'завороженный': {'correct': 'заворожённый', 'variants': ['заворожённый', 'заворо́женный']},
     'заговор (как тайное соглашение, так и заклинание)': {'correct': 'за́говор',
                                                           'variants': ['за́говор', 'загово́р']},
     'загодя': {'correct': 'за́годя', 'variants': ['за́годя', 'загодя́']},
     'загнутый': {'correct': 'за́гнутый', 'variants': ['за́гнутый', 'загну́тый']},
     'задолго': {'correct': 'задо́лго', 'variants': ['задо́лго', 'за́долго']},
     'заем': {'correct': 'заём', 'variants': ['заём', 'за́ем']},
     'заиндеветь': {'correct': ['заи́ндеветь', 'заиндеве́ть'], 'variants': ['заи́ндеветь', 'заиндеве́ть']},
     'закупорить': {'correct': 'заку́порить', 'variants': ['заку́порить', 'закупо́рить']},
     'закупорив': {'correct': 'заку́порив', 'variants': ['заку́порив', 'закупо́рив']},
     'закупорка': {'correct': 'заку́порка', 'variants': ['заку́порка', 'закупо́рка']},
     'занятой': {'correct': 'занято́й', 'variants': ['занято́й', 'за́нятой']},
     'занятый': {'correct': 'за́нятый', 'variants': ['за́нятый', 'заня́тый']},
     'занята': {'correct': 'занята́', 'variants': ['занята́', 'за́нята']},
     'занять': {'correct': 'заня́ть', 'variants': ['заня́ть', 'за́нять']},
     'занял': {'correct': 'за́нял', 'variants': ['за́нял', 'заня́л']},
     'заняла': {'correct': 'заняла́', 'variants': ['за́няла', 'заняла́']},
     'заняло': {'correct': 'за́няло', 'variants': ['за́няло', 'заняло́']},
     'заняли': {'correct': 'за́няли', 'variants': ['за́няли', 'заняли́']},
     'заперлась': {'correct': 'заперла́сь', 'variants': ['за́перлась', 'заперла́сь']},
     'запертый': {'correct': 'за́пертый', 'variants': ['за́пертый', 'запёртый']},
     'заперта': {'correct': 'заперта́', 'variants': ['заперта́', 'за́перта']},
     'заржаветь': {'correct': 'заржаве́ть', 'variants': ['заржаве́ть', 'заржа́веть']},
     'засветло': {'correct': 'за́светло', 'variants': ['за́светло', 'засветло́']},
     'заселенный': {'correct': 'заселённый', 'variants': ['заселённый', 'засе́ленный']},
     'заселена': {'correct': 'заселена́', 'variants': ['заселена́', 'засе́лена']},
     'затемно': {'correct': 'за́темно', 'variants': ['за́темно', 'затемно́']},
     'звонишь': {'correct': 'звони́шь', 'variants': ['звони́шь', 'зво́нишь']},
     'звонит': {'correct': 'звони́т', 'variants': ['звони́т', 'зво́нит']},
     'звонят': {'correct': 'звоня́т', 'variants': ['звоня́т', 'зво́нят']},
     'зимовщик': {'correct': 'зимо́вщик', 'variants': ['зимо́вщик', 'зимовщи́к']},
     'злоба': {'correct': 'зло́ба', 'variants': ['зло́ба', 'злоба́']},
     'знамение': {'correct': 'зна́мение', 'variants': ['зна́мение', 'знаме́ние']},
     'знахарство': {'correct': 'зна́харство', 'variants': ['зна́харство', 'знаха́рство']},
     'знахарка': {'correct': ['знаха́рка', 'зна́харка'], 'variants': ['зна́харка', 'знаха́рка']},
     'значимость': {'correct': 'зна́чимость', 'variants': ['зна́чимость', 'значи́мость']},
     'значимый': {'correct': 'зна́чимый', 'variants': ['зна́чимый', 'значи́мый']},
     'зубчатый': {'correct': 'зубча́тый', 'variants': ['зубча́тый', 'зу́бчатый']},
     'игрище': {'correct': 'и́грище', 'variants': ['и́грище', 'игри́ще']},
     'иероглиф': {'correct': 'иероглиф', 'variants': ['иеро́глиф', 'иерогли́ф']},
     'избалованный': {'correct': 'избало́ванный', 'variants': ['избало́ванный', 'изба́лованный']},
     'издавна': {'correct': 'и́здавна', 'variants': ['и́здавна', 'изда́вна']},
     'изредка': {'correct': 'и́зредка', 'variants': ['и́зредка', 'изредка́']},
     'иконопись': {'correct': 'и́конопись', 'variants': ['и́конопись', 'ико́нопись']},
     'иксы': {'correct': 'и́ксы', 'variants': ['и́ксы', 'иксы́']},
     'индустрия': {'correct': 'индустри́я', 'variants': ['индустри́я', 'инду́стрия']},
     'инсульт': {'correct': 'инсу́льт', 'variants': ['инсу́льт', 'и́нсульт']},
     'исключит': {'correct': 'исключи́т', 'variants': ['исключи́т', 'исклю́чит']},
     'искра': {'correct': 'и́скра', 'variants': ['и́скра', 'искра́']},
     'исстари': {'correct': 'и́сстари', 'variants': ['и́сстари', 'исста́ри']},
     'исчерпать': {'correct': 'исче́рпать', 'variants': ['исче́рпать', 'исчерпа́ть']},
     'каталог': {'correct': 'катало́г', 'variants': ['катало́г', 'ката́лог']},
     'катарсис': {'correct': 'ка́тарсис', 'variants': ['ка́тарсис', 'ката́рсис']},
     'кашлянуть': {'correct': 'ка́шлянуть', 'variants': ['ка́шлянуть', 'кашляну́ть']},
     'квартал': {'correct': 'кварта́л', 'variants': ['кварта́л', 'ква́ртал']},
     'кедровый': {'correct': 'кедро́вый', 'variants': ['кедро́вый', 'ке́дровый']},
     'километр': {'correct': 'киломе́тр', 'variants': ['киломе́тр', 'кило́метр']},
     'кинематография': {'correct': 'кинематогра́фия', 'variants': ['кинематогра́фия', 'кинематографи́я']},
     'клала': {'correct': 'кла́ла', 'variants': ['кла́ла', 'клала́']},
     'клеенный (причастие)': {'correct': 'кле́енный', 'variants': ['кле́енный', 'клеённый']},
     'клееный (прилагательное)': {'correct': 'клеёный', 'variants': ['клеёный', 'кле́еный']},
     'кожевенный': {'correct': 'коже́венный', 'variants': ['коже́венный', 'кожеве́нный']},
     'коклюш': {'correct': 'коклю́ш', 'variants': ['коклю́ш', 'ко́клюш']},
     'колледж': {'correct': 'ко́лледж', 'variants': ['ко́лледж', 'колле́дж']},
     'коллеж': {'correct': 'колле́ж', 'variants': ['колле́ж', 'ко́ллеж']},
     'колосс': {'correct': 'коло́сс', 'variants': ['коло́сс', 'ко́лосс']},
     'компас': {'correct': 'ко́мпас', 'variants': ['ко́мпас', 'компа́с']},
     'кормящий': {'correct': 'кормя́щий', 'variants': ['кормя́щий', 'ко́рмящий']},
     'корысть': {'correct': 'коры́сть', 'variants': ['коры́сть', 'ко́рысть']},
     'краны': {'correct': 'кра́ны', 'variants': ['кра́ны', 'краны́']},
     'красивее': {'correct': 'краси́вее', 'variants': ['краси́вее', 'красивее́']},
     'красивейший': {'correct': 'краси́вейший', 'variants': ['краси́вейший', 'красиве́йший']},
     'кралась': {'correct': 'кра́лась', 'variants': ['крала́сь', 'кра́лась']},
     'кремень': {'correct': 'креме́нь', 'variants': ['креме́нь', 'кре́мень']},
     'кремня': {'correct': 'кремня́', 'variants': ['кремня́', 'кре́мня']},
     'кровоточащий': {'correct': 'кровоточа́щий', 'variants': ['кровоточа́щий', 'кровото́чащий']},
     'кровоточить': {'correct': 'кровоточи́ть', 'variants': ['кровоточи́ть', 'кровото́чить']},
     'кухонный': {'correct': 'ку́хонный', 'variants': ['ку́хонный', 'кухо́нный']},
     'лгала': {'correct': 'лгала́', 'variants': ['лгала́', 'лга́ла']},
     'лекторов': {'correct': 'ле́кторов', 'variants': ['ле́кторов', 'лекторо́в']},
     'лилась': {'correct': 'лила́сь', 'variants': ['лила́сь', 'ли́лась']},
     'ловка': {'correct': 'ловка́', 'variants': ['ловка́', 'ло́вка']},
     'ломота': {'correct': 'ломо́та', 'variants': ['ломо́та', 'ломота́']},
     'ломоть': {'correct': 'ломо́ть', 'variants': ['ломо́ть', 'ло́моть']},
     'лоскут (отходы, остатки)': {'correct': 'ло́скут', 'variants': ['ло́скут', 'лоску́т']},
     'лоскут (кусочек ткани)': {'correct': 'лоску́т', 'variants': ['лоску́т', 'ло́скут']},
     'лососевый': {'correct': 'лососёвый', 'variants': ['лососёвый', 'лосо́севый']},
     'лубочный': {'correct': 'лубо́чный', 'variants': ['лубо́чный', 'лу́бочный']},
     'мастерски': {'correct': ['ма́стерски', 'мастерски́'], 'variants': ['ма́стерски', 'мастерски́']},
     'мастерство': {'correct': 'мастерство́', 'variants': ['ма́стерство', 'мастерство́']},
     'мельком': {'correct': 'ме́льком', 'variants': ['ме́льком', 'мелько́м']},
     'местностей': {'correct': 'ме́стностей', 'variants': ['ме́стностей', 'местносте́й']},
     'металлургия': {'correct': 'металлурги́я', 'variants': ['металлурги́я', 'металлу́ргия']},
     'мещанин': {'correct': 'мещани́н', 'variants': ['мещани́н', 'меща́нин']},
     'мизерный': {'correct': ['ми́зерный', 'мизе́рный'], 'variants': ['ми́зерный', 'мизе́рный']},
     'мозаичный': {'correct': 'мозаи́чный', 'variants': ['мозаи́чный', 'моза́ичный']},
     'молящий': {'correct': 'моля́щий', 'variants': ['моля́щий', 'мо́лящий']},
     'мусоропровод': {'correct': 'мусоропрово́д', 'variants': ['мусоропрово́д', 'мусоропро́вод']},
     'мытарство': {'correct': 'мыта́рство', 'variants': ['мыта́рство', 'мы́тарство']},
     'набело': {'correct': 'на́бело', 'variants': ['на́бело', 'набело́']},
     'наврала': {'correct': 'наврала́', 'variants': ['наврала́', 'навра́ла']},
     'надолго': {'correct': 'надо́лго', 'variants': ['надо́лго', 'на́долго']},
     'наголо': {'correct': ['на́голо', 'наголо́'], 'variants': ['на́голо', 'наголо́']},
     'нагнутый': {'correct': 'нагну́тый', 'variants': ['нагну́тый', 'на́гнутый']},
     'наделит': {'correct': 'надели́т', 'variants': ['надели́т', 'наде́лит']},
     'надорвалась': {'correct': 'надорвала́сь', 'variants': ['надорва́лась', 'надорвала́сь']},
     'наживший': {'correct': 'нажи́вший', 'variants': ['нажи́вший', 'на́живший']},
     'нажитый': {'correct': 'на́житый', 'variants': ['на́житый', 'нажи́тый']},
     'нажита': {'correct': 'нажита́', 'variants': ['нажита́', 'на́жита']},
     'назвалась': {'correct': 'назвала́сь', 'variants': ['назвала́сь', 'назва́лась']},
     'накренится': {'correct': 'накрени́тся', 'variants': ['накрени́тся', 'накре́нится']},
     'налила': {'correct': 'налила́', 'variants': ['налила́', 'нали́ла']},
     'наливший': {'correct': 'нали́вший', 'variants': ['нали́вший', 'на́ливший']},
     'налита': {'correct': 'налита́', 'variants': ['нали́та', 'налита́']},
     'нанявший': {'correct': 'наня́вший', 'variants': ['наня́вший', 'на́нявший']},
     'нарвала': {'correct': 'нарвала́', 'variants': ['нарвала́', 'нарва́ла']},
     'насорит': {'correct': 'насори́т', 'variants': ['насори́т', 'насо́рит']},
     'начать': {'correct': 'нача́ть', 'variants': ['нача́ть', 'на́чать']},
     'начал': {'correct': 'на́чал', 'variants': ['на́чал', 'нача́л']},
     'начала': {'correct': 'начала́', 'variants': ['начала́', 'на́чала']},
     'начали': {'correct': 'на́чали', 'variants': ['на́чали', 'начали́']},
     'начавший': {'correct': 'нача́вший', 'variants': ['нача́вший', 'на́чавший']},
     'начав': {'correct': 'нача́в', 'variants': ['нача́в', 'на́чав']},
     'начавшись': {'correct': 'нача́вшись', 'variants': ['нача́вшись', 'на́чавшись']},
     'начатый': {'correct': 'на́чатый', 'variants': ['на́чатый', 'нача́тый']},
     'недруг': {'correct': 'не́друг', 'variants': ['не́друг', 'недру́г']},
     'недуг': {'correct': 'неду́г', 'variants': ['неду́г', 'не́дуг']},
     'некролог': {'correct': 'некроло́г', 'variants': ['некроло́г', 'некро́лог']},
     'неровен (час)': {'correct': ['неро́вен', 'неровён'], 'variants': ['неро́вен', 'неровён']},
     'нефтепровод': {'correct': 'нефтепрово́д', 'variants': ['нефтепрово́д', 'нефтепро́вод']},
     'низведенный': {'correct': 'низведенный', 'variants': ['низведённый', 'низведе́нный']},
     'низведен': {'correct': 'низведён', 'variants': ['низведён', 'низведе́н']},
     'никчемный': {'correct': 'никчёмный', 'variants': ['никчёмный', 'никче́мный']},
     'новорожденный': {'correct': 'новорождённый', 'variants': ['новорождённый', 'новоро́жденный']},
     'ногтя': {'correct': 'но́гтя', 'variants': ['но́гтя', 'ногтя́']},
     'обеспечение': {'correct': 'обеспе́чение', 'variants': ['обеспе́чение', 'обеспече́ние']},
     'облегчить': {'correct': 'облегчи́ть', 'variants': ['облегчи́ть', 'обле́гчить']},
     'облегчит': {'correct': 'облегчи́т', 'variants': ['облегчи́т', 'обле́гчит']},
     'облилась': {'correct': 'облила́сь', 'variants': ['облила́сь', 'обли́лась']},
     'обнялась': {'correct': 'обняла́сь', 'variants': ['обняла́сь', 'обня́лась']},
     'обогнала': {'correct': 'обогнала́', 'variants': ['обогнала́', 'обогна́ла']},
     'ободрала': {'correct': 'ободрала́', 'variants': ['ободрала́', 'ободра́ла']},
     'одолжить': {'correct': 'одолжи́ть', 'variants': ['одолжи́ть', 'одо́лжить']},
     'одолжит': {'correct': 'одолжи́т', 'variants': ['одолжи́т', 'одо́лжит']},
     'озлобить': {'correct': 'озло́бить', 'variants': ['озло́бить', 'озлоби́ть']},
     'озлобленный': {'correct': 'озло́бленный', 'variants': ['озло́бленный', 'озлоблённый']},
     'оклеить': {'correct': 'окле́ить', 'variants': ['окле́ить', 'оклеи́ть']},
     'окружит': {'correct': 'окружи́т', 'variants': ['окружи́т', 'окру́жит']},
     'опериться': {'correct': 'опери́ться', 'variants': ['опери́ться', 'опе́риться']},
     'опломбировать': {'correct': 'опломбирова́ть', 'variants': ['опломбирова́ть', 'опломби́ровать']},
     'опошлить': {'correct': 'опо́шлить', 'variants': ['опо́шлить', 'опошли́ть']},
     'опошлит': {'correct': 'опо́шлит', 'variants': ['опо́шлит', 'опошли́т']},
     'оптовый': {'correct': 'опто́вый', 'variants': ['опто́вый', 'о́птовый']},
     'осведомить': {'correct': 'осве́домить', 'variants': ['осве́домить', 'осведоми́ть']},
     'осведомишь': {'correct': 'осве́домишь', 'variants': ['осве́домишь', 'осведоми́шь']},
     'осведомит': {'correct': 'осве́домит', 'variants': ['осве́домит', 'осведоми́т']},
     'острие': {'correct': 'остриё', 'variants': ['остриё', 'острие́']},
     'осужденный': {'correct': 'осуждённый', 'variants': ['осуждённый', 'осу́жденный']},
     'отбеленный': {'correct': 'отбелённый', 'variants': ['отбелённый', 'отбе́ленный']},
     'отбыть': {'correct': 'отбы́ть', 'variants': ['отбы́ть', 'о́тбыть']},
     'отбыла': {'correct': 'отбыла', 'variants': ['отбыла́', 'о́тбыла']},
     'отдать': {'correct': 'отда́ть', 'variants': ['отда́ть', 'о́тдать']},
     'отдала': {'correct': 'отдала́', 'variants': ['отдала́', 'отда́ла']},
     'отдав': {'correct': 'отдав', 'variants': ['отда́в', 'о́тдав']},
     'отключенный': {'correct': 'отключённый', 'variants': ['отключённый', 'отклю́ченный']},
     'откупорить': {'correct': 'отку́порить', 'variants': ['отку́порить', 'откупо́рить']},
     'отозвала': {'correct': 'отозвала́', 'variants': ['отозвала́', 'отозва́ла']},
     'отозвалась': {'correct': 'отозвала́сь', 'variants': ['отозвала́сь', 'отозва́лась']},
     'отрочество': {'correct': 'о́трочество', 'variants': ['о́трочество', 'отро́чество']},
     'отчасти': {'correct': 'отча́сти', 'variants': ['отча́сти', 'о́тчасти']},
     'отыменный': {'correct': 'отымённый', 'variants': ['отымённый', 'отыме́нный']},
     'отзыв (на книгу)': {'correct': 'о́тзыв', 'variants': ['о́тзыв', 'отзы́в']},
     'отзыв (посла)': {'correct': 'отзы́в', 'variants': ['отзы́в', 'о́тзыв']},
     'партер': {'correct': 'парте́р', 'variants': ['парте́р', 'па́ртер']},
     'патриархия': {'correct': ['патриархи́я', 'патриа́рхия'], 'variants': ['патриархи́я', 'патриа́рхия']},
     'пахота': {'correct': 'па́хота', 'variants': ['па́хота', 'пахо́та']},
     'пепелище': {'correct': 'пепели́ще', 'variants': ['пепели́ще', 'пе́пелище']},
     'перезвонит': {'correct': 'перезвони́т', 'variants': ['перезвони́т', 'перезво́нит']},
     'перелила': {'correct': 'перелила́', 'variants': ['перелила́', 'перели́ла']},
     'перчить': {'correct': ['пе́рчить', 'перчи́ть'], 'variants': ['пе́рчить', 'перчи́ть']},
     'петля': {'correct': ['пе́тля', 'петля́'], 'variants': ['пе́тля', 'петля́']},
     'планер': {'correct': ['пла́нер', 'планёр'], 'variants': ['пла́нер', 'планёр']},
     'плесневеть': {'correct': 'пле́сневеть', 'variants': ['пле́сневеть', 'плесневе́ть']},
     'плодоносить': {'correct': 'плодоноси́ть', 'variants': ['плодоноси́ть', 'плодоно́сить']},
     'поваренная (соль)': {'correct': 'пова́ренная', 'variants': ['пова́ренная', 'поварённая']},
     'повторит': {'correct': 'повтори́т', 'variants': ['повтори́т', 'повто́рит']},
     'повторенный': {'correct': 'повторённый', 'variants': ['повторённый', 'повто́ренный']},
     'поделенный': {'correct': 'поделённый', 'variants': ['поделённый', 'поде́ленный']},
     'подняв': {'correct': 'подня́в', 'variants': ['подня́в', 'по́дняв']},
     'позвала': {'correct': 'позвала́', 'variants': ['позвала́', 'позва́ла']},
     'позвонишь': {'correct': 'позвони́шь', 'variants': ['позвони́шь', 'позво́нишь']},
     'позвонит': {'correct': 'позвони́т', 'variants': ['позвони́т', 'позво́нит']},
     'полила': {'correct': 'полила́', 'variants': ['полила́', 'поли́ла']},
     'поняла': {'correct': 'поняла́', 'variants': ['поняла́', 'по́няла']},
     'понявший': {'correct': 'поня́вший', 'variants': ['поня́вший', 'по́нявший']},
     'поняв': {'correct': 'поня́в', 'variants': ['поня́в', 'по́няв']},
     'поручни': {'correct': 'по́ручни', 'variants': ['по́ручни', 'пору́чни']},
     'послала': {'correct': 'посла́ла', 'variants': ['посла́ла', 'послала́']},
     'постамент': {'correct': 'постаме́нт', 'variants': ['поста́мент', 'постаме́нт']},
     'похороны': {'correct': 'по́хороны', 'variants': ['по́хороны', 'похоро́ны']},
     'похорон': {'correct': 'похоро́н', 'variants': ['похоро́н', 'по́хорон']},
     '(на) похоронах': {'correct': 'похорона́х', 'variants': ['похорона́х', 'похоро́нах']},
     'предрекший': {'correct': 'предрёкший', 'variants': ['предре́кший', 'предрёкший']},
     'преминуть': {'correct': 'преми́нуть', 'variants': ['преми́нуть', 'премину́ть']},
     'премировать': {'correct': 'премирова́ть', 'variants': ['премирова́ть', 'преми́ровать']},
     'прибыть': {'correct': 'прибы́ть', 'variants': ['прибы́ть', 'при́быть']},
     'прибыл': {'correct': 'при́был', 'variants': ['при́был', 'прибы́л']},
     'прибыла': {'correct': 'прибыла́', 'variants': ['прибыла́', 'при́была']},
     'прибыв': {'correct': 'прибы́в', 'variants': ['прибы́в', 'при́быв']},
     'привнесенный': {'correct': 'привнесённый', 'variants': ['привнесённый', 'привне́сенный']},
     'приданое': {'correct': 'прида́ное', 'variants': ['прида́ное', 'при́даное']},
     'призыв': {'correct': 'призы́в', 'variants': ['призы́в', 'при́зыв']},
     'призывник': {'correct': 'призывни́к', 'variants': ['призывни́к', 'призы́вник']},
     'призывной (пункт, возраст)': {'correct': 'призывно́й', 'variants': ['призывно́й', 'призы́вной']},
     'призывный (зовущий)': {'correct': 'призы́вный', 'variants': ['призы́вный', 'при́зывный']},
     'принудить': {'correct': 'прину́дить', 'variants': ['прину́дить', 'принуди́ть']},
     'принял': {'correct': 'при́нял', 'variants': ['при́нял', 'приня́л']},
     'принятый': {'correct': 'при́нятый', 'variants': ['при́нятый', 'приня́тый']},
     'принцип': {'correct': 'при́нцип', 'variants': ['при́нцип', 'принци́п']},
     'прирост': {'correct': 'приро́ст', 'variants': ['приро́ст', 'при́рост']},
     'прирученный': {'correct': 'приручённый', 'variants': ['приручённый', 'приру́ченный']},
     'проживший': {'correct': 'прожи́вший', 'variants': ['прожи́вший', 'про́живший']},
     'прозорливый': {'correct': 'прозорли́вый', 'variants': ['прозорли́вый', 'прозо́рливый']},
     'простыня': {'correct': 'простыня́', 'variants': ['простыня́', 'про́стыня']},
     'псевдоним': {'correct': 'псевдони́м', 'variants': ['псевдони́м', 'псе́вдоним']},
     'пуловер': {'correct': 'пуло́вер', 'variants': ['пуло́вер', 'пу́ловер']},
     'ракурс': {'correct': 'ра́курс', 'variants': ['ра́курс', 'раку́рс']},
     'ракушка': {'correct': ['раку́шка', 'ра́кушка'], 'variants': ['раку́шка', 'ра́кушка']},
     'рассердился': {'correct': 'рассерди́лся', 'variants': ['рассерди́лся', 'рассе́рдился']},
     'рвала': {'correct': 'рвала́', 'variants': ['рвала́', 'рва́ла']},
     'ревень': {'correct': 'реве́нь', 'variants': ['реве́нь', 'ре́вень']},
     'ремень': {'correct': 'реме́нь', 'variants': ['реме́нь', 'ре́мень']},
     'ржаветь': {'correct': ['ржаве́ть', 'ржа́веть'], 'variants': ['ржаве́ть', 'ржа́веть']},
     'ровен': {'correct': 'ро́вен', 'variants': ['ро́вен', 'рове́н']},
     'равны': {'correct': 'равны́', 'variants': ['равны́', 'ра́вны']},
     'русло': {'correct': 'ру́сло', 'variants': ['ру́сло', 'русло́']},
     'санитария': {'correct': 'санитари́я', 'variants': ['санитари́я', 'санита́рия']},
     'сантиметр': {'correct': 'сантиме́тр', 'variants': ['сантиме́тр', 'санти́метр']},
     'сведущий': {'correct': 'све́дущий', 'variants': ['све́дущий', 'сведу́щий']},
     'сверлить': {'correct': 'сверли́ть', 'variants': ['сверли́ть', 'све́рлить']},
     'сверлишь': {'correct': 'сверли́шь', 'variants': ['сверли́шь', 'све́рлишь']},
     'сверлит': {'correct': 'сверли́т', 'variants': ['сверли́т', 'све́рлит']},
     'свекла': {'correct': 'свёкла', 'variants': ['свёкла', 'свекла́']},
     'силос': {'correct': 'си́лос', 'variants': ['си́лос', 'сило́с']},
     'симметрия': {'correct': ['симме́трия', 'симметри́я'], 'variants': ['симме́трия', 'симметри́я']},
     'сирота': {'correct': 'сирота́', 'variants': ['сирота́', 'сиро́та']},
     'сироты (мн.ч)': {'correct': 'сиро́ты', 'variants': ['сиро́ты', 'сироты́']},
     'сняла': {'correct': 'сняла́', 'variants': ['сняла́', 'сня́ла']},
     'соболезнование': {'correct': 'соболе́знование', 'variants': ['соболе́знование', 'соболезнова́ние']},
     'согнутый': {'correct': 'со́гнутый', 'variants': ['со́гнутый', 'согну́тый']},
     'создала': {'correct': 'создала́', 'variants': ['создала́', 'созда́ла']},
     'созыв': {'correct': 'созы́в', 'variants': ['созы́в', 'со́зыв']},
     'соплеменный': {'correct': 'соплеме́нный', 'variants': ['соплеме́нный', 'сопле́менный']},
     'сорвала': {'correct': 'сорвала́', 'variants': ['сорвала́', 'сорва́ла']},
     'сорит': {'correct': 'сори́т', 'variants': ['сори́т', 'со́рит']},
     'сосредоточение': {'correct': 'сосредото́чение', 'variants': ['сосредото́чение', 'сосредоточе́ние']},
     'средства': {'correct': 'сре́дства', 'variants': ['сре́дства', 'средства́']},
     'статус': {'correct': 'ста́тус', 'variants': ['ста́тус', 'стату́с']},
     'статут': {'correct': 'стату́т', 'variants': ['стату́т', 'ста́тут']},
     'стенография': {'correct': 'стеногра́фия', 'variants': ['стеногра́фия', 'стенографи́я']},
     'столяр': {'correct': 'столя́р', 'variants': ['столя́р', 'сто́ляр']},
     'судно': {'correct': 'су́дно', 'variants': ['су́дно', 'судно́']},
     'таможня': {'correct': 'тамо́жня', 'variants': ['тамо́жня', 'та́можня']},
     'танцовщица': {'correct': 'танцо́вщица', 'variants': ['танцо́вщица', 'танцовщи́ца']},
     'тендер': {'correct': 'те́ндер', 'variants': ['те́ндер', 'тенде́р']},
     'теплиться': {'correct': 'те́плиться', 'variants': ['те́плиться', 'тепли́ться']},
     'торты': {'correct': 'то́рты', 'variants': ['то́рты', 'торты́']},
     'триптих': {'correct': 'три́птих', 'variants': ['три́птих', 'трипти́х']},
     'туфля': {'correct': 'ту́фля', 'variants': ['ту́фля', 'туфля́']},
     'убрала': {'correct': 'убрала́', 'variants': ['убрала́', 'убра́ла']},
     'убыстрить': {'correct': 'убыстри́ть', 'variants': ['убыстри́ть', 'убы́стрить']},
     'угольный (от уголь)': {'correct': 'у́гольный', 'variants': ['у́гольный', 'уго́льный']},
     'угольный (от угол)': {'correct': 'уго́льный', 'variants': ['уго́льный', 'у́гольный']},
     'углубить': {'correct': 'углуби́ть', 'variants': ['углуби́ть', 'углу́бить']},
     'украинский': {'correct': 'украи́нский', 'variants': ['украи́нский', 'укра́инский']},
     'укрепит': {'correct': 'укрепи́т', 'variants': ['укрепи́т', 'укре́пит']},
     'улучшить': {'correct': 'улу́чшить', 'variants': ['улу́чшить', 'улучши́ть']},
     'улучшенный': {'correct': 'улу́чшенный', 'variants': ['улу́чшенный', 'улучшённый']},
     'усугубить': {'correct': 'усугуби́ть', 'variants': ['усугуби́ть', 'усугу́бить']},
     'факсимиле': {'correct': 'факси́миле', 'variants': ['факси́миле', 'факсимиле́']},
     'фарфор': {'correct': 'фарфо́р', 'variants': ['фарфо́р', 'фа́рфор']},
     'феномен (научн. термин)': {'correct': 'фено́мен', 'variants': ['фено́мен', 'феноме́н']},
     'феномен (редкое явление)': {'correct': ['фено́мен', 'феноме́н'], 'variants': ['фено́мен', 'феноме́н']},
     'фетиш': {'correct': 'фети́ш', 'variants': ['фети́ш', 'фе́тиш']},
     'филистер': {'correct': 'фили́стер', 'variants': ['фили́стер', 'фи́листер']},
     'флейтовый': {'correct': 'фле́йтовый', 'variants': ['фле́йтовый', 'флейто́вый']},
     'флюорография': {'correct': 'флюорогра́фия', 'variants': ['флюорогра́фия', 'флюорографи́я']},
     'форзац': {'correct': 'фо́рзац', 'variants': ['фо́рзац', 'форза́ц']},
     'формировать': {'correct': 'формирова́ть', 'variants': ['формирова́ть', 'форми́ровать']},
     'хаос': {'correct': 'ха́ос', 'variants': ['ха́ос', 'хао́с']},
     'характерный (типичный)': {'correct': 'характе́рный', 'variants': ['характе́рный', 'хара́ктерный']},
     'характерный (актёр)': {'correct': 'хара́ктерный', 'variants': ['хара́ктерный', 'характе́рный']},
     'хлопок (материал)': {'correct': 'хло́пок', 'variants': ['хло́пок', 'хлопо́к']},
     'хлопковый': {'correct': 'хло́пковый', 'variants': ['хло́пковый', 'хлопко́вый']},
     'ходатайствовать': {'correct': 'хода́тайствовать', 'variants': ['хода́тайствовать', 'ходата́йствовать']},
     'хозяева': {'correct': 'хозя́ева', 'variants': ['хозя́ева', 'хозяева́']},
     'холенный (прич.)': {'correct': 'хо́ленный', 'variants': ['хо́ленный', 'холённый']},
     'холеный (прил.)': {'correct': ['хо́леный', 'холёный'], 'variants': ['хо́леный', 'холёный']},
     'холодность': {'correct': 'хо́лодность', 'variants': ['хо́лодность', 'холо́дность']},
     'христианин': {'correct': 'христиани́н', 'variants': ['христиани́н', 'христиа́нин']},
     'христопродавец': {'correct': 'христопрода́вец', 'variants': ['христопрода́вец', 'христопродаве́ц']},
     'цемент': {'correct': 'цеме́нт', 'variants': ['цеме́нт', 'це́мент']},
     'центнер': {'correct': 'це́нтнер', 'variants': ['це́нтнер', 'центне́р']},
     'цепочка': {'correct': 'цепо́чка', 'variants': ['цепо́чка', 'це́почка']},
     'цыган': {'correct': 'цыга́н', 'variants': ['цыга́н', 'цы́ган']},
     'черпать': {'correct': 'че́рпать', 'variants': ['че́рпать', 'черпа́ть']},
     'чистильщик': {'correct': 'чи́стильщик', 'variants': ['чи́стильщик', 'чисти́льщик']},
     'шасси': {'correct': 'шасси́', 'variants': ['шасси́', 'ша́сси']},
     'шарфа': {'correct': 'ша́рфа', 'variants': ['ша́рфа', 'шарфа́']},
     'шарфы': {'correct': 'ша́рфы', 'variants': ['ша́рфы', 'шарфы́']},
     'шахтинский (г. Шахты)': {'correct': 'ша́хтинский', 'variants': ['ша́хтинский', 'шахти́нский']},
     'шахтинцы (г. Шахты)': {'correct': 'ша́хтинцы', 'variants': ['ша́хтинцы', 'шахти́нцы']},
     'шприцы': {'correct': 'шпри́цы', 'variants': ['шпри́цы', 'шприцы́']},
     'щавель': {'correct': 'щаве́ль', 'variants': ['щаве́ль', 'ща́вель']},
     'щебень': {'correct': 'ще́бень', 'variants': ['ще́бень', 'щебе́нь']},
     'щегольской': {'correct': 'щегольско́й', 'variants': ['щегольско́й', 'щего́льской']},
     'щемит': {'correct': 'щеми́т', 'variants': ['щеми́т', 'ще́мит']},
     'щепа': {'correct': 'ще́па', 'variants': ['ще́па', 'щепа́']},
     'щепотка': {'correct': 'щепо́тка', 'variants': ['щепо́тка', 'ще́потка']},
     'щелка': {'correct': 'щёлка', 'variants': ['щёлка', 'ще́лка']},
     'щелкать': {'correct': 'щёлкать', 'variants': ['щёлкать', 'щелка́ть']},
     'экскурс': {'correct': 'э́кскурс', 'variants': ['э́кскурс', 'экску́рс']},
     'эксперт': {'correct': 'экспе́рт', 'variants': ['экспе́рт', 'э́ксперт']},
     'экспорт': {'correct': 'э́кспорт', 'variants': ['э́кспорт', 'экспо́рт']},
     'эпиграф': {'correct': 'эпи́граф', 'variants': ['эпи́граф', 'эпигра́ф']},
     'эпилог': {'correct': 'эпило́г', 'variants': ['эпило́г', 'эпи́лог']},
     'юркнуть': {'correct': ['ю́ркнуть', 'юркну́ть'], 'variants': ['ю́ркнуть', 'юркну́ть']},
     'юродивый': {'correct': 'юро́дивый', 'variants': ['юро́дивый', 'юроди́вый']},
     'языковой (относящийся к словесному выражению мыслей человека)': {'correct': 'языково́й',
                                                                       'variants': ['языково́й', 'языко́вой']},
     'языковый (относящийся к органу полости рта)': {'correct': 'языко́вый', 'variants': ['языко́вый', 'язы́ковый']}
     })
