import subprocess
import sys
import os
import extcolors

def getColor(filePath):
  colors, pixel_count = extcolors.extract_from_path("image.jpg", tolerance=20)
  main_color = colors[0][0]
  return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def setWallpaper(filePath):
  pass

def setTerminalColor():
  pass

def editKittyConfig(color):
  pass

def setCurrentBackgrounds(color):
  pass