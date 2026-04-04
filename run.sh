#!/bin/bash

command=$1
projectDir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

source "$projectDir/.venv/bin/activate"
python3 "$projectDir/main.py" "$command"
deactivate