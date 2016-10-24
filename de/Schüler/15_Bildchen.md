# Bildchen

Der micro:bit hat eine so genannte Matrix (also fünf Zeilen mal fünf Spalten) aus 25 LEDs (Leuchtdioden), die man prima zum Anzeigen von kleinen Bildchen benutzen kann. MicroPython unterstützt diese 5 x 5 Matrix voll und gibt Dir die Kontrolle darüber. Damit kannst Du ein paar schöne Effekte gestalten.

MicroPython hat jede Menge vorinstallierter Bildchen, die Du auf dem "Display" zeigen kannst. Zum Beispiel kannst Du sagen, dass der micro:bit glücklich aussehen soll:

```python
from microbit import *
display.show(Image.HAPPY)
```

Was die erste Zeile macht, weißt Du ja schon. Die zweite Zeile sagt dem Display, dass es ein Bildchen (Image) zeigen soll (show), und zwar mit dem Namen "HAPPY". Wie beim [ersten Beispiel](10_Hallo_Welt.md) setzen wir das was wir zeigen wollen in eine Klammer (). Es gibt eine ganze Menge vorgefertigter Bildchen, die Du gerne mal ausprobieren kannst:

ANGRY, ARROW_E, ARROW_N, ARROW_NE, ARROW_NW, ARROW_S, ARROW_SE, ARROW_SW, ARROW_W, ASLEEP, BUTTERFLY, CHESSBOARD, CLOCK1, CLOCK2, CLOCK3, CLOCK4, CLOCK5, CLOCK6, CLOCK7, CLOCK8, CLOCK9, CLOCK10, CLOCK11, CLOCK12, CONFUSED, COW, DIAMOND, DIAMOND_SMALL, DUCK, FABULOUS, GHOST, GIRAFFE, HAPPY, HEART, HEART_SMALL, HOUSE, MEH, MUSIC_CROTCHET, MUSIC_QUAVER, MUSIC_QUAVERS, NO, PACMAN, PITCHFORK, RABBIT, ROLLERSKATE, SAD, SILLY, SKULL, SMILE, SNAKE, SQUARE, SQUARE_SMALL, STICKFIGURE, SURPRISED, SWORD, TARGET, TORTOISE, TRIANGLE, TRIANGLE_LEFT, TSHIRT, UMBRELLA, XMAS, YES

## Eigene Bildchen

Ist schon klar - das sind viele Bildchen, aber Du willst gerne Dein eigenes anzeigen lassen? Das geht auch und zwar ziemlich einfach!

Jeder LED Punkt (Pixel) kann einen von zehn Werten (für die Helligkeit) erhalten. Wenn ein Pixel 0 (Null) ist, dann ist es aus (dunkel). Es hat eine Helligkeit von Null. Wenn es aber eine Helligkeit von 9 hat, leuchtet es ganz stark. Die Werte 1 bis 8 sind irgendwas dazwischen. Mit dieser Information kannst Du jetzt Deine eigenen Bildchen malen:

```python
from microbit import *

boot = Image("05050:"
             "05050:"
             "05050:"
             "99999:"
             "09990")

display.show(boot)
```