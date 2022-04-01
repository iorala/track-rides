# Projektidee Python 

- GPX files einlesen 
- networks 
- OSM am Schluss als eigener Teil

- Anzeige auf OpenStreetMap 
- Fokus auf Data Insight 

## Funktionen 
- Routen hochladen
- Metadaten versehen 
	- name, alleine usw. 
- Routen Analisieren / parsen 
	- Dauer -> banal
	- Distanz 
	- durchschnittliche HF
	- (durchschnittsgeschwindigkeit)
	- Routen als gleiche Routen festhalten? -> manuell auswählen (warnung)
		- WIe ist das möglich?
		- Stimmen nicht genau überein 


## Nutzen des Programms 
- Routen vergleichen 
	- WIe schnell 
	- Entwicklung über Zeit? -> Verbesserung, Tagesform 
	- Herzfrequenz 
	- Trainingsrouten nach Zeit suchen (ich habe eine Stunde, was kann ich fahren?)
	- -> Route Herunterladen und Fahren können (kann in ein Programm importiert werden


## Übersicht der Seiten 
- Main page
- Upload page 
- View Strecke 
 - Insight Fahrtenvergleich 
 - Bar-chart
- Search Page 
- Trainingstagebuch (mit zeitauswahl)

## Datenmodell
- Dictionary
	- Route X
		- GPX-Datei 
		- Distanz: (der Datei)
		- Zeit: (Durchschnitt aller Fahrten)
		- Zeit Min/Zeit max 
		- Fahrten
			- 2022_03_26_1
				- Streckenlänge
				- Dauer 
				- Durchschnittliche HF
			- 2022_03_26_2
				- Streckenlänge
				- Dauer 
				- Durchschnittliche HF


Alles = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}