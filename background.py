import subprocess
import sys
import os
import extcolors

def setWallpaper(filePath):
  script = f"""
  var allDesktops = desktops();
  for (i=0; i<allDesktops.length; i++) {{
    d = allDesktops[i];
    d.wallpaperPlugin = "org.kde.image";
    d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
    d.writeConfig("Image", "file://{filePath}");
  }}
  """

  command = [
    "qdbus", "org.kde.plasmashell", "/PlasmaShell", 
    "org.kde.PlasmaShell.evaluateScript", script
  ]

  try:
    subprocess.run(command, check=True)
  except subprocess.CalledProcessError as e:
    sys.exit(f"Failed to set wallpaper: {e}")

def getColor(filePath):
  colors, pixel_count = extcolors.extract_from_path("image.jpg", tolerance=20)
  main_color = colors[0][0]
  return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def setTerminalColor():
  try:
    cmd = "grep 'Image=' ~/.config/plasma-org.kde.plasma.desktop-appletsrc | head -n 1"
    result = subprocess.check_output(cmd, shell=True).decode("utf-8")
    
    path = result.strip().replace("Image=file://", "")
    color = getColor(path)

    setCurrentBackgrounds(color)
    editKittyConfig(color)
  except Exception as e:
    sys.exit(f"Failed to find your wallpaper\'s path: {e}")

def editKittyConfig(color):
  conf_path = os.path.expanduser("~/.config/kitty/kitty.conf")
    
  if os.path.exists(conf_path):
    with open(conf_path, 'r') as f:
      lines = f.readlines()
  else:
    lines = []

  new_lines = [line for line in lines if not line.startswith("background ")]
  new_lines.append(f"background {color}\n")

  with open(conf_path, 'w') as f:
    f.writelines(new_lines)

def setCurrentBackgrounds(color):
  try:
    command = ["kitty", "@", "set-colors", f"background={color}"]
    
    subprocess.run(command, check=True)
    print(f"Background successfully set to {color}")
      
  except subprocess.CalledProcessError as e:
    print(f"Error: Could not change color. Is 'allow_remote_control' enabled?")
  except FileNotFoundError:
    print("Error: 'kitty' command not found in your path.")