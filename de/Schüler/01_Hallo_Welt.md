# Hallo Welt!

Jeder Programmierer, der sich an eine neue Computersprache wagt fängt mit diesen Zeile Code an, um seine Computer "Hallo Welt!" sagen zu lassen. Falls es nicht schon (oder noch) offen ist, starte Mu und gib Folgendes ein:

```python
from microbit import *
display.scroll("Hallo Welt!")
```

Diese zwei Zeilen Code sagen Deinem micro:bit Folgendes:
1. Zeile: Du sagst ihm, dass Du alles aus dem Modul microbit benutzen möchtest (ein Modul ist so eine Art Bibliothek mit bereits existierendem Code)
2. Zeile: Du sagst dem micro:bit, dass er sein Display (die 5 x 5 LEDs) benutzen soll, um eine Nachricht als eine Art Laufband (scroll) anzuzeigen; die Nachricht lautet *Hallo Welt!*

## Übungen

1. Kopiere den Code in den Mu Editor und lade (flashe) ihn auf Dein micro:bit. *Tipp:* Benutze das **Flash** Icon:

![Flash button](../../images/flash_button.png)

2. Ändere die Nachricht! Kannst Du ihm sagen, dass er Deine Klasse grüßen soll? *Tipp:* Du musst das Argument der `scroll` Methode ändern.

### ACHTUNG!

Es könnte schief gehen. Normalerweise ist das kein Problem. Eigentlich ist das der Punkt, an dem der echte Spaß beginnt! MicroPython versucht immer, hilfreich zu sein. Wenn es einen Fehler findet, wird es eine Nachricht übe das Display Deines micro:bit laufen lassen. IfWenn möglich, wird die Zeile, in derder Fehler aufgetreten ist, angezeigt.

Check Deinen Code: hast Du alles richtig abgetippt? Die Programmiersprache Python erwartet von Dir, dass Du alles richtig schreibst. Überprüfe Deine Schreibweisen (`display/Display/disPlay`) und Deine Zeichensetzung (hast Du auch wirklich einen . zwischen `display` und `scroll` und hast Du auch Anführungszeichen um `Hallo Welt!`?).

Falls Dein micro:bit nicht mehr reagiert: zieh' ihm den Stecker, d.h. trenne die USB-Verbindung und stecke sie wieder an. Es könnte auch sein, dass Du Mu neu starten musst.

## Weiter geht's...

Wenn Du hier fertig bist, mache mit der [nächsten Lektion](02_Images.md) weiter.