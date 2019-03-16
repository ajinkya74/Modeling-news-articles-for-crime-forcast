# -*- coding: utf-8 -*-

import json
#import simplejson  # simplejson provides more descriptive error message
import os
import csv

ganglist1 = ['la oficina','pijarbey','díaz gonzález','orozco','vicente castaño','office of envigado','erpac','libertadores del vichada','bloque meta','nueva generación','los gaitanistas','renacer','los machos','los paisas','the black eagles','aguilas negras','los rastrojos','la familia michoacana','el chapo','la oficina','pijarbey','díaz gonzález','orozco','vicente castaño','office of envigado','erpac','libertadores del vichada','bloque meta','nueva generación','los gaitanistas','renacer','los machos','the black eagles','aguilas negras','la familia michoacana','el chapo','Los Angelitos','ERPAC','Gaitanistas','La Oficina de Envigado','Nueva Generación', 'Los Magníficos','Aguilas Negras','Black Eagles','AUC','United Self-Defense Forces of Colombia','Autodefensas Unidas de Colombia','Nueva Orteguaza','Autodefensas Gaitanistas de Colombia','Ejército Popular de Liberación','EPL','Clan del Golfo','Águilas Negras', 'Los Norteños El Parche', 'Los Tesos', 'Los Yiyos', 'Los Mongolitos', 'Los Jíbaros', 'Los Chamizo', 'Los Chamos','Los Vacasen','La Banda del Negro Orlando','Los Kits Los Daza','Los Paisas','Los Pájaros','El Turco','El Zarco','El Monedita','El Mono','Los Simpson','Los Monsalve','Los Parrado','Los Peluzas','Los Moros','Los Gomelos','Los Rusos','Los Destroyers','Los Nicos','Los Monos','Los Navajas','Los Cucarachos','Los Magníficos','Los Choquis','Los Pitufos','El Caballo','El Beto','Los Nazi','El Coronel','Libertadores del Vichada','Oficina de Envigado','El Flaco','Los Calvos','El Jinete','El Parche','Los Velozas','Los Vampiros','Los Cucarrones','Los Chéveres','Los Cocos','Los Rapados','Los Zepelines','Los Zorreros','Los Galletas','Los Gomelos','Los Puntilleros','Meta Bloc','Puntilla','Los Bollos','Los Daza','AGC','Clan Usuga','Urabeños','Clan del Golfo','Rastrojos','Los Chachos','Los Rapados','Los Norteños','Los Gusanos','Los Canecos','Los Tigres','Los Pablos','Los Paisas','El Caleño','Banda del Gallina','Los Tacheros-Emboladores','bacrim','Otoniel','Black Eagles','Las Águilas Negras',' Úsuga','Bloque Meta',' Los Machos','Renacer','Los Gaitanistas','Nueva Generación','Libertadores del Vichada','The Office of Envigado','Los Urabeños','Pandillas en Santa Isabel','Galán','Santa Matilde y Salazar Gómez','Pandillas en El Guavio','Los Laches y El Consuelo','Los Camellos','Los Chávez','Los Gatos','Los Diablos','Los Crespos','Los Camiones Chapulín','Los Romilocos','El Enano','Los Pecas','Los N.Ns','Los Motas','El Memín','El Vaca Juanito','La 59','La Pulga','El Zapatero Milthon','Los Brothers','Los Memos','Los Kikos']
nbhlist1 = ['Usaquén','Chapinero', 'Santafé','San Cristobal','Usme','Tunjuelito','Bosa','Kennedy','Fontibón','Engativá','Suba','Barrios Unidos','Teusaquillo','los Mártires','Antonio Nariño','Puente Aranda','La Candelaria','Rafael Uribe Uribe','Ciudad Bolívar']	
ldlist1 = ['Paseo los libertadores','Las ferias','El Refugio','Sagrado Corazón','San Blas','Verbenal','Minuto de Dios','San Isidro','La Macarena','Sosiego','La Uribe','Boyacá Real','Prdo Rubio','Las Nieves','20 de Julio','San Cristóbal','Santa Cecilia','Chico Lago','Las Cruces','Gloria','Toberín','Bolivia','Chapinero','Lourdes','Los Libertadores','Los Cedros','Garcés Navas','Usaquén','Engativa','Country Club','Jardín Botánico','Santa Bárbara','Alamos','La Flora','Venecia','Fontibón','Apogeo','Santa Isabel','Danubio','Tunjuelito','Fontibón San Pablo','Bosa occidental','La Sabana','Gran Yomasa','Zona Franca','Bosa central','Comuneros','Ciudad Salitre occidente','El Porvenir','Alfonso López','Granjas de techo','Tintal Sur','Parque Entrenubes','Modelia','Ciudad Usme','Capellanía','Aeropuerto El Dorado','Castilla','La Academia','Los Andes','Galenas','Ciudad Jardín','Américas','Guaymaral','Doce de Octubre','Teusaquillo','Restrepo','Carvajal','San José de Bavaria','Los Alcázares','Parque Simón Bolívar','Kennedy Central','Britalia','Parque Salitre','La Esmeralda','Timiza','El Prado','Quinta Paredes','Tintal Norte','La Alhambra','Ciudad Salitre Oriental','Calandaima','Casa Blanca Suba','Corabastos','Niza','Gran Britalia','La Floresta','Patio Bonito','Suba','Las Margaritas','El Rincón','Bavaria','Tibabuyes','Ciudad Montes','La Candelaria','San José','El Mochuelo','Muzú','Quiroga','Monteblanco','San Rafael','Marco Fidel Suárez','Arborizadota','Zona Industrial','Marruecos','San Francisco','Puente Aranda','Diana Turbay','Lucero','El Tesoro','Ismael Perdomo','Jerusalem','Usaquén','Chapinero','Santa Fe','San Cristóbal','Usme','Tunjuelito','Bosa','Kennedy','Fontibón','Engativá','Suba','Barrios Unidos','Teusaquillo','Los Mártires','Antonio Nariño','Puente Aranda',' 	La Candelaria','Rafael Uribe Uribe','Ciudad Bolívar','Sumapaz']
gmemlist1 = ['Vicente Castaño',' Ramón Navarro Serrano','Megateo', 'Ivan Marquez','Luis Enrique Calle Serna','Octavio Orrego','Sebastián','Carlos Andres Bustos Cortez','Jairo Alirio Puerta Peña','Cuñado','Omar', 'El Paisa', 'Rastrojos', 'Simon Trinidad','Puntilla','Tanja Nijmeijer', 'ERPAC', 'Don Berna','Don Mario','Pablo Beltran','Pastor Alape','Joaquin Gomez','Otoniel','Urabeños', "Daniel 'El Loco' Barrera", 'Fabian Ramirez','EPL','Los Pelusos','Aguilas Negras','Libertadores de Vichada','AGC','Gaitanista Self-Defense Forces of Colombia','Paisas','FIAC','Megateo','Salvatore Mancuso','Romaña','Oficina de Envigado','Pablo Escobar','Franco Jiménez','German','Nicolas Rodriguez Bautista','Gabino','Eliecer Erlinto Chamorro','Antonio Garcia','Miguel Ángel Alfaro','Dámaso López Núñez','Luciano Marin Arango','Ivan Marquez','Cesarin','Roberto Vargas Gutierrez','Gavilan','Fredy Alonzo Mira Perez','Fredy Colas','Licenciado','Jorge 40','Movil 7','Timochenko','Pablito','Abimel Coneo Martínez','Torta','Carlos Marin Guarin','Antonio Garcia','Pablo Beltrán','Gabino','Calle Serna','Pijarbey','Martin Farfan Diaz Gonzalez','Comba','Otoniel','Martín Farfán Díaz González','Pijarbey','Díaz González','Dairo Antonio Úsuga David','Mao','Guillermo Alejandro','Dario Antonio Usuga','Raul Jaramillo','Abeja','Efrain Guzman',' Nariño','Iván Marquéz','Mauricio Jaramillo','El Médico','Pablo Catatumbo','Timoleón Jiménez','Juaquin Gomez','Blanco','Escobar','Orejuela','Úsuga']
newnbh = ['Antioquia','Meta','Envigado','Arauca','Guaviare','Vichada','Valle del Cauca','Sucre','Cqueta','Huila','Putumayo','Quindio','Risaralda','Tolima','Boyaca','Santander','Norte de Santander','Buenaventura','Magdalena','Caquetá','Vichada','Guaviare','Casanare','Uraba','Cordoba','Guajira','Bolivar','Sucre','Cesar','Cauca','Chocó','Tumaco','Nariño']
general1 = []
nbhlist2 = nbhlist1 + ldlist1

