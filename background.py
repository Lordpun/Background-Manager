from pathlib import Path
import subprocess
import sys
import os
import extcolors
import colorsys

wallpaperPath = Path.home() / ".config" / "plasma-org.kde.plasma.desktop-appletsrc"
kittyConfig = Path.home() / ".config" / "kitty" / "kitty.conf"

def getWallpaper():
  with open(wallpaperPath, "r") as config:
    lines = config.readlines()
    for line in lines:
      if "Image=file://" in line.strip():
        return line.replace("Image=file://", "", 1)

def getColor():
  path = getWallpaper()
  colors, pixel_count = extcolors.extract_from_path(path.strip(), tolerance=20)
  main_color = colors[0][0]
  h, l, s = colorsys.rgb_to_hls(main_color[0]/255, main_color[1]/255, main_color[2]/255)
  newBrightness = l * 0.75
  r, g, b = colorsys.hls_to_rgb(h, newBrightness, l)
  hexColor = '#{:02x}{:02x}{:02x}'.format(round(r * 255), round(g * 255), round(b * 255))

  return hexColor, newBrightness * 100

def setWallpaper(filePath):
  js_script = f"""
  var allDesktops = desktops();
  for (var i = 0; i < allDesktops.length; i++) {{
    var d = allDesktops[i];
    d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
    d.writeConfig("Image", "file://{filePath}");
    d.reloadConfig();
  }}
  """

  if subprocess.run(["which", "qdbus-qt6"], capture_output=True).returncode == 0:
    command = "qdbus-qt6"
  elif subprocess.run(["which", "qdbus"], capture_output=True).returncode == 0:
    command = "qdbus"
  else:
    command = "/usr/lib/qt6/bin/qdbus" 

  if not os.path.exists(command) and subprocess.run(["which", command], capture_output=True).returncode != 0:
    sys.exit("Error: Neither qdbus-qt6 nor qdbus was found. Please install qt6-tools.")
    return
  
  subprocess.run([
    command, 
    "org.kde.plasmashell", 
    "/PlasmaShell", 
    "org.kde.PlasmaShell.evaluateScript", 
    js_script
  ])


def setTerminalColor():
  color,brightness = getColor()

  if brightness < 60:
    textColor = "#ddd"
  else:
    textColor = "#111"

  colorExists = False
  textExists = False
  remoteExists = False

  with open(kittyConfig, "r") as config:
    lines = config.readlines()
    for line in lines:
      if line.strip().startswith("background "):
        lines[lines.index(line)] = f"background {color}\n"
        colorExists = True
      
      if line.strip().startswith("foreground "):
        lines[lines.index(line)] = f"foreground {textColor}\n"
        textExists = True

      if line.strip().startswith("allow_remote_control "):
        if line.strip().endswith("no"):
          break
        remoteExists = True

      if colorExists and textExists and remoteExists:
        break

  if not colorExists:
    lines.append(f"\nbackground {color}\n")
  if not textExists:
    lines.append(f"\nforeground {textColor}\n")
  if not remoteExists:
    sys.exit("Please set allow_remote_control to yes in kitty.conf")

  with open(kittyConfig, "w") as config:
    config.writelines(lines)

  subprocess.run(["kitty", "@", "set-colors", "--all", f"background={color}", f"foreground={textColor}"])