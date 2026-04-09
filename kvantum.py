from pathlib import Path
import xml.etree.ElementTree as ET
import background
import colorsys
import subprocess
import shutil
import sys

def getQdbus():
  for cmd in ['qdbus6', 'qdbus-qt5', 'qdbus']:
    if shutil.which(cmd):
      return cmd
  return None

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

  # Hard coded for the theme I use. I'm assuming most themes use different methods of setting colors, so probably best to edit this to fit yours
  ET.register_namespace('inkscape', "http://www.inkscape.org/namespaces/inkscape")
  ET.register_namespace('sodipodi', "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd")

  svg = Path.home() / ".config" / "Kvantum" / "Glassy" / "Glassy.svg"

  tree = ET.parse(svg)
  root = tree.getroot()

  window = root.find(".//{http://www.w3.org/2000/svg}g[@id='window-normal']")
  if window is None:
    sys.exit("Kvantum theme window wasn't found in the SVG")
  window.set("style", f"fill-opacity:0.70588237;opacity:0.7;fill:{color}")

  windowRect = window.find("{http://www.w3.org/2000/svg}rect")
  if windowRect is None:
    sys.exit("Kvantum theme rect wasn't found in the SVG")
  windowRect.set("style", f"fill-opacity:0.70588237;stroke:none;fill:{color}")

  tree.write(svg, encoding='utf-8', xml_declaration=True)

  subprocess.run(f"{getQdbus()} org.kde.KWin /KWin reconfigure", shell=True)

  cache_path = Path.home() / ".cache" / "kvantum"
  if cache_path.exists():
    try:
      shutil.rmtree(cache_path)
    except OSError:
      pass
        
  subprocess.run(["killall", "-9", "dolphin"], stderr=subprocess.DEVNULL)
  subprocess.Popen(["dolphin"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)