ganglist = []
nbhlist = []
gmemlist = []

for word in ganglist1:
	word = word.lower()
	ganglist.append(unicode(word, 'utf-8'))
for word in nbhlist2:
	word = word.lower()
	nbhlist.append(unicode(word, 'utf-8'))
for word in gmemlist1:
	word = word.lower()
	gmemlist.append(unicode(word, 'utf-8'))

excel_nbh = []
excelfile = 'homicide_2015_nbh_muni_date_homicidios.csv' 
with open(excelfile) as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:
		if row[0] == 'BOGOTA DC (CT)':
			excel_nbh.append(row[1])
			
excel_nbh = list(set(excel_nbh))

nbh_excel = []
for word in excel_nbh:
	word = word.lower()
	nbh_excel.append(word.decode('latin-1'))

fontibon1=['Fontibón','Capellanía','Puente Grande','Flandes','Saturno','San Pablo','Versalles','La Palestina','La Laguna','Modelia','Villas de Madrigal'
'Ciudad Salitre']
fontibon = []
for nbh in fontibon1:
	nbh = nbh.lower()
	fontibon.append(unicode(nbh, 'utf-8'))	
fontibon = list(set(fontibon))
suba1 = ['Suba','Calle 187','Aures','El Rincón','Pinares','Lisboa','Prado Veraniego','Suba Reservado','La Alambra','Campania','Calle 169','Nueva Tibabuyes',
'Beamonte','Salamanca y Catalayud','manzana 13','Bilbao','San Jorge','Manuel Mejia','Punta del este','Transversal 126','Siberia','Niza','Las Villas','Bulevar',
'Andes','La Floresta','Puente Largo','Pontevedra','Santa Rosa','San Nicolás', 'Morato', 'La Alhambra', 'Malibú', 'Recreo de los Frayles', 'Batán', 'Niza', 
'Córdoba', 'Las Villas', 'Calatrava', 'Casablanca', 'Colina Campestre', 'Prado Veraniego and Mazurén', 'San José de Bavaria', 'Britalia', 
'Del Monte', 'Granada Norte', 'Villa del Prado', 'Nueva Zelandia', 'Santa Catalina', 'Mirandela', 'Vilanova', 'Guicaní','San Pedro','La Campiña', 'Pinares', 
'Tuna baja', 'La pradera', 'Nuevo Suba', 'Alcaparros', 'Cataluña', 'Costa Azul', 'Lagos de Suba', 'Corinto','El Laguito Villa Maria', 
'La Chucua Norte', 'El Rosal de Suba', 'El Rincón', 'El Rubí', 'Bilbao', 'Fontanar del Río', 'La Gaitana', 'Tibabuyes', 'Lisboa', 'Berlín','Villa Cindy', 
'Sabana de Tibabuyes']
suba = []
for nbh in suba1:
	nbh = nbh.lower()
	suba.append(unicode(nbh, 'utf-8'))
