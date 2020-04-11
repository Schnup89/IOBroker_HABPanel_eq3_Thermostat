var tmrWohnzimmer = null;
var tmrSchlafzimmer = null;
var tmrKueche = null;
var tmrBuero = null;


/*******************************************************************************
 * Setze Thermostat-Werte  bei Änderung in HABPanel
 ******************************************************************************/

function fSetTemp(sRoom, sTemp) {
    exec('python3 /home/pi/eq3Controller.py ' + sRoom + ' ' + sTemp, function (error, stdout, stderr) { 
        log("Output: "+stdout); 
    }); 
}

//### Wir prüfen auf Änderung und warten 7 Sekunden ab bevor die Daten übertragen
//### So wird nicht für jede Änderung im VIS ein Befehl an den Thermostat geschickt
//### Befehl wird erst geschickt wenn 7 Sekunden keine Wertänderung stattgefunden hat
on({ id: "javascript.0.Thermometer.Wohnzimmer_Temp", change: 'ne'}, function(obj) {
    //Wenn Änderung des Objekts druch web.adapter
    if (obj.state.from == "system.adapter.web.0") {
        //Wenn Timer läuft, diesen zurücksetzen
        if(tmrWohnzimmer) {
            clearTimeout(tmrWohnzimmer);
        }
        //Timer starten 7 Sekunden
        tmrWohnzimmer = setTimeout(function(){
            //Wenn 7 Sekunden keine Änderung, dann Temperatur setzen
            fSetTemp('Wohnzimmer',obj.state.val);
            //Timer abschalten
            tmrWohnzimmer = null;
        }, 7000);
    }    
});

on({ id: "javascript.0.Thermometer.Schlafzimmer_Temp", change: 'ne'}, function(obj) {
    if (obj.state.from == "system.adapter.web.0") {
        if(tmrSchlafzimmer) {
            clearTimeout(tmrSchlafzimmer);
        }
        tmrSchlafzimmer = setTimeout(function(){
            fSetTemp('Schlafzimmer',obj.state.val);
            tmrSchlafzimmer = null;
        }, 7000);
    }    
});

on({ id: "javascript.0.Thermometer.Kueche_Temp", change: 'ne'}, function(obj) {
    if (obj.state.from == "system.adapter.web.0") {
        if(tmrKueche) {
            clearTimeout(tmrKueche);
        }
        tmrKueche = setTimeout(function(){
            fSetTemp('Kueche',obj.state.val);
            tmrKueche = null;
        }, 7000);
    }    
});

on({ id: "javascript.0.Thermometer.Buero_Temp", change: 'ne'}, function(obj) {
    if (obj.state.from == "system.adapter.web.0") {
        if(tmrBuero) {
            clearTimeout(tmrBuero);
        }
        tmrBuero = setTimeout(function(){
            fSetTemp('Buero',obj.state.val);
            tmrBuero = null;
        }, 7000);
    }    
});
