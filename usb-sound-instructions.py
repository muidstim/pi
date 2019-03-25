#First, delete the ~/.asoundrc


#Run this command
#sudo nano /etc/modprobe.d/alsa-base.conf

# put the following lines into the file, excluding the """
"""
options snd_usb_audio index=0 nrpacks=1
options snd_bcm2835 index=1

#does the reordering - added by Mr.Tim
options snd slots=snd_usb_audio, snd_bcm2835
"""


#download a sample wav from the web, and run this code to test it
import pygame.mixer
from pygame.mixer import Sound

from signal import pause

pygame.mixer.init()

mysound = Sound("sample.wav")

mysound.play()

pause()
