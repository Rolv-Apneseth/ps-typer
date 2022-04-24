#!/bin/env bash

for ui_file in source/*.ui
do
    base_filename="$(basename -s .ui "$ui_file")"

    pyuic5 "$ui_file" -o "$base_filename.py"
done
