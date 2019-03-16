# -*- coding: utf-8 -*-
from vincenty import vincenty
import numpy as np
import os
import json

suba = [('prado veraniego',(4.71000195,-74.0659163)),('casablanca',(4.7376246,-74.0755493)),('la campiña',(4.7444033,-74.08567225)),('berlín',(4.7473583,-74.1171587574)),('pinares',(4.7495449,-74.0856456)),('santa rosa',(4.6965457,-74.0757271)),('suba',(4.73538995,-74.0822649713)),('lisboa',(4.7429247,-74.1229854)),('san jorge',(4.7144217,-74.0879699)),('suba reservado',(4.7512328,-74.112527)),('nueva zelandia',(4.7583197,-74.0482248)),('nueva tibabuyes',(4.7342056,-74.1086286)),('lago de suba',(4.7309519, -74.098624)),('salamanca y catalayud',(4.7340866,-74.0767505)),('puente largo',(4.6966924,-74.0658302)),('la floresta',(4.689288,-74.0740472)),('calle 187',(4.7655175,-74.0475745)),('san josé de bavaria',(4.7635443,-74.0615984)),('del monte',(4.7542047,-74.0677086)),('bulevar',(4.7447664,-74.0892808)),('morato',(4.6942855,-74.0753727)),('calatrava',(4.715543,-74.0752631)),('villa del prado',(4.7557424,-74.0537778)),('la alhambra',(4.69875,-74.0569907064)),('nuevo suba',(4.7545317,-74.0874733)),('calle 169',(4.7518483,-74.0585624)),('pontevedra',(4.6994285,-74.0792461)),('el rincón',(4.7250134,-74.0896687)),('el rubí',(4.7279215,-74.0901337)),('mirandela',(4.7655556,-74.0464503)),('córdoba',(4.7047194,-74.081218)),('niza',(4.7114031,-74.0731876207)),('tibabuyes',(4.7342056,-74.1086286)),('la gaitana',(4.7453692,-74.1079444)),('cataluña',(4.7417753,-74.0581713)),('punta del este',(4.7160813,-74.0937918)),('beamonte',(4.725324,-74.0626858)),('santa catalina',(4.7330632,-74.0634369495)),('aures',(4.7324296,-74.0986809)),('campania',(4.7141237,-74.071422)),('batán',(4.7033154,-74.0654623)),('manzana 13',(4.8001397,-74.0708502)),('bilbao',(4.7514007,-74.1195606)),('andes',(4.6930921,-74.0672382902)),('la pradera',(4.7549217,-74.1050811526)),('colina campestre',(4.7205491,-74.0675866)),('san pedro',(4.7669547,-74.0498970316))]
bosa = [('despensa',(4.5951372,-74.1881175)),('la libertad',(4.6250752,-74.1922483)),('transversal 77j',(4.5979635,-74.1898972)),('alameda del parque',(4.6033751,-74.2017827)),('laureles',(4.6103373,-74.1973599)),('pôrtal del porvenir',(4.6351192,-74.1903707)),('el jardín',(4.6128161,-74.2082547)),('olarte',(4.6006249,-74.1648094)),('piamonte',(4.6022214,-74.1902818)),('la capilla',(4.6061769,-74.1827105)),('palestina',(4.6160219,-74.1941877613)),('nuevo chile',(4.6033384,-74.1653016)),('calle 51c s',(4.6183945,-74.173436)),('bosa la esperanza',(4.6087433,-74.2091411)),('el recreo',(4.6326698,-74.2031471)),('calle 69b sur',(4.6000446,-74.190372)),('calle 54 bis s',(4.6182954,-74.1758284)),('la estación',(4.5976912,-74.1808275)),('calle 59c sur',(4.6258387,-74.1916078)),('bosa',(4.6098804,-74.1847155)),('carrera 81i',(4.6212488,-74.1761384)),('bosa islandia',(4.6141412,-74.2047188)),('getsemaní',(4.612645,-74.2065864)),('brasilia',(4.6280463,-74.1824055)),('parques de villa javier',(4.6125022,-74.204671)),('kasay',(4.6343038,-74.1998941)),('atalayas',(4.6314151,-74.1962206)),('portal del sol',(4.6319926,-74.2051577)),('bosa san diego',(4.6108608,-74.2116088)),('la amistad',(4.60291215,-74.1862513446))]
kennedy = [('patio bonito',(4.6371837,-74.1626883)),('carvajal',(4.6126766,-74.1387982)),('banderas',(4.6301224,-74.1501133)),('tintal',(4.6563117,-74.1580857)),('calle 9b s',(4.6172437,-74.126888)),('alquería',(4.6047732,-74.1359554)),('ciudad kennedy',(4.6213173,-74.1565652)),('lucerna',(4.6147131,-74.1465997)),('maria paz',(4.6370553,-74.1583475)),('casablanca',(4.6159652,-74.1701286)),('manuel mejia',(4.6141426,-74.1727056)),('mandalay',(4.6280664,-74.1435089)),('villa claudia',(4.6165206,-74.1286277)),('timiza',(4.6134038,-74.1536469)),('britalia',(4.6248444,-74.1708363)),('villas de kennedy',(4.64728835,-74.1362871186)),('techo',(4.625769,-74.1483562)),('castilla',(4.6398801,-74.1438846)),('parques de castilla',(4.6451583,-74.1403509)),('marsella',(4.6324646,-74.1311421)),('villa alsacia',(4.6426293,-74.1367689)),('el carmelo',(4.626476,-74.127856389)),('tintalá',(4.6404348,-74.1601433)),('class',(4.6143481,-74.1788191)),('calle 12',(4.6293865,-74.1499106403)),('alfonso lopez',(4.6028468,-74.1411414)),('kennedy',(4.6328768,-74.1525832)),('floralia',(4.6094816,-74.1331237)),('argelia',(4.6081369,-74.1425477)),('pio x',(4.6253665,-74.1396629)),('Mandalay',(4.6280664,-74.1435089))]
fontibon = [('fontibón', (4.6732919,-74.144636)), ('capellanía',(4.6694743,-74.1318729)),('puente grande',(4.6963439,-74.1678422)),('flandes',(4.6808394,-74.1512875)),('saturno',(4.6805831,-74.1480027)),('san pablo',(4.6873084,-74.1557508)),('versalles',(4.6838913,-74.1438694)),('la palestina',(4.6827639,-74.1493247)),('la laguna',(4.6717719,-74.1485211)),('modelia',(4.6676563,-74.1221512))]
engativa = [('tabora',(4.6939034,-74.1001372)),('ciudadela colsubsidio',(4.7209445,-74.1153633)),('metrópolis',(4.6816698,-74.0837965)),('conjunto florida de la sabana',(4.7212796,-74.1329415)),('avenida ciudad de cali',(4.7000644,-74.1031846)),('quirigua',(4.7095048,-74.1029737797)),('las ferias',(4.6887444,-74.08529)),('villas de granada',(4.7153998,-74.123366)),('bochica',(4.7157693,-74.1087115)),('la clarita',(4.6987928,-74.112882)),('calle 86',(4.69662765,-74.1061903699)),('bonanza',(4.6913705,-74.0904226)),('normandía',(4.6705301,-74.1097864)),('villas de madrigal',(4.7073762,-74.1121215)),('minuto de dios',(4.6977036,-74.0905468)),('el mirador',(4.7067569,-74.1370417)),('engativá',(4.68523865,-74.1141917683)),('garces navas',(4.7137089,-74.1195077)),('villas del dorado',(4.7015512,-74.1288219))]
usaquen = [('las orquídeas',(4.7408998,-74.0415338)),('bosque del marqués',(4.71515,-74.0285534)),('lijacá',(4.76628,-74.0288313)),('santa ana',(4.6875886,-74.0332444)),('quintas del redil',(4.7527429,-74.027559)),('verbenal',(4.7651505,-74.0383936)),('tibabita',(4.7633181,-74.0280315)),('canteras',(4.69785,-74.0259344)),('capri',(4.7283338,-74.0348055)),('toberín',(4.7472743,-74.0437185)),('san antonio',(4.7604128,-74.0377814)),('barrancas',(4.7348948,-74.0256288)),('usaquén',(4.6907151,-74.0377862528)),('san patricio',(4.69444665,-74.0505287729)),('bella suiza',(4.7063138,-74.0305872)),('servitá',(4.74159375,-74.0266687346)),('el otoño',(4.7655611,-74.033115)),('san antonio i',(4.7597047,-74.029111)),('la ermita',(4.710105,-74.0477394)),('cedritos',(4.7270454,-74.0443851)),('cantón norte',(4.6867619,-74.0390105)),('santa barbara',(4.7027863,-74.044451767)),('la carolina',(4.70422485,-74.0421826982))]
unidos = [('baquero',(4.6532601,-74.06905)),('quinta mutis',(4.65231325,-74.0723390228)),('siete de agosto',(4.6586107,-74.0734493)),('parque central salitre etapa 1',(4.6630841,-74.0817033)),('rionegro',(4.682342,-74.065662)),('jorge eliecer gaitan',(4.6736213,-74.0732198)),('doce de octubre',(4.6676689,-74.0738044)),('san fernando',(4.6779554,-74.0827904479)),('barrios unidos',(4.6701224,-74.0709255)),('calle 64',(4.67050195,-74.0750704541)),('la paz',(4.6605823,-74.0766009)),('alcázares norte',(4.663768,-74.0667188)),('entre ríos',(4.6810793,-74.075399)),('concepción norte',(4.65671895,-74.0654127833)),('la esperanza',(4.6507136,-74.0674583)),('villa calasanz',(4.6855099,-74.0596873663)),('los andes',(4.686598,-74.0708777)),('benjamín herrera',(4.652771,-74.0757209)),('muequetá',(4.65183575,-74.0722053118)),('la patria',(4.6845105,-74.0361422632)),('el rosario',(4.6549015,-74.0722113)),('el labrador',(4.6700484,-74.0872561971)),('josé joaquín vargas',(4.67037965,-74.0843203)),('polo club',(4.6727265,-74.0618128)),('jorge eliécer gaitán',(4.6736213,-74.0732198))]
teusaquillo = [('el campín',(4.6492185,-74.0729872244)),('ortezal',(4.6323357,-74.0939485)),('simón bolívar',(4.6280616,-74.0648872)),('la esmeralda',(4.646242,-74.0897417)),('rafael nuñez',(4.641683,-74.0886871)),('teusaquillo',(4.6423434,-74.0872168)),('acevedo tejada',(4.6298822,-74.0802485)),('la soledad',(4.63115145,-74.075252639)),('ciudad universitaria',(4.63874255,-74.0852376575)),('la magdalena',(4.62704825,-74.0727231764)),('galerías',(4.6430327,-74.0759949)),('quesada',(4.6405435,-74.0677509603)),('salitre oriental',(4.6428824,-74.1007665)),('belalcázar',(4.6413716,-74.0787789)),('nicolás de federman',(4.6493191,-74.0823261)),('quinta paredes',(4.6341901,-74.0932213)),('palermo',(4.63293615,-74.0695142346)),('calle 45a',(4.648597,-74.0908149)),('quirinal',(4.65418,-74.0867099)),('san luis',(4.6473439,-74.0684104)),('marly',(4.6375815,-74.0682333551)),('centro antonio nariño',(4.61671905,-74.0862002649)),('pablo vi',(4.651446,-74.087752))]
chapinero = [('la cabrera',(4.6662123,-74.0464209448)),('pardo rubio',(4.63346115,-74.063756775)),('calle 57',(4.6498252,-74.0465736042)),('el nogal',(4.6603208,-74.0535637)),('chapinero alto',(4.63232435,-74.063245273)),('quinta camacho',(4.65435295,-74.0607157)),('chapinero central',(4.64609685,-74.0609264156)),('la porciúncula',(4.6595752,-74.0572044844)),('el virrey',(4.67625875,-74.058965687)),('mariscal sucre',(4.6309073,-74.0610266)),('san luis',(4.6473439,-74.0684104)),('rosales',(4.6544679,-74.0496793)),('el lago',(4.66223635,-74.0606217214)),('chapinero',(4.6471197,-74.0634583)),('bosque calderón',(4.64214785,-74.0620784244)),('el chicó',(4.67021995,-74.044536091)),('la salle',(4.6438809,-74.0616022101)),('antiguo country',(4.6731551,-74.0539417))]
aranda = [('sorrento',(4.6192136,-74.1144189)),('ciudad montes',(4.5980478,-74.0760866)),('calle 1f',(4.6026895,-74.1062645)),('salazár gómez',(4.632255,-74.1125716)),('tejar',(4.6091307,-74.1281855)),('galán',(4.6181398,-74.1194443)),('torcoroma',(4.6215588,-74.1210439)),('trinidad',(4.6256084,-74.1180023)),('veraguas',(4.6068443,-74.1010331)),('la camelia',(4.615506,-74.1215696)),('colón',(4.619088,-74.0971036)),('puente aranda',(4.6135126,-74.1065729)),('milenta 3',(4.6171219,-74.1260438)),('comuneros',(4.611218,-74.1059001)),('la alquería',(4.59837135,-74.126607576)),('santa matilde',(4.5989051,-74.1067371191)),('alcalá',(4.6028079,-74.1281118)),('el jazmín',(4.6099241,-74.1150142)),('el ejido',(4.6262956,-74.1017129)),('torremolinos',(4.6084209,-74.1234627)),('gorgonzola',(4.6195015,-74.1062401)),('pradera, milenta',(4.5906344,-74.1018346211)),('la ponderosa',(4.610809,-74.119)),('primavera',(4.615025,-74.1078769)),('sonora',(4.61053,-74.1130478)),('tibana',(4.6117529,-74.1087750365)),('americas 68',(4.6234918,-74.1254391)),('jorge gaitán cortés',(4.5860329,-74.1298053)),('villa sonia',(4.5953793,-74.1283675)),('san rafael',(4.6258714,-74.0853288109)),('muzu',(4.5983524,-74.1199347)),('la pradera',(4.6243268,-74.1215789)),('santa isabel',(4.6010941,-74.1019894)),('milenta',(4.6131999,-74.1256615)),('el remanso',(4.5988015,-74.1130681)),('pensilvania',(4.6126932,-74.0933428)),('santa rita',(4.5978818,-74.1240115))]
martires = [('los mártires',(4.6210192,-74.0850280616)),('ricaurte',(4.6086085,-74.093938)),('el progreso',(4.60154165,-74.0934274491)),('paloquemao',(4.6130056,-74.0848628)),('avenida caracas',(4.6113248,-74.0750011)),('santa isabel',(4.6010941,-74.1019894)),('Ciudad Montes',(4.608375, -74.0864488926515))]
narino = [('tumaco',(1.8077554,-78.7705976)),('la fragua',(4.5945493,-74.10998325)),('caracas',(4.5832193,-74.0987529)),('ciudad jardín',(4.5819643,-74.0900354)),('santander',(4.5929258,-74.112862)),('nariño',(4.5862814,-74.0939387)),('san antonio',(4.5899204,-74.0950108705)),('restrepo',(4.5861242,-74.1011032)),('ciudad jardín sur',(4.5882529,-74.0974546)),('ciudad berna',(4.5821153,-74.0903097)),('villa mayor',(4.5903664,-74.1214658)),('avenida primero de mayo',(4.5758254,-74.0945425))]
uribe = [('mirador',(4.5980625,-74.0759424)),('marco fidel suarez',(4.5677117,-74.118317)),('la resurrección',(4.5692269,-74.110864)),('country sur',(4.5720564,-74.0980049)),('marruecos',(4.5535025,-74.1152536)),('claret',(4.5838662,-74.1276074)),('sosiego',(4.5755559,-74.0988094972)),('molinos',(4.5563733,-74.1215048)),('bochica',(4.5556928,-74.1161634)),('bosque de san carlos',(4.5726196,-74.1073112)),('gustavo restrepo',(4.5765292,-74.1057202)),('quiroga',(4.5767729,-74.1144585)),('inglés',(4.5843285,-74.1234496)),('rafael uribe',(4.5531636,-74.107622)),('san josé',(4.5761803,-74.1024457)),('molinos sur',(4.5551568,-74.1178297)),('socorro',(4.58315015,-74.1282378)),('olaya',(4.5786556,-74.1079469)),('la picota',(4.5486163,-74.1162850389)),('libertador',(4.5865315,-74.112592)),('santa lucia',(4.5707853,-74.1247515))]
tunjuelito = [('abraham lincom',(4.5575302,-74.123693)),('san vicente tunal',(4.5794657,-74.1395277)),('tunal antiguo',(4.575754,-74.1299851)),('el tunal',(4.5679605,-74.139738)),('san carlos',(4.5662527,-74.1312832)),('laguneta',(4.5939927,-74.1435182)),('isla del sol',(4.5895252,-74.1542267)),('fátima',(4.5871532,-74.1377259)),('el carmen',(4.5816468,-74.1354625)),('portal de santafe',(4.585673,-74.1428172)),('cordoba',(4.5766087,-74.1292345)),('autopista sur',(4.5943365,-74.1352015)),('tejar de ontario',(4.5781007,-74.1422522)),('la sevillana',(4.59428565,-74.144492621)),('tunjuelito',(4.5610488,-74.1275232)),('venecia',(4.59443518484,-74.1392049724)),('marcofidel suarez',(4.5694022,-74.1232622)),('san benito',(4.5636583,-74.1350441)),('san vicente ferrer',(4.5842135,-74.1413634)),('muzú',(4.5807211,-74.1424251)),('samore',(4.5821389,-74.1320499))]
candelaria = [('barrio la paz',(4.606787,-74.0646938)),('candelaria',(4.593925,-74.0713365)),('belen',(4.5911072,-74.0729648)),('ciudadela nueva santafe',(4.5930446,-74.0759694))]
santa_fe = [('santa fé',(4.5948029,-74.0337423)),('san bernardo',(4.59300205,-74.0852279733)),('ciudadela nueva santafe',(4.5930446,-74.0759694)),('las cruces',(4.5874534,-74.0792089)),('barrio la aguas',(4.6009295,-74.0672853)),('barrio la paz',(4.606787,-74.0646938)),('la roca',(4.5786144,-74.07671)),('el rocio',(4.5845017,-74.0709048)),('girardot',(4.5864054,-74.0749817)),('egipto',(4.5925455,-74.0685231))]
san_cristobal = [('la belleza',(4.5643537,-74.0833911732)),('vitelma',(4.5730799,-74.0778571)),('villa javier',(4.5802294,-74.0839008)),('20 de julio',(4.5707131,-74.0938906)),('santa ines',(4.5599874,-74.0842464)),('la y',(4.5486579,-74.0474728043)),('villas de los alpes',(4.5621798,-74.0984488)),('la victoria',(4.5536633,-74.0944089)),('la maría',(4.5775389,-74.0858478)),('las guacamayas',(4.5526478,-74.096995)),('villa de los alpes',(4.5588138,-74.0973154)),('suramérica',(4.5671851,-74.0945997)),('canadá',(4.5446259,-74.0989013)),('la gloria',(4.5715735,-74.0981993)),('bello horizonte',(4.5624472,-74.0925935)),('quindío',(4.5376389,-74.0826573)),('san blas',(4.5675019,-74.0857001)),('san cristóbal',(4.560513,-74.0625888)),('altamira',(4.5439421,-74.0890128)),('san isidro',(4.5649814,-74.1003158)),('las brisas',(4.5836462,-74.080668)),('granada sur',(4.5689053,-74.0871857))]
bolivar = [('madelena',(4.5938648,-74.1567923)),('calle 60b s',(4.5607297,-74.1365065)),('el espino',(4.5816454,-74.1790618)),('la coruña',(4.5782731,-74.152367)),('los alpes',(4.5432071,-74.1542879)),('candelaria la nueva',(4.5697519,-74.1503182)),('perdomo',(4.58666,-74.1678686)),('san francisco',(4.5625082,-74.1442181)),('arborizadora baja',(4.5731905,-74.1512004)),('monterrey',(4.5388435,-74.1339674)),('santa bibiana',(4.5751018,-74.1712503)),('la esperanza',(4.5349718,-74.1500178)),('gibraltar',(4.5562551,-74.1421214)),('republica del canada sur',(4.5324477,-74.1477433)),('lucero alto',(4.549945,-74.1477433)),('quiba',(4.5413034,-74.1406622)),('juan pablo ii',(4.5543727,-74.1480651)),('lucero bajo',(4.5522765,-74.1444602)),('kalamary',(4.5822477,-74.15911)),('diagonal 58 sur',(4.5942275,-74.181846)),('sierra morena',(4.5780929,-74.1687184)),('la isla',(4.5732675,-74.1822696)),('caracoli',(4.5732598,-74.1737929)),('el paraíso',(4.5503067,-74.158992)),('potosi',(4.5701156,-74.1710034)),('tres esquinas',(4.5733617,-74.1672379)),('arborizadora alta',(4.5674419,-74.1623989)),('jerusalén',(4.5705119,-74.1620454)),('bonavista',(4.5875974,-74.1625973)),('la estancia',(4.5915504,-74.1737302)),('brisas del volador',(4.5467793,-74.1553607)),('la estrella',(4.5449825,-74.1456833)),('ciudad bolivar',(4.5374953,-74.1527368)),('casalinda',(4.5695824,-74.1436738))]
usme = [('calle 133 sur',(4.4780551,-74.122568)),('el virrey',(4.4979427,-74.1122448)),('villa maria',(4.501836,-74.0905938)),('tihuaque',(4.5021366,-74.0831298)),('yomasa',(4.5076977,-74.1092842)),('comuneros',(4.4987914,-74.1084656)),('costa rica',(4.5262291,-74.1205773839)),('usminia',(4.4944976,-74.1173732)),('la aurora',(4.5253626,-74.121669)),('puerta al llano',(4.4878253,-74.1004018)),('casaloma',(4.5015853,-74.0988705)),('marichuela',(4.5123112,-74.1185824)),('santa marta',(4.5261598,-74.115663)),('danubio azul',(4.5404481,-74.1163105)),('usme',(4.4709337,-74.1253573)),('calle 138b',(4.4705196,-74.1277181)),('santa librada',(4.5174509,-74.1145419)),('las quintas',(4.52015425,-74.1228965459)),('juán josé rondón',(4.4990937,-74.0865839)),('chuniza',(4.5050767,-74.1101317)),('la cabaña',(4.5103961,-74.1089533)),('el uval',(4.4868247,-74.1037352))]
sumapaz = [('sumapaz',(4.0988002, -74.3415295))]
cundinamarca = [('junín',(4.7901837,-73.6631716)),('chaguaní',(4.949256,-74.5937869)),('zipacón',(4.7605894,-74.3802641)),('nimaima',(5.125392,-74.3853501)),('la vega',(5.0006956,-74.340005)),('chipaque',(4.4418869,-74.0440216)),('tabio',(4.9159164,-74.0981081)),('apulo',(4.520545,-74.5938264)),('el colegio',(4.5809252,-74.4416221)),('cundinamarca',(5.4560159,-74.1675856)),('albán',(4.8780617,-74.4384461)),('fusagasugá',(4.3369235,-74.3644853)),('gama',(4.7626787,-73.6107979)),('cota',(4.7797683,-74.1383982)),('cachipay',(4.730389,-74.4358942)),('cucunubá',(5.2502785,-73.7664624)),('paratebueno',(4.4817686,-73.1379024)),('guayabal',(4.5044273,-74.5100521)),('gachalá',(4.6931498,-73.5202944)),('gachetá',(4.8174862,-73.6371012)),('jerusalén',(4.5623901,-74.6942066)),('san rafael',(4.8650696,-74.3654276)),('pekín',(4.3523061,-74.3775677)),('choachí',(4.5288916,-73.9230789)),('nocaima',(5.0697197,-74.3774766)),('madrid',(4.7324758,-74.2567083)),('anolaima',(4.7616931,-74.4650093)),('agua de dios',(4.3766682,-74.6684565)),('villeta',(5.0112214,-74.4701579)),('rionegro',(5.2595722,-74.3662939)),('san francisco',(4.5940047,-73.9861139)),('soacha',(4.5777003,-74.2126179)),('novillero',(4.3654525,-73.9158152)),('tena',(4.6554712,-74.3893392)),('guayabal de síquima',(4.8782654,-74.4675634)),('simijaca',(5.5000667,-73.8645474)),('tibiritá',(5.0524582,-73.5046943)),('cajicá',(4.2983692,-74.2410544)),('sesquilé',(5.0665846,-73.8038352)),('manta',(5.0084071,-73.540458)),('funza',(4.7163036,-74.2122205)),('mosquera',(4.7050959,-74.2303984)),('cáqueza',(4.4039927,-73.947005)),('medina',(4.5883759,-73.382189)),('guasca',(4.8517214,-73.773727)),('villapinzón',(5.2171873,-73.5976301)),('nilo',(4.3065906,-74.6197607)),('cucharal',(5.1222062,-74.6251886)),('la palma',(5.3589384,-74.3909199)),('chía',(4.8610723,-74.060255)),('quetame',(4.331535,-73.86133)),('la calera',(4.7201219,-73.9689085)),('viotá',(4.4386903,-74.5233521)),('guataquí',(4.5514462,-74.7464108)),('fosca',(4.3392237,-73.9391743)),('ubaté',(5.311796,-73.8123753)),('tequendama',(4.6163301,-74.3520066)),('ubalá',(4.7444552,-73.5345919)),('anapoima',(4.5493011,-74.5359118)),('bituima',(4.8719178,-74.5385652)),('carmen de carupa',(5.3552343,-73.9049344)),('vianí',(4.87426,-74.5624054)),('tierra negra',(3.9490024,-74.3921338)),('ubaque',(4.4822948,-73.9349376)),('el triunfo',(4.5428529,-74.4736898)),('la mesa',(4.632082,-74.4615462)),('mesitas',(4.7555895,-73.4085794)),('sopó',(4.9083572,-73.9406714)),('tenjo',(4.8087533,-74.1388782)),('ricaurte',(4.3177714,-74.7580318)),('la isla',(4.5732675,-74.1822696)),('sibaté',(4.491155,-74.2605785)),('machetá',(5.0804789,-73.6077282)),('fómeque',(4.4863244,-73.8952524)),('santa lucía',(4.6101137,-74.5096219)),('batán',(4.7843637,-74.6435859)),('beltrán',(4.7993086,-74.7408058)),('facatativá',(4.8097329,-74.3541283)),('subachoque',(4.9289303,-74.1745005)),('los robles',(4.574333,-74.1769179)),('alcaparros',(4.6636339,-73.9765137167)),('el rosal',(4.8525377,-74.2605921)),('chia',(4.8610723,-74.060255)),('guavio',(4.792796,-73.3448194)),('bojacá',(4.732482,-74.3416741)),('sasaima',(4.9645773,-74.433115)),('antigua vía al guavio',(4.7647795,-74.0088857)),('san antonio',(4.6657124,-74.3334233)),('la aguadita',(4.3883444,-74.3248933)),('tocaima',(4.4579274,-74.6342233)),('la peña',(5.1976287,-74.3938006)),('quebradanegra',(5.1359731,-74.498505)),('zipaquirá',(5.0235578,-74.0032488)),('pulí',(4.6809255,-74.7135541)),('la puerta',(5.3057512,-74.5101955)),('guayabetal',(4.2375527,-73.8237947)),('mosqueral',(4.3246814,-74.383198)),('quipile',(4.7439107,-74.5336881)),('chocontá',(5.1459409,-73.6839511)),('junín',(4.7901837,-73.6631716)),('chaguaní',(4.949256,-74.5937869)),('zipacón',(4.7605894,-74.3802641)),('nimaima',(5.125392,-74.3853501)),('la vega',(5.0006956,-74.340005)),('chipaque',(4.4418869,-74.0440216)),('tabio',(4.9159164,-74.0981081)),('apulo',(4.520545,-74.5938264)),('el colegio',(4.5809252,-74.4416221)),('cundinamarca',(5.4560159,-74.1675856))]
others = [('venezuela',(8.0018709,-66.1109318)),('china',(35.000074,104.999927)),('perú',(-6.8699696,-75.0458514)),('siria',(34.6401861, 39.0494106)),('salhi',(38.2372178, 39.6632501)),('trujillo',(15.8224938, -85.9232509235649)),('parís',(48.8566101, 2.3514992)),('la habana',(23.1379911, -82.3658561)),('francia',(46.603354, 1.8883335)),('el río',(-22.9110136, -43.2093726)),('brasil',(-10.3333332, -53.1999999)),('américa',(-40.81750225,-63.0084845334))]
nbhlist = [suba,bosa,kennedy,fontibon,engativa,usaquen,unidos,teusaquillo,chapinero,aranda,martires,narino,uribe,tunjuelito,candelaria,santa_fe,san_cristobal,bolivar,usme,sumapaz,cundinamarca,others]
dict = {}
for nb in nbhlist:
	for f in nb:
		nbh = f[0].lower()
		l = []
		nbh = unicode(nbh, 'utf-8')
		lat = float(f[1][0])
		lon = float(f[1][1])
		l.append(lat)
		l.append(lon)
		dict[nbh] = l

