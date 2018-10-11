import time
from dotstar import Adafruit_DotStar

numpixels = 77
brightness = 16

datapin = 23
clockpin = 24

def main():
    strip = Adafruit_DotStar(numpixels, datapin, clockpin, order='gbr'.encode('utf-8'))
    strip.begin()
    strip.setBrightness(brightness)

    print("Hit Ctrl-C to end test")

    try:
        while True:
            strip.setPixelColor(5, 0xFF0000)
            strip.show()
            time.sleep(1000)
    except (KeyboardInterrupt, Exception) as ex:
        print(ex)
        print("")
        print("Turning off all lights...")
        # Not well documented, but this is how you turn
        # off everything
        strip.clear()
        strip.show()

        strip.close()
        print("Strip closed")


if __name__ == "__main__":
    main()