suba = list(set(suba))
bosa1=['bosa','Pôrtal del porvenir','La Capilla','Brasilia','Calle 59C Sur','Nuevo Chile','Laureles','Atalayas','Calle 51C S','Carrera 81I',
'Bosa la Esperanza','Kasay','El Recreo','Recreo Reservad','Alameda del Parque','Parques de Villa Javier','Alameda el Porvenir', 'El Jardín','Bosa Islandia',
'Bosa San Diego','Getsemaní','Calle 54 BIS S','Calle 69B Sur','Portal del Sol','Transversal 77J', 'La Libertad', 'Palestina', 'Bosa Brasil', 
'Bosa La Independencia', 'Piamonte', 'Jiménez De Quesada', 'Despensa','La Estación', 'La Azucena', 'La Amistad', 'El Motorista', 'Antonia Santos', 
'Naranjos', 'Olarte']
bosa = []
for nbh in bosa1:
	nbh = nbh.lower()
	bosa.append(unicode(nbh, 'utf-8'))	
bosa = list(set(bosa))
kennedy1=['Kennedy','Tintalá','calle 12','Marsella','Patio Bonito','Parques de Castilla','Casablanca','Carvajal','Lucerna','Ciudad Kennedy','Abastos'
'Britalia','Boita','Banderas','Tintal','Pio X','Manuel Mejia','Maria Paz','Timiza','calle 9B S','Quintas de Castilla','Argelia','Villa Claudia','Floralia',
 'Castilla', 'Ciudad Roma', 'Ciudad Kennedy', 'Timiza', 'Patio Bonito', 'Alquería', 'Britalia', 'Tintal', 'Class', 'El Rubí', 'Mandalay', 'La Fragua', 
 'Villa Alsacia', 'El Carmelo', 'Casablanca', 'Villa Andrea', 'Alfonso Lopez', 'Villas de Kennedy', 'El Gran Colombiano', 'Techo', 'Villa Claudia', 
 'El Socorro and Tintalito']
