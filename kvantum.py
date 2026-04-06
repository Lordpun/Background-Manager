from pathlib import Path
import background
import configparser
import colorsys
import subprocess

kvantumPath = Path.home() / ".config" / "Kvantum"

def findColorConfig():
  config = configparser.ConfigParser()
  config.read(kvantumPath / "kvantum.kvconfig")

  if config.has_option("General", "theme"):
    theme = config.get("General", "theme")
    themePath = kvantumPath / theme

    files = [f for f in themePath.iterdir() if f.is_file()]
    for file in files:
      if file.suffix == ".kvconfig":
        return themePath / file
  return kvantumPath / "kvantum.kvconfig"

def makeBaseColor(color):
  value = color.lstrip('#')
  rgb = tuple(int(value[i:i+2], 16) for i in (0, 2, 4))
  h, l, s = colorsys.rgb_to_hls(rgb[0]/255, rgb[1]/255, rgb[2]/255)
  l = l * 0.9
  r, g, b = colorsys.hls_to_rgb(h, l, s)
  return '#{:02x}{:02x}{:02x}'.format(round(r * 255), round(g * 255), round(b * 255))

def setKvantumColor(color="auto"):
  if color == "auto" or not color[0] == "#" or len(color) > 7:
    color = background.getColor()[0]
  baseColor = makeBaseColor(color)

  configPath = findColorConfig()

  config = configparser.ConfigParser()
  config.read(configPath)

  if not config.has_section("GeneralColors"):
    config.add_section("GeneralColors")
  config.set("GeneralColors", "window.color", color)
  config.set("GeneralColors", "base.color", baseColor)

  with open(configPath, 'w') as configfile:
    config.write(configfile, space_around_delimiters=False)

  subprocess.run(["kvantummanager", "--set", configPath.stem])
  subprocess.run(["dbus-send", "--type=signal", "/KGlobalSettings", "org.kde.KGlobalSettings.notifyChange", "int32:0", "int32:0"])
  subprocess.run(["killall", "dolphin"])