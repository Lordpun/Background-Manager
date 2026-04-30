from pathlib import Path
import subprocess
import sys
import json

imgConfig = Path.home() / ".config" / "BgManager" / "imgConfig.json"

def saveImg(imgPath, width, padding):
  if not imgConfig.exists():
    with open(imgConfig, "w") as file:
      file.close()

  imgData = {
    "imgPath": imgPath,
    "width": width,
    "padding": padding
  }

  with open(imgConfig, "w") as config:
    json.dump(imgData, config)

def wipeData():
  imgConfig.unlink()

def getData():
  if not imgConfig.exists():
    return None
  with open(imgConfig, "r") as config:
    return json.load(config)

def updateImg():
  configData = getData()
  if configData is None:
    return
  imgPath = configData.get("imgPath")
  width = configData.get("width")
  padding = configData.get("padding")
  subprocess.run(f"clear && fastfetch --logo \"{imgPath}\" --logo-type kitty-direct --logo-width {width} --logo-padding-top {padding}", shell=True)
