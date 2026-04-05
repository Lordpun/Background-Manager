from pathlib import Path
import subprocess
import sys
import os
import extcolors

wallpaperPath = Path.home() / ".config" / "plasma-org.kde.plasma.desktop-appletsrc"
kittyConfig = Path.home() / ".config" / "kitty" / "kitty.conf"

def getWallPaper():
  with open(wallpaperPath, "r") as config:
    lines = config.readlines()
    for line.strip() in lines:
      if "Image=file://" in line:
        return line.replace("Image=file://", "", 1)

def getColor():
  path = getWallpaper()
  colors, pixel_count = extcolors.extract_from_path(path, tolerance=20)
  main_color = colors[0][0]
  return '#{:02x}{:02x}{:02x}'.format(main_color[0], main_color[1], main_color[2])

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
  color = getColor()
  colorExists = False

  with open(kittyConfig, "r") as config:
    lines = config.readlines()
    for line in lines:
      if line.strip().startswith("background "):
        lines[lines.index(line)] = f"background {color}\n"
        colorExists = True
        break

      if line.strip().startswith("allow_remote_control "):
        if line.strip().endswith("no"):
          sys.exit("Please make sure allow_remote_control is set to yes in kitty.conf")

  if not colorExists:
    lines.append(f"background {color}\n")

  with open(kittyConfig) as config:
    config.writelines(lines)

  setActiveTerminals(color)

def findSockets():
  sockets = []
  search_paths = ['/tmp', os.environ.get('XDG_RUNTIME_DIR', '/run/user/1000')]
  
  for path in search_paths:
    if os.path.exists(path):
      for item in os.listdir(path):
        if item.startswith('kitty-control-'):
          sockets.append(os.path.join(path, item))
  return sockets

def setActiveTerminals(color):
  sockets = findSockets()

  if not sockets:
    sys.exit("No active Kitty sockets found.")
    return

  for socket in sockets:
    socket_path = f"unix:{socket}"
    
    command = [
      "kitty", "@", 
      "--to", socket_path, 
      "set-colors", 
      f"background={color}"
    ]
    
    try:
      subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
      sys.exit(f"Failed to update: {socket}")