#!/bin/sh

# set monitor arrangement
$HOME/.screenlayout/default.sh

# enable Russian keyboard
setxkbmap -model logicordless -layout "us,ru" -variant ",mac" -option "grp:alt_space_toggle" &

# launch compositor
compton --config ./.config/picom/picom.conf &

# launch clipboard manager
copyq &

# launch notifications daemon
dunst &

# draw wallpaper
nitrogen --restore &

# enable natural scrolling
natural-scrolling

# start regular shit
telegram-desktop &
discord &
slack &

