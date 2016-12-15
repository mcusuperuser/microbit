# Tasten

Bis jetzt haben wir Programme für unseren micro:bit geschrieben, die dafür gesorgt haben, er etwas anzeigt. Das nennt man Ausgabe/Output. Man kann aber auch dafür sorgen, dass er darauf wartet, dass etwas passiert. Das nennt man Eingabe/Input.

Wie können wir nun etwas eingeben? Der micro:bit hat ja weder Maus noch Touchscreen. Er hat aber eine Tastatur, die aus zwei Tasten besteht, nämlich **A** und **B**. Jetzt müssne wir nur noch dafür sorgen, dass er auf eine Eingabe wartet. Das geht ganz einfach:

```python
from microbit import *

sleep(10000)
display.scroll(str(button_a.get_presses()))
```

Was macht dieser Code? Probier's aus!

Das Skript wartet zehn Sekunden (10.000 Millisekunden) lang auf Eingaben und zeigt dann an, wie oft Du in dieser Zeit die Taste A gedrückt hast. 

Ein paar Anmerkungen:
1. Die `sleep` Funktion sorgt dafür, dass unser micro:bit für eine bestimmte Anzahl an Millisekunden schläft. Wenn Dein Programm mal eine Pause braucht, weisst Du jetzt, wie es geht. Eine Funktion ist wie eine Methode, aber sie ist nicht mit einem Punkt an ein Objekt geheftet.
2. Es gibt ein Objekt namens `button_a` und Du kannst damit die Anzahl der Tastendrücke mit der Methode `get_presses` zählen.
3. Weil `get_presses` uns einen numerischen Wert (=eine Zahl) zurückliefert, aber `display.scroll` nur Zeichen anzeigt, müssen wir den Wert mit Hilfe der `str` Funktion (Kurzform für "string") konvertieren. Diese Funktion übersetzt alles Mögliche in Zeichenketten (strings).

## Verschachtelungen

Unsere dritte Code-Zeile ist ein wenig wie eine Zwiebel: man kann sie entlang der runden Klammern häuten. `button_a.get_presses` hat ein paar davon, `str` packt `button_a.get_presses` dazwischen und wird seinerseits von denen von `display.scroll` eingeklammert. Wie kann man die nun auseinanderpfriemeln?

Im Gegensatz zu der Zwiebel, die wir von außen nach innen häuten, löst Python die Klammern von innen nach außen auf. Stellen wir uns vor, wir hätten die Taste A siebenmal gedrückt. Dadurch wird der Wert von `button_a.get_presses()` zu '7'. Python setzt den Wert in `str` ein und erhält `str(7)`, das wiederum in `display.scroll()` eingesetzt wird. Es entsteht: `display.scroll(str(7))`. Das Ganze nennt man Verschachtelung/Nesting. Damit kann man schon eine Menge anstellen.

## Schleifen

Oft müssen Programme darauf warten, dass etwas geschieht. Um das zu erreichen, macht man eine Schleife um ein Stück Code, der zum Beispiel definiert, wie unser micro:bit auf bestimmte Ereignisse wie einen Knopfdruck reagieren soll.

Um Schleifen/Loops in Python zu erstellen, benutzen wir das `while`-Schlüsselwort. Es überprüft, ob etwas wahr ist. Wenn es das ist, führt es ein Code-Block aus, das der Körper der Schleife genannt wird. Wenn es das nicht ist, bricht es aus der Schleife aus, ignoriert den Körper, und der Rest des Programms kann fortgesetzt werden.

Python macht es einfach, Code-Blöcke zu definieren. Man muss einfach nur die Sachen, die gemeinsam ausgeführt werden sollen, einrücken (also ein paar Leerzeichen davor stellen) und untereinander schreiben. Ein Beispiel:

```python
from microbit import *

while running_time() < 10000:
    display.show(Image.ASLEEP)

display.show(Image.SURPRISED)
```

Die Funktion `running_time` gibt die Anzahl der Millisekunden zurück, die vergangen sind, seitem der micro:bit das aktuelle Programm gestartet hat. das nennt man Laufzeit.

Die Zeile `while running_time() < 10000:` überprüft, ob die Laufzeit kleiner als 10000 Millisekunden (also 10 Sekunden) ist. Solange das der Fall ist, wird die nächste Zeile, der Körper der Schleife ausgeführt und das Schlaf-Bildchen angezeigt.

Und sobald die Laufzeit 10 Sekunden beträgt (oder sogar größer als das ist), zeigt der micro:bit `Image.SURPRISED` and. Warum? Weil die Bedingung der Schleife falsch ist (Laufzeit ist nicht länger kleiner als 10 Selunden). In diesem Fall wird die Schleife verlassen und der Rest der Programms wird ausgeführt. Da `display.show(Image.SURPRISED)` nicht eingerückt ist und somit nicht zur Schleife gehört, ist es nun an der Reihe. Unser micro:bit schläft also für zehn Sekunden und schaut dann überrascht aus der Wäsche.

Versuch's!


## Eingaben behandeln

Wenn wir nun wollen, dass unser micro:bit generell auf Tastendrücke reagiert, müssen wir eine unendliche Schleife benutzen und darin abfragen, ob mit den Tasten etwas passiert ist. Eine unendliche Schleife ist einfach:

```python
while True:
    # mach' etwas
```

Erinnerst Du dich? `while` testet, ob etwas **wahr** ist. Nun, **True** ist das englische Wort für wahr und das ist immer wahr - also wird diese Schleife niemal verlassen.

Lass uns einen kleinen Zoo errichten. Dort sehen wir immer eine Giraffe, aber solange wir Taste A drücken, sehen wir eine Schlange. Wenn wir Taste B drücken, gehen wir nach Hause und sehen gar nichts mehr:
```python
from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.SNAKE)
    elif button_b.is_pressed():
        break
    else:
        display.show(Image.GIRAFFE)

display.clear()
```

Verstehst Du, wie wir testen, welche Tasten gedrückt werden? Wir haben `if`, `elif` und `else` benutzt, englisch für wenn (`if`), wenn was anderes (`elif` = else if) und ansonsten (`else`). Das nennt man Bedingungen und die funktionieren so:
```python
if irgendwas ist True:
    # tu eine Sache
elif irgendetwas anderes ist True:
    # tu eine andere Sache
else:
    # mach was ganz anderes.
```

Das ist fast wir ganz normale Sprache. die Methode `is_pressed` gibt entweder wahr (True) oder falsch (False) zurück. Wenn man eine Taste drückt, bekommt man wahr, ansonsten falsch. Unser Code sagt also, dass wir für immer testen wollen, dass:
- wenn Taste A gedrückt wird, eine Schlange erscheint
- wenn Taste B gedrückt wird, wir im Programm weitermachen wollen (`break`)
- und wir ansonsten eine Giraffe sehen wollen.

Wenn wir nun die Schleife verlassen, weil wir die Taste B gedrückt haben, dann beenden wir das Programm mit einer leeren Anzeige.

Was passiert, wenn wir beide Tasten gleichzeitig drücken? Kannst Du das Programm umschreiben, so dass diese Fall auch abgefragt wird? Tipp: Python hat sogenannte logische Operatoren (und/oder/nicht, `and`/`or`/`not`), mit denen man mehrere Aussagen überprüfen kann.

## Weiter geht's...

Die [nächste Lektion](30_IO.md) zeigt Dir, wozu die goldenen Kontakte an dem einen Ende von unserem micro:bit da sind.