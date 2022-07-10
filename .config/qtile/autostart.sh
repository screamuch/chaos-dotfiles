#!/bin/sh

# defaults
$TERM=alacritty

# set monitor arrangement
$HOME/.screenlayout/default.sh

# enable Russian keyboard
setxkbmap -model Apple -layout "us,ru" -variant ",mac" -option "grp:alt_space_toggle" &

# launch compositor
compton --config ./.config/picom/picom.conf &

# launch clipboard manager
copyq &

# launch notifications daemon
dunst &

# draw wallpaper
nitrogen --restore &

# enable natural scrolling
natural-scrolling &

# start regular shit
telegram-desktop -startintray & 
discord --start-minimized &
slack -u &

# faster qutebrowser
qutebrowser --nowindow &