kennedy = []
for nbh in kennedy1:
	nbh = nbh.lower()
	kennedy.append(unicode(nbh, 'utf-8'))	
kennedy = list(set(kennedy))
engativa1=['Engativá','Calle 86','Bochica','Tabora','Villas del Dorado','El Mirador','Conjunto Florida de la Sabana','Metrópolis','Normandía','La Florida'
'La Granja','Bonanza','Las Ferias','Avenida Ciudad de Cali','Minuto de Dios','Villas de Granada','Villas de Madrigal','Garces Navas','Minuto de Dios',
'Quirigua','La Clarita','Ciudadela Colsubsidio','Normandía']
engativa = []
for nbh in engativa1:
	nbh = nbh.lower()
	engativa.append(unicode(nbh, 'utf-8'))	
engativa = list(set(engativa))
usaquen1= ['Usaquén','Tibabita','Bosque del Marqués','Capri','Santa Ana','San Antonio I','Las Orquídeas','Lijacá','Quintas del Redil','Canteras',
'La Ermita','Verbenal','El Otoño', 'Lijacá', 'Verbenal', 'San Antonio', 'Servitá', 'San Cristóbal Norte', 'Toberín', 
'Barrancas', 'Cedritos', 'Bella Suiza', 'La Carolina', 'Santa Ana', 'Santa Barbara', 'San Gabriel Norte', 'Cantón Norte', 'Francisco Miranda', 
'Las Margaritas', 'San Patricio']
usaquen = []
for nbh in usaquen1:
	nbh = nbh.lower()
	usaquen.append(unicode(nbh, 'utf-8'))	
usaquen = list(set(usaquen))
barrios_unidos1= ['Barrios Unidos','Siete de Agosto','Jorge Eliecer Gaitan','Parque Central Salitre Etapa 1','Calle 64','Entre Ríos','calle 75','Los Andes',
'Villa Calasanz', 'Entre Ríos', 'La Castellana', 'La Patria', 'Los Andes', 'Rionegro', 'Urbanización San Martín y Vizcaya','Doce de Octubre',
'Jorge Eliécer Gaitán', 'José Joaquín Vargas', 'La Libertad', 'Rincón Del Salitre', 'El Labrador', 'Metrópolis','Modelo Norte', 
'San Fernando', 'San Miguel y Simón Bolívar','Los Alcazares','11 De Noviembre', 'Alcázares Norte', 'Baquero', 'Benjamín Herrera', 
'Chapinero Noroccidental', 'Concepción Norte', 'Juan XXIII Norte', 'La Aurora', 'La Esperanza', 'La Merced Norte', 'La Paz', 
'Muequetá', 'Polo Club', 'Quinta Mutis', 'Rafael Uribe Uribe', 'San Felipe', 'Santa Sofía y Siete De Agosto','Parque El Salitre', 'El Rosario']
barrios_unidos = []
for nbh in barrios_unidos1:
	nbh = nbh.lower()
	barrios_unidos.append(unicode(nbh, 'utf-8'))	
barrios_unidos = list(set(barrios_unidos))
teusaquillo1= ['Teusaquillo','Galerías','Pablo VI','Calle 45A','Salitre Oriental','La Magdalena', 'La Soledad', 'Cundinamarca', 'Palermo', 'Marly',
'El Campín', 'Nuevo Campín', 'Quesada', 'Belalcázar', 'Nicolás de Federman', 'Rafael Nuñez', 'Ciudad Universitaria', 'Acevedo Tejada', 'Quinta Paredes', 
'Centro Antonio Nariño', 'La Esmeralda', 'Pablo VI', 'Quirinal', 'San Luis', 'Simón Bolívar', 'Ortezal', 'Camavieja', 'Ciudad Salitre Oriental y CAN']
teusaquillo = []
for nbh in teusaquillo1:
	nbh = nbh.lower()
	teusaquillo.append(unicode(nbh, 'utf-8'))	
teusaquillo = list(set(teusaquillo))
chapinero1=['Chapinero','Mariscal Sucre','Casaloma','Calle 57','San Luis','El Nogal','El Chicó', 'Antiguo Country', 'Rosales', 
'Villa del Cerro', 'Chapinero Central', 'Chapinero Alto', 'La Cabrera', 'El Lago', 'El Virrey', 'Quinta Camacho', 'Pardo Rubio', 'Marly', 'La Salle', 
'Bosque Calderón', 'La Porciúncula']
chapinero = []
for nbh in chapinero1:
	nbh = nbh.lower()
	chapinero.append(unicode(nbh, 'utf-8'))	