suba1 = []
for f in suba:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	suba1.append(nbh)
bosa1 = []
for f in bosa:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	bosa1.append(nbh)
kennedy1 = []
for f in kennedy:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	kennedy1.append(nbh)
fontibon1 = []
for f in fontibon:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	fontibon1.append(nbh)
engativa1 = []
for f in engativa:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	engativa1.append(nbh)
usaquen1 = []
for f in usaquen:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	usaquen1.append(nbh)
unidos1 = []
for f in unidos:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	unidos1.append(nbh)
teusaquillo1 = []
for f in teusaquillo:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	teusaquillo1.append(nbh)
chapinero1 = []
for f in chapinero:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	chapinero1.append(nbh)
aranda1 = []
for f in aranda:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	aranda1.append(nbh)
martires1 = []
for f in martires:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	martires1.append(nbh)
narino1 = []
for f in narino:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	narino1.append(nbh)
uribe1 = []
for f in uribe:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	uribe1.append(nbh)
tunjuelito1 = []
for f in tunjuelito:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	tunjuelito1.append(nbh)
candelaria1 = []
for f in candelaria:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	candelaria1.append(nbh)
santa_fe1 = []
for f in santa_fe:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	santa_fe1.append(nbh)
san_cristobal1 = []
for f in san_cristobal:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	san_cristobal1.append(nbh)
bolivar1 = []
for f in bolivar:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	bolivar1.append(nbh)
usme1 = []
for f in usme:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	usme1.append(nbh)
sumapaz1 = []
for f in sumapaz:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	sumapaz1.append(nbh)
cundinamarca1 = []
for f in cundinamarca:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	cundinamarca1.append(nbh)
others1 = []
for f in others:
	nbh = f[0].lower()
	nbh = unicode(nbh, 'utf-8')
	others1.append(nbh)

