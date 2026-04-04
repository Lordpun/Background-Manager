from pathlib import Path
import sys
import json

command = ""

def getArgs():
  global command
  if len(sys.argv) > 1:
    command = sys.argv[1]

configPath = Path.home() / ".config" / "BgManager" / "config.json"

def getConfig():
  with open('data.json', 'r') as configFile:
    config = json.load(configFile)

  if not config[command]:
    sys.exit(f"Command {command} not found")


def getCommand():
  if not configPath.exists():
    sys.exit("No config found")

getArgs()

if command == "":
  sys.exit()