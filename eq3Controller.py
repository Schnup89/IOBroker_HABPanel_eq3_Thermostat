from eq3bt import Thermostat
import subprocess
import sys

# Zuordnung der BTLE MAC-Adressen der Geraete zu den Zimmer
aMacs = ['00:1A:22:xx:xx:xx', '00:1A:22:xx:xx:xx',  '00:1A:22:xx:xx:xx', '00:1A:22:xx:xx:xx']
aZimmer = ['Kueche', 'Buero', 'Wohnzimmer', 'Schlafzimmer']


# Script->IOBroker - Setze die Temp fuer den Raum im IOBroker 
def setIOTemp(sRoom, sTemp):
    command = 'iobroker state set javascript.0.Thermometer.' + str(sRoom) + '_Temp ' + str(sTemp)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

# Script->IOBroker - Setze die Ventilstellung fuer den Raum im IOBroker 
def setIOValve(sRoom, sValve):
    command = 'iobroker state set javascript.0.Thermometer.' + str(sRoom) + '_Valve ' + str(sValve)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

# Script->IOBroker - Setze den Batteriealarm fuer den Raum im IOBroker  
def setIOAlarm(sRoom, sAlarm):
    command = 'iobroker state set javascript.0.Thermometer.' + str(sRoom) + '_Alarm ' + str(sAlarm)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

# IOBroker->Script - Setze den Temperaturwert im Thermostat 
def setEQTemp(sMAC, sTemp):
    thermostat = Thermostat(sMAC)
    thermostat.target_temperature = float(sTemp)
    thermostat.update()

# Pruefe bei aufruf des Script die mitgegebenen Parameter
if len(sys.argv) > 1:
    # Mehr als 1 Parameter, dann setze Temp im Thermostat
    sZimmer = sys.argv[1]
    sTemp = sys.argv[2]
    nArrID = aZimmer.index(sZimmer)
    setEQTemp(aMacs[nArrID], sTemp)
else:
    # Kein Parameter, dann aktualisere Werte im IOBroker für jeden definierten Themostat
    for i in range(len(aMacs)):
        thermostat = Thermostat(aMacs[i])
        thermostat.update()
        # Wenn Mode Closed gesetzt am Thermostat, dann setzen wird Mode Manual (5 Grad), sonst gibts Probleme
        if str(thermostat.mode) == "Mode.Closed":
            print("setmode")
            thermostat.mode = 3
            thermostat.update()
        # Debug
        print(str(thermostat.mode) + " : " + str(thermostat.target_temperature) + " : " + str(thermostat.valve_state))
        # Setze Werte im IOBroker
        setIOTemp(aZimmer[i],thermostat.target_temperature)
        setIOValve(aZimmer[i],thermostat.valve_state)
        setIOAlarm(aZimmer[i],thermostat.low_battery)
