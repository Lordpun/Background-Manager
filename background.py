import subprocess
import sys
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
  return main_color

def setTerminalColor():
  try:
    cmd = "grep 'Image=' ~/.config/plasma-org.kde.plasma.desktop-appletsrc | head -n 1"
    result = subprocess.check_output(cmd, shell=True).decode("utf-8")
    
    path = result.strip().replace("Image=file://", "")
    color = getColor(path)
  except Exception:
    sys.exit("Failed to find your wallpaper\'s path")