a1 = suba1 
a2 =  bosa1+kennedy1+fontibon1+engativa1   #'bosa','Kennedy','Fontibón','Engativá'
a3 =  usaquen1+unidos1+teusaquillo1+chapinero1    #['Usaquén','Barrios Unidos','Teusaquillo','Chapinero']
a4 =  aranda1+martires1+narino1+uribe1+tunjuelito1+candelaria1+santa_fe1    #['Puente Aranda','Los Mártires','Antonio Nariño','Rafael Uribe','Tunjuelito','La Candelaria','Santa Fe']
a5 = 	san_cristobal1+bolivar1+usme1+sumapaz1		#['San Cristóbal','Ciudad Bolívar','Usme','Sumapaz']
a6 = 	cundinamarca1		#['Cundinamarca']
a7 = 	others1					#['others']
all = a1 + a2 + a3 + a4 + a5 + a6 + a7 
areadict = {1: a1, 2:a2, 3: a3, 4:a4, 5:a5, 6:a6, 7:a7}

def find_area(targetdir):
	#print targetdir
	for file in os.listdir(targetdir):
		if ((file!='a1trainR' ) and (file!='a2trainR') and (file!='a2trainR') and (file!='a4trainR') and (file!='a5trainR') and (file!='a6trainR') and (file!='a7trainR')):
			filename = os.path.join(targetdir, file)
			#print filename
			with open(filename) as f:
				dir1 =  os.path.join(os.getcwd(), 'a1trainR')
				fname1 = os.path.join(dir1, file)
				ff1 = open(fname1, 'a+')
				ff1.truncate()
				dir2 =  os.path.join(os.getcwd(), 'a2trainR')
				fname2 = os.path.join(dir2, file)
				ff2 = open(fname2, 'a+')
				ff2.truncate()
				dir3 =  os.path.join(os.getcwd(), 'a3trainR')
				fname3 = os.path.join(dir3, file) 
				ff3 = open(fname3, 'a+')
				ff3.truncate()
				dir4 =  os.path.join(os.getcwd(), 'a4trainR')
				fname4 = os.path.join(dir4, file)
				ff4 = open(fname4, 'a+')
				ff4.truncate()
				dir5 =  os.path.join(os.getcwd(), 'a5trainR')
				fname5 = os.path.join(dir5, file)
				ff5 = open(fname5, 'a+')
				ff5.truncate()
				dir6 =  os.path.join(os.getcwd(), 'a6trainR')
				fname6 = os.path.join(dir6, file) 
				ff6 = open(fname6, 'a+')
				ff6.truncate()
				dir7 =  os.path.join(os.getcwd(), 'a7trainR')
				fname7 = os.path.join(dir7, file)
				ff7 = open(fname7, 'a+')
				ff7.truncate()
				for line in f:
					if line:
						jsondata = line
						line = line.strip()
						areas, locations = [], []
						try:
							maindict = json.loads(jsondata)
							for key in maindict:
								if key == 'content_title':
									value = maindict[key]
									string = value.lstrip('\n').rstrip('\n').replace('\n', ' ')
									string = string.lower()
									for a in all:
										if a in string:
											areas.append(a)
								if key == 'Content' or key == 'content':
									value = maindict[key]
									string = value.lstrip('\n').rstrip('\n').replace('\n', ' ')
									string = string.lower()
									for a in all:
										if a in string:
											areas.append(a)
								if key == 'BasisEnrichment':
									value = maindict[key]
									entities = value.get('entities')
									for x in range(len(entities)):
										item = entities[x]
										for k in item:
											loc = 0
											if k == 'neType' and item[k] == 'LOCATION':
												#print k, item[k]
												loc = 1
											if loc == 1 and k == 'expr':
												itemval = item[k].lower()
												locations.append(itemval)
											locval = ''
											if k == 'neType' and item[k] == 'LOCATION':
												if locval:
													locval = locval.lower()
													locations.append(locval)
									if locations:
										for a in all:
											if a in locations:
												areas.append(a)
						except ValueError as e:
							print e, filename
							pass 
						dist = []
						for i in range(len(areas)):
							current = areas[i]
							current_sum = 0
							current_lats = (dict[current][0], dict[current][1])
							for t in areas:
								t_lats = (dict[t][0], dict[t][1])
								d = vincenty(current_lats, t_lats)
								current_sum += d
							dist.append(current_sum)
						minlist = []
						if dist:
							minindex = np.argmin(dist)
							minlist.append(minindex)
							min = np.min(dist)
						for i in range(len(dist)):
							if dist[i] == min:
								minlist.append(i)
						minlist = list(set(minlist))
						area = np.inf
						arealist = []
						if minlist:
							for key in areadict:
								items = areadict[key]
								for ind in minlist:
									if areas[ind] in items:
										arealist.append(key) 
										area = 1000
						if area == np.inf:
							ff7.write(line)
							ff7.write('\n')
						elif area == 1000:
							arealist = list(set(arealist))
							for r in arealist:
								if r == 1:
									ff1.write(line)
									ff1.write('\n')
								if r == 2:
									ff2.write(line)
									ff2.write('\n')
								if r == 3:
									ff3.write(line)
									ff3.write('\n')
								if r == 4:
									ff4.write(line)
									ff4.write('\n')
								if r == 5:
									ff5.write(line)
									ff5.write('\n')
								if r == 6:
									ff6.write(line)
									ff6.write('\n')
								if r == 7:
									ff7.write(line)
									ff7.write('\n')

def main():
	root = os.getcwd()
	targetdir = os.path.join(root, 'crimes-apr-to-oct-R')
	find_area(targetdir)
	
main()