chapinero = list(set(chapinero))
puente_aranda1=['PUENTE ARANDA','Torcoroma','Milenta 3','Trinidad','La Pradera','Villa Sonia','Americas 68','Sonora','Veraguas','Milenta','Calle 1F',
'Alcalá','Tibana', 'Pensilvania', 'Comuneros', 'Primavera', 'El Jazmín', 'Jorge Gaitán Cortés', 'Santa Matilde', 'Ciudad Montes', 
'La Guaca', 'El Remanso', 'La Ponderosa', 'La Alquería', 'La Coruña', 'Ospina Pérez', 'Muzu', 'Galán', 'La Asunción', 'Bochica Sur', 'Pradera, Milenta', 
'Trinidad Galán', 'La Igualdad', 'San Rafael', 'San Rafael Industrial', 'Salazár Gómez', 'Veraguas', 'Veraguas Central', 'Gorgonzola', 'La Camelia', 
'Tejar','Santa Rita', 'Vosconia', 'Torremolinos', 'El Ejido', 'Santa Isabel', 'Colón', 'San Gabriel','Sorrento']
puente_aranda = []
for nbh in puente_aranda1:
	nbh = nbh.lower()
	puente_aranda.append(unicode(nbh, 'utf-8'))	
puente_aranda = list(set(puente_aranda))
los_martires1= ['Los Mártires','Santa Isabel','El Progreso','Ricaurte','Avenida Caracas','Santa Isabel', 'Ciudad Montes','Paloquemao']
los_martires = []
for nbh in los_martires1:
	nbh = nbh.lower()
	los_martires.append(unicode(nbh, 'utf-8'))	
los_martires = list(set(los_martires))
antonio_narino1= ['Antonio Nariño','Restrepo','Ciudad Jardín Sur','Avenida Primero de Mayo','Santander', 'Nariño','Pasto',
'Policarpa Salavarrieta', 'Luna Park', 'Villa Mayor', 'Eduardo Freí', 'San Antonio', 'Caracas', 'Ciudad Berna', 'Ciudad Jardín', 'La Fragua']
antonio_narino = []
for nbh in antonio_narino1:
	nbh = nbh.lower()
	antonio_narino.append(unicode(nbh, 'utf-8'))	
antonio_narino = list(set(antonio_narino))
cundinamarca1= ['Cundinamarca','Antigua vía al Guavio','Soacha', 'Fusagasugá', 'Girardot', 'Facatativá', 'Zipaquirá','Chia','Los Robles', 
'San Rafael', 'La Aguadita', 'Bermajal', 'Tierra Negra', 'Parte Piamonte', 'Parte Usatama','El Jordán', 'La Palma', 'Pekín', 'Sauces', 'Bethel', 'Mosqueral', 
'La Venta','El Placer', 'Espinalito', 'Sardinas', 'La Isla', 'Mesitas', 'Palacios', 'Bochica', 'Guayabal', 'Batán', 'Guavio', 'Santa Lucía', 'El Carmen',
'San Antonio', 'Santa María', 'La Puerta', 'El Triunfo','Parte De Usatama', 'Parte Piamonte', 'Bosachoque', 'El Resguardo', 'Cucharal', 'La Venta', 
'Novillero', 'Viena','Mosquera','Funza','Cajicá','Almeidas','Chocontá','Machetá','Manta','Sesquilé','Suesca','Tibiritá','Villapinzón','Agua de Dios','Guataquí',
'Jerusalén','Nilo','Ricaurte','Tocaima','Albán','La Peña','La Vega','Nimaima','Nocaima','Quebradanegra','San Francisco','Sasaima','Supatá','Útica','Vergara',
'Villeta','La Calera','Gachalá','Gachetá','Gama','Guasca','Guatavita','Junín','Ubalá','Beltrán','Bituima','Chaguaní','Guayabal de Síquima','Pulí',
'San Juan de Rioseco','Vianí','Medina','Paratebueno','Cáqueza','Chipaque','Choachí','Fómeque','Fosca','Guayabetal','Gutiérrez','Quetame','Ubaque','Une','Rionegro',
'Guavio','Gualivá','Cajicá','Cogua','Cota','Chía','Gachancipá','Nemocón','Sopó','Tabio','Tenjo','Tocancipá','Zipaquirá','Bojacá','Facatativá','Funza','Madrid',
'Mosquera','El Rosal','Subachoque','Zipacón','Soacha','Sibaté','Tequendama','Anapoima','Anolaima','Apulo','Cachipay','El Colegio','La Mesa','Quipile','Tena',
'Viotá','Ubaté','Carmen de Carupa','Cucunubá','Fúquene','Guachetá','Lenguazaque','Simijaca','Susa','Sutatausa','Tausa','alcaparros','la alambra']
cundinamarca = []
for nbh in cundinamarca1:
	nbh = nbh.lower()
	cundinamarca.append(unicode(nbh, 'utf-8'))	
