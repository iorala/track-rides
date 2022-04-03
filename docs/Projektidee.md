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
- Routen Analysieren / parsen 
	- Dauer -> banal
	- Distanz 
	- durchschnittliche HF
	- (durchschnittsgeschwindigkeit)
	- Routen als gleiche Routen festhalten? -> Manuell auswählen (warnung bei unterschiedlicher Länge)
		- Wie ist das möglich?
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

## Feedback zweites Tutoring
- Ich kann gerne mit einem Modul arbeiten
  - Nicht von hand mit 
- Ich muss das Modul einfach detailliert untersuchen:
  - Ist es sicher, malware. Code ansehen usw.
- Modul verwenden für das auslesen der Daten: berechnungen selbst durchführen 
- Zusammenfassungen im Datensatz speichern:
  - GPX-Blob jeder fahrt in Verzeichnis speichern: für spätere auswertung
  - Metadaten der Strecke neu Berechnen 
  - On The fly: Wenn inspiriert noch mit externen daten ergänzen (z.b. Wetter)
- Für jede Fahrt eine eigene Seite machen: 
  - Grafik mit Geschwindigkeit/Herzfrequenz/Höhenmeter/..?
  -> Datenasuwertung 
### Dokumentation
  - Readme kann hinweis auf Pythonversion und beschreibung der Module enthalten 
  - Es kann aber auch einfach auf das requirements.txt verweisene werden