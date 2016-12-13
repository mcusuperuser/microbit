from microbit import *

boot1 = Image("00500:"
              "05550:"
              "00500:"
              "99999:"
              "09990")

boot2 = Image("00000:"
              "00500:"
              "05550:"
              "00500:"
              "99999")

boot3 = Image("00000:"
              "00000:"
              "00500:"
              "05550:"
              "00500")

boot4 = Image("00000:"
              "00000:"
              "00000:"
              "00500:"
              "05550")

boot5 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00500")

boot6 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")

sinkendes_schiff = [boot1, boot2, boot3, boot4, boot5, boot6]
display.show(sinkendes_schiff, delay=750)