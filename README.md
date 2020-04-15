# IOBroker_HABPanel_eq3_Thermostat

<img src="https://github.com/Schnup89/IOBroker_HABPanel_eq3_Thermostat/blob/master/eq3-panel.jpg?raw=true" width="30%">

Schritt für Schritt Anleitung um die EQ3-Thermostate via HabPanel, IOBroker und einem Raspberry PI zu steuern.
Die Habpanel Webseite kann dann von Smartphones sowie Laptop/PC's aufgerufen werden.

# Veraltet / Deprecated
# Es steht euch nun ein Adapter zur Verfügung

-> Stand heute, 15.04.2020 müsst ihr den Adapter manuell installieren, er ist noch nicht im offiziellen IOBroker repo zu finden.

-> "Adapters"-Seite im IOBroker öffnen, oben auf die GITHub-Katze klicken "Adapter aus beliebiger Quelle" und die URL einfügen

-> https://github.com/Schnup89/ioBroker.eq3-Thermostat

-> Ihr könnt von dieser Anleitung das HABPanel-Design übernehmen (Ab Punkt 5), ihr müsst nur die Item-ID im HabPanel anpassen.




## Voraussetzungen
Bitte bemüht Google um die Installation und Konfiguration folgender Systeme durchzuführen
- Raspberry PI mit Bluetooth
- IOBroker
- HABPanel (IOBroker-Adapter)
- Javscript (IOBroker-Adapter)

Hardware:
- EQ3 Thermostate Produktbeschreibung: https://www.eq-3.de/produkte/eqiva/detail/bluetooth-smart-heizkoerperthermostat.html


## 1. MAC-Adressen herausfinden

- per SSH auf den RPI-Verbinden
- EINEN Thermostat in der nähe des RPI starten
- expect installieren 

sudo apt install expect
- ** BTLE scan durchführen

sudo hcitool lescan
- Wenn alles passt, bekommt mein ein Gerät "CC-RT-BLE" mit einer MAC-Adresse angezeigt.
- MAC-Adresse und zukünftiger Raum des Thermostats notieren für später
- Für jeden Thermostat die Prozedur wiederholen ab **


## 2. Anlegen des Python Script für eq3-Thermostate und Zuweisung der MAC's

Basis zur Übertragung der Daten von/zu den Thermostaten ist eine Eq3 Python Library welche die Übertragung für uns übernimmt:
https://github.com/rytilahti/python-eq3bt

- Lib installieren

pip install python-eq3bt
- Die Datei eq3Controller.py aus dem Repository auf den RPI kopieren, z.B. wie bei mir unter /home/pi/
- In dieser Datei die MAC's und Räume anpassen (sollten in deinen Notizen von Schritt 1 stehen) :)

## 3. Objekte anlegen in IOBroker

- Unter den Objekten in IOBroker folgenden Ordner erstellen:

javascript.0.Thermometer.

https://github.com/Schnup89/IOBroker_HABPanel_eq3_Thermostat/blob/master/objekte.jpg

(( Fragt mich nicht warum ich Thermometer als Ordnername genommen habe, ich war Verwirrt :) ))


## 4. Javscript hinzufügen

- Legt ein neues Javascript-Script an und kopiert den Inhalt der Datei Thermostat_VIS.js in meinen Repository rein
- Passt die Namen der Räume an!!!
- Script starten


## 5. HABPanel Ansicht anlegen

- Ruft euer HABPanel auf und erstellt zwei Objekte, ein "template" und einen "knob" wie im Bild "HabPanel-Objects.png" zu sehen
- In das Template-Objekt kommt der Inhalt der Datei "Habpanel-Template" im Repository mit angepasstem Raumnamen!
- Meine Einstellungen für das "Knob"-Element:

__General__

Item: javascript.0.Thermometer.Wohnzimmer_Temp

Min: 5

Max: 29

Step: 0,5

Unit: °C

x Show Value

x Show Name

__Bar & Track__

Angles: Start 20, End 340

x Display previous value when dragging

__Misc.__

Font Size: 24

