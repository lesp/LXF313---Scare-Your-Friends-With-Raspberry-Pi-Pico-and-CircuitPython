import time
import board
import digitalio
import audiomp3
import audiopwmio

sensor = digitalio.DigitalInOut(board.GP2)
sensor.switch_to_input(pull=digitalio.Pull.DOWN)
audio = audiopwmio.PWMAudioOut(board.GP0)

decoder = audiomp3.MP3Decoder(open("alert-tone.mp3", "rb"))

while True:
    print(sensor.value)
    if sensor.value == False:
        print("ALARM TRIGGERED")
        audio.play(decoder)
        while audio.playing:
            pass
    else:
        print("ALARM STANDBY")
    time.sleep(0.5)