cundinamarca = list(set(cundinamarca))
rafael_uribe1=['Rafael Uribe','Libertador','Molinos de Milenio','Olaya','San José','Sosiego Sur','La Picota', 'Quiroga', 'Diana Turbay', 'Molinos', 
'Libertador', 'Olaya', 'Gustavo Restrepo', 'Santa Lucia', 'Inglés', 'La Resurrección', 'Sosiego', 'Claret', 'San Jorge', 'Marco Fidel Suarez', 'El Pesebre', 
'Río de Janeiro', 'Las Colinas', 'Luis López de MMeza', 'Terrazas de San Jorge', 'Molinos Sur', 'Bochica', 'Marruecos', 'Socorro', 'Puerto Rico', 'Pijaos', 
'Las Lomas', 'Mirador', 'Bosque de San Carlos','Country Sur', 'Los Pinos', 'Libertadores']
rafael_uribe = []
for nbh in rafael_uribe1:
	nbh = nbh.lower()
	rafael_uribe.append(unicode(nbh, 'utf-8'))	
rafael_uribe = list(set(rafael_uribe))
tunjuelito1=['Tunjuelito','Tejar de Ontario','Cordoba','Tunal Antiguo','Marcofidel Suarez','Autopista Sur','Laguneta','Samore','Portal de Santafe',
'ABRAHAM LINCOM','SAN BENITO','San Carlos','Fatima','El Carmen','San Vicente Tunal','San Vicente Ferrer','Autopista Sur','El Tunal', 'San Benito', 
'San Vicente Ferrer', 'Fátima', 'El Carmen', 'San Carlos', 'Muzú', 'Venecia', 'Isla del Sol','La Sevillana']
tunjuelito = []
for nbh in tunjuelito1:
	nbh = nbh.lower()
	tunjuelito.append(unicode(nbh, 'utf-8'))	
tunjuelito = list(set(tunjuelito))
la_candelaria1= ['La Candelaria','Candelaria','Belen','Ciudadela Nueva Santafe','Barrio La Paz']
la_candelaria = []
for nbh in la_candelaria1:
	nbh = nbh.lower()
	la_candelaria.append(unicode(nbh, 'utf-8'))	
la_candelaria = list(set(la_candelaria))
santa_fe1=['Santa Fé','Las Cruces','Barrio La Aguas','Barrio La Paz','Egipto','El Rocio','La Roca','San Bernardo','Ciudadela Nueva Santafe','Las Brisas',
'Girardot']
santa_fe = []
for nbh in santa_fe1:
	nbh = nbh.lower()
	santa_fe.append(unicode(nbh, 'utf-8'))	
santa_fe = list(set(santa_fe))
san_cristobal1=['San Cristóbal','altamira','La Y','Bello Horizonte','San Blas','Las Guacamayas','20 de Julio','Santa Ines','Villas de los Alpes',
'Vitelma','San Isidro','Las Brisas','Villa Javier','Barcelona', 'Columnas', 'Corinto', 'La Castaña', 'La Gran Colombia', 'La María', 'Montecarlo', 'Quinta Ramos',
'San Pedro', 'Aguas Claras', 'La Belleza', 'Buenos Aires', 'Canadá', 'El Triángulo', 'Granada Sur', 'Juan Rey', 'La Victoria', 'Las Mercedes', 'Los Alpes', 
'Los Libertadores', 'Malvinas', 'Nariño Sur', 'Los Pinares', 'Quindío', 'Ramajal', 'Sagrada Familia', 'San Blas', 'San Isidro', 'San José Sur Oriental', 
'Santa Inés Sur Oriental', 'Sociego', 'Suramérica', 'La Gloria', 'Veinte de Julio', 'Villa de los Alpes', 'Villa Javier', 'Vitelma']
san_cristobal = []
for nbh in san_cristobal1:
	nbh = nbh.lower()
	san_cristobal.append(unicode(nbh, 'utf-8'))	
