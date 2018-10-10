# labo-3-ifttt-adafruit-io-raspi-samdesme

Maak een applicatie waarmee met de volgende flow:

* de gebruiker drukt op de IFTTT Do-button (Koppelingen naar een externe site.)Koppelingen naar een externe site.;
* de Adafruit IO (Koppelingen naar een externe site.)Koppelingen naar een externe site. gateway ontvangt de trigger en lanceert een MQTT-bericht;
* het MQTT-bericht wordt gecapteerd door de Raspberry Pi;
* de Raspberry Pi laat een bel rinkelen en de led-matrix laten flikkeren;
* de gebruiker drukt vervolgens op de drukknop van de Joystick;
* de reactietijd (tijd van reactie - tijd van inkomende aanvraag) wordt verstuurd naar een Adafruit IO feed;
* IFTTT reageert op wijzigingen in deze feed en stuurt vervolgens een e-mail bericht.