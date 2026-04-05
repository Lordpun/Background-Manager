from pathlib import Path
import subprocess
import sys
import os
import extcolors

wallpaperPath = Path.home() / ".config" / "plasma-org.kde.plasma.desktop-appletsrc"
kittyConfig = Path.home() / ".config" / "kitty" / "kitty.conf"

def getColor(filePath):
  colors, pixel_count = extcolors.extract_from_path("image.jpg", tolerance=20)
  main_color = colors[0][0]
  return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def getWallPaper():
  with open(wallpaperPath, "r") as config:
    lines = config.readlines()
    for line.strip() in lines:
      if "Image=file://" in line:
        return line.replace("Image=file://", "", 1)

def setWallpaper(filePath):
  pass

def setTerminalColor():
  pass

def editKittyConfig(color):
  pass

def setCurrentBackgrounds(color):
  pass
  pass