san_cristobal = list(set(san_cristobal))
ciudad_bolivar1=['Ciudad Bolivar','Quiba','Candelaria la Nueva','Juan Pablo II','Brisas del Volador','Arborizadora Alta','Jerusalén','Lucero Bajo',
'Republica del Canada Sur','Perdomo','La Estancia','Gibraltar','Los Alpes','Tres Esquinas','La Coruña','Caracoli','La Estrella','Perdomo','Potosi',
'La Esperanza','Sierra Morena','Bonavista','Monterrey','San Francisco','Lucero Alto','Casalinda','Kalamary','Arborizadora Baja','Casalinda','El Espino',
'Madelena','calle 60B S','Diagonal 58 Sur','Santa Bibiana','La Estrella', 'El Paraíso', 'Lucero Alto', 'San Joaquín', 'Sierra Morena', 'San Francisco', 
'Perdomo', 'Madelena', 'La Isla', 'Alto de La Cruz', 'Minuto de María', 'Francisco Pizarro']
ciudad_bolivar = []
for nbh in ciudad_bolivar1:
	nbh = nbh.lower()
	ciudad_bolivar.append(unicode(nbh, 'utf-8'))	
ciudad_bolivar = list(set(ciudad_bolivar))
usme1= ['Usme','Santa Marta','Usminia','Calle 133 Sur','Juán José Rondón','Barrio La Aguas','Calle 138B','Danubio Azul','Casaloma','El Virrey',
'Villa Maria','El Uval','Tihuaque','Yomasa', 'El Uval', 'Monte Blanco', 'Santa Librada', 'Chiguaza', 'El Virrey', 'Chuniza', 'Puerta al Llano', 
'Usminia', 'La Aurora', 'Marichuela', 'Sauces Miravalle', 'Santa Marta', 'Barranquillita', 'San Andres de los Altos', 'Costa Rica', 'Villa Isabel', 
'Las Quintas', 'La Cabaña', 'Betania', 'Danubio Azul', 'La Fiscala', 'Chuniza', 'Lorenzo Alcantuz', 'Comuneros', 'La Requilina', 'Serranias']
usme = []
for nbh in usme1:
	nbh = nbh.lower()
	usme.append(unicode(nbh, 'utf-8'))	
usme = list(set(usme))
sumapaz1 = ['sumapaz']
sumapaz = []
for nbh in sumapaz1:
	nbh = nbh.lower()
	sumapaz.append(unicode(nbh, 'utf-8'))	
sumapaz = list(set(sumapaz))
all = fontibon+suba+bosa+kennedy+engativa+usaquen+barrios_unidos+teusaquillo+chapinero+puente_aranda+los_martires+antonio_narino+cundinamarca+rafael_uribe+tunjuelito+la_candelaria+santa_fe+san_cristobal+ciudad_bolivar+usme+sumapaz
#print type(all)
all = list(set(all))
dict = {}

root = os.getcwd()
targetdir = os.path.join(root, 'crimes-apr-to-jan-R') 

