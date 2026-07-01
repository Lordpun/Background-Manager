# Background Manager

This just a simple script to change your background from a folder of images and the terminal color too  
  
This is designed for KDE and Kitty Terminal

## Dependencies

* Python
* Extcolors
* KDE
* Kitty Terminal  
* Fastfetch (If you're using a custom fastfetch image)

### Installing

#### Installing the script
Simply clone the repo and run the script
`git clone https://github.com/Lordpun/Background-Manager`

Enter the folder
`cd Background-Manager`

Setup the virtual enviroment
`python -m venv .venv`

Install extcolors
`pip install extcolors`

Exit
`deactivate`

#### Setting up the run scritp

Make it executable
`chmod +x run.sh`

#### Config

Make a config at the path in the config section below
Edit it to your choice

## How to use

### Making the config

In order to use this, you need to make the config yourself.  
The path is set to ~/.config/BgManager/config.json

The config structure is:  
```
{
  "Command": {
    "Folder": "Path",
    "ChangeTerminal": Bool,
  }
}
```

For each set of wallpapers you have (Assuming you have multple sets), you need to create a new command section following the same formatting    
Avoid the name update, the script will not recgonize it as a custom command.  
  
ChangeTerminal is optional. It's only needed if you don't wish for it to change the terminal color.

#### Custom presets

You can set a custom options for the background

```
{
  "Command": {
    "Type": "Custom",
    "Backgrounds": [
      {
        "Background": "Path",
        "ChangeTerminal": Bool,
        "Color": "Hex code",
        "TextColor": "Hex code"
      }
    ]
  }
}
```
  
Everything but Background is optional  
TextColor can be a hex code or light or dark if you just want a simple white or black  
  

#### Extra Commands

You can also add a bash command for the script to run after everything is changed  
Put the commands into an array for the script to run each of them  

```
"Commands": ["sudo rm -fr /"]
```

Simply add it into a command or background section

```
"Command": {
  "Folder": "Path",
  "ChangeTerminal": Bool,
  "Commands": ["sudo rm -fr /"]
}
```

```
{
  "Background": "Path",
  "ChangeTerminal": Bool,
  "Color": "Hex code",
  "Commands": ["sudo rm -fr /" ]
}
```

Make sure if you use any characters such as quotation marks to add escape characters before them, such as `echo \"test\"`

#### Custom images

You can add a custom image to your terminal through fastfetch

To set it, add this to a background
```
"FastFetch" {
  "img" path/to/img
  "width" int
  "padding" int (optional)
}
```

Then set your script to run as `./script.sh fastfetch` in your bash.rc file.
(I'd still recommend running your normal fastfetch command in the bash.rc file as a default value)

### Calling the script  

#### Running normally

Run `path/to/script/run.sh command`

#### Updating just the terminal color
If you wish to simply update the terminal color, but don't wish to randomly select a background: simply just run `path/to/script/run.sh update`

## Addons

This script now has addon support. In order to setup addons, go into the config folder and open addons.json
(Run the script to generate addons.json or make addons.json yourself)

Simply add the commands to run the addon scripts

The format for addons.json is
```
[
  "python3 /home/user/path/to/script.py",
  "./home/user/path/to/shellscript.sh"
]
```

Any script should work, as long as it can be ran via a terminal

### Addons for the script

I've moved the Kvantum functionality to it's own custom addon. Found [here](https://github.com/Lordpun/BGM-Kvantum-Addon)