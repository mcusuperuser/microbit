# Bewegte Bilder

Bildchen machen schon eine Menge Spaß. Aber bewegte Bilder sind viel lustiger. Wie man Bilder bewegen kann? Ganz einfach: man macht eine Liste von Bildern, die man zeigen will und schickt die Elemente dieser Liste dann eins nach dem anderen zum micro:bit.

Wie erstellt man Listen in Python? Hier ist eine einfache Liste mit Dingen, die man in der Schule braucht:
- Epochenheft
- Wachsmalkreiden
- Brotzeitbox

Nennen wir diese Liste "Schulutensilien". In Python machen wir folgendermaßen eine Liste daraus:

```python
Schulutensilien = ["Epochenheft", "Wachsmalkreiden", "Brotzeitbox" ]
```

Das ist einfach! Python weiß, dass das eine Liste ist, weil die einzelnen Elemente in eckigen Klammern ([ ]) aufgezählt werden. Die Elemente trennt man mit einem Komma und Zeichenfolgen, sogenannte **Strings**, setzt man in englische Anführungszeichen (" "). In Python kann man aus allem Möglichen eine Liste machen, z.B.:

```python
Irre_Liste = ["Pausenbrot", 5, 28.3, "Schulbus", Image.HEART ]
```

**Notiz**
> Zahlen müssen nicht Anführungszeichen gesetzt werden. Sind sie in Anführungszeichen, sind es keine Zahlen mehr, sondern Text. Verwirrt?

In dem Beispiel oben war das letzte Element ein Bildchen (das Herz). Damit weisst Du jetzt, wie Du eine Liste von verschiedenen Bildchen erstellen kannst. Probier's doch mal mit Deinen drei Lieblingsbildchen aus!

Wir können in MicroPython jede Liste mit Bildchen anzeigen, und zwar mit dem uns schon bekannten Befehl `display.show`. Zum Glück gibt es schon ein paar vordefiniert Listen, die Du ganz schnell ausprobieren kannst:

```python
from microbit import *

display.show(Image.ALL_ARROWS, loop=True, delay=100)
```

Wie bei einem einzelnen Bildchen sagen wir dem micro:bit mit `display.show`, dass er etwas anzeigen soll. Das, was er anzeigen soll, ist die Liste `Image.ALL_ARROWS` und zwar in einer endlosen Schleife (`loop=True`). Die einzelnen Elemente sollen alle 100 ms (eine Zehntelsekunde) gewechselt werden (`delay=100`).

Es gibt noch eine andere Liste, und zwar `ALL_CLOCKS`. Wie kannst Du sie anzeigen? Wie machst Du, dass die Anzeige langsamer wird? Und wie kannst Du dafür sorgen, dass die Bildchen nur einmal angezeigt werden (anstatt immer im Wechsel)?

Kannst Du das Bildchen, das Du in der [vorherigen Lektion](15_Bildchen.md) gezeichnet hast auch animieren? Denk daran, die einzelnen Bilder zu einer Liste zusammenzufügen. Im Code gibt es ein Beispiel mit einem sinkenden Schiff. Schau mal rein!

## Weiter geht's...

Die [nächste Lektion](25_Knöpfe.md) zeigt Dir, was man mit den Knöpfen **A** und **B** anfangen kann..