for file in os.listdir(targetdir):
	linecount = 0
	filename = os.path.join(targetdir, file)
	with open(filename) as f:
		for line in f:
			linecount += 1
			found = 0
			line = line.strip()
			glist, nlist, entlist, gmlist, exnbhlist = [], [], [], [], []
			entitydict = {}
			entry = ' '
			if line:
				jsondata = line
				try:
					maindict = json.loads(jsondata)
					for key in maindict:
						entry = filename[-19:]
						x = linecount
						entry = entry + '_' + str(x)
						if key == 'content_title':
							value = maindict[key]
							title = value.lower()
							for gang in ganglist:
								if gang in title:
									found = 1
									glist.append(gang)
							for nbh in all:
								if nbh in title:
									nlist.append(nbh)
							for gmem in gmemlist:
								if gmem in title:
									found = 1
									gmlist.append(gmem)
							for exnbh in nbh_excel:
								if exnbh in title:
									exnbhlist.append(exnbh)
						if key == 'Content' or key == 'content':
							value = maindict[key]
							string = value.lstrip('\n').rstrip('\n').replace('\n', ' ')
							string = string.lower()
							for gang in ganglist:
								if gang in string:
									found = 1
									glist.append(gang)
							for nbh in all:
								if nbh in string:
									nlist.append(nbh)
							for gmem in gmemlist:
								if gmem in string:
									found = 1
									gmlist.append(gmem)
							for exnbh in nbh_excel:
								if exnbh in string:
									exnbhlist.append(exnbh)
						if key == 'BasisEnrichment':
							value = maindict[key]
							entities = value.get('entities')
							for x in range(len(entities)):
								org = 0
								person = 0
								loc = 0
								item = entities[x]
								for k in item:
									if k == 'neType' and item[k] == 'ORGANIZATION':
										org = 1
									if org == 1 and k == 'expr':
										itemval = item[k].lower()
										if itemval in entitydict:
											entitydict[itemval] += 1
										else:
											entitydict[itemval] = 0
											entitydict[itemval] += 1
									if k == 'neType' and item[k] == 'LOCATION':
										loc = 1
									if loc == 1 and k == 'expr':
										itemval = item[k].lower()
										if itemval in entitydict:
											entitydict[itemval] += 1
										else:
											entitydict[itemval] = 0
											entitydict[itemval] += 1
									if k == 'neType' and item[k] == 'PERSON':
										#print k, item[k]
										person = 1
									if person == 1 and k == 'expr':
										itemval = item[k].lower()
										if itemval in entitydict:
											entitydict[itemval] += 1
										else:
											entitydict[itemval] = 0
											entitydict[itemval] += 1
									orgval = ''
									if k == 'expr':
										orgval = item[k]
									if k == 'neType' and item[k] == 'ORGANIZATION':
										if orgval:
											orgval = orgval.lower()
											if orgval in entitydict:
												entitydict[orgval] += 1
											else:
												entitydict[orgval] = 0
												entitydict[orgval] += 1
									locval = ''
									if k == 'expr':
										locval = item[k]
									if k == 'neType' and item[k] == 'LOCATION':
										if locval:
											locval = locval.lower()
											if locval in entitydict:
												entitydict[locval] += 1
											else:
												entitydict[locval] = 0
												entitydict[locval] += 1
									pval = ''
									if k == 'expr':
										pval = item[k]
									if k == 'neType' and item[k] == 'PERSON':
										if pval:
											pval = pval.lower()
											if pval in entitydict:
												entitydict[pval] += 1
											else:
												entitydict[pval] = 0
												entitydict[pval] += 1
							for key, val in entitydict.items():
								#if val > 2:
								st = key + ':'+str(val)
								entlist.append(st)
				except ValueError as e:
					print e, filename
					pass
			glist = list(set(glist))
			nlist = list(set(nlist))
			entlist = list(set(entlist))
			gmlist = list(set(gmlist))
			exnbhlist = list(set(exnbhlist))
			glen = len(glist)
			nlen = len(nlist):
			if found == 1:
				newdict = {'gang':glist, 'nbh':nlist, 'gmem':gmlist, 'entities':entlist, 'exnbh': exnbhlist}
				dict[entry] = newdict
					

gfile = open('Ncrime-gangs-crimes-apr-to-jan-R.txt', 'a+')
gfile.truncate()
nfile = open('Ncrime-nbh-crimes-apr-to-jan-R.txt', 'a+')
nfile.truncate()
entfile = open('Ncrime-entities-crimes-apr-to-jan-R.txt', 'a+')
entfile.truncate()
gmfile = open('Ncrime-gangmems-crimes-apr-to-jan-R.txt', 'a+')
gmfile.truncate()
exnbhfile = open('Ncrime-excel-crimes-apr-to-jan-R.txt', 'a+')
exnbhfile.truncate()

for key in dict:
	val = dict[key]
	for k in val:
		if k == 'gang':
			v = val[k]
			if v:
				for name in v:
					gfile.write(name.encode('utf-8'))
					gfile.write('\n')
		if  k == 'nbh':
			v = val[k]
			if v:
				for name in v:
					nfile.write(name.encode('utf-8'))
					nfile.write('\n')
		if k == 'entities':
			v = val[k]
			if v:
				for name in v:
					name = name[:-2]
					entfile.write(name.encode('utf-8'))
					entfile.write('\n')
		if k == 'gmem':
			v = val[k]
			if v:
				for name in v:
					gmfile.write(name.encode('utf-8'))
					gmfile.write('\n')
		if k == 'exnbh':
			v = val[k]
			if v:
				for name in v:
					exnbhfile.write(name.encode('utf-8'))
					exnbhfile.write('\n')

gfile.close()
nfile.close()
entfile.close()
gmfile.close()
exnbhfile.close()




