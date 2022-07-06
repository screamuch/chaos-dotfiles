#!/bin/bash
# This script copies my configs over from the current system to the repository

# get directory of the repo
BASEDIR=$(dirname $0)

# ~/.config/ files
DIRECTORY=${BASEDIR}/.config/
if [ ! -d "$DIRECTORY" ]; then
  mkdir ${DIRECTORY}
fi

# alacritty
DIRECTORY=${BASEDIR}/.config/alacritty/
if [ ! -d "$DIRECTORY" ]; then
  mkdir ${DIRECTORY}
fi
cp ${HOME}/.config/alacritty/alacritty.yml ${BASEDIR}/.config/alacritty/alacritty.yml

# coc (for vim)
cp -r ${HOME}/.config/coc/ ${BASEDIR}/.config/

# copyq
DIRECTORY=${BASEDIR}/.config/copyq/
if [ ! -d "$DIRECTORY" ]; then
  mkdir ${DIRECTORY}
fi
cp ${HOME}/.config/copyq/copyq.conf ${BASEDIR}/.config/copyq/copyq.conf

# dunst
DIRECTORY=${BASEDIR}/.config/dunst/
if [ ! -d "$DIRECTORY" ]; then
  mkdir ${DIRECTORY}
fi
cp ${HOME}/.config/dunst/dunstrc ${BASEDIR}/.config/dunst/dunstrc

# fish
cp -r ${HOME}/.config/fish/ ${BASEDIR}/.config/

# htop
DIRECTORY=${BASEDIR}/.config/htop/
if [ ! -d "$DIRECTORY" ]; then
  mkdir ${DIRECTORY}
fi
cp ${HOME}/.config/htop/htoprc ${BASEDIR}/.config/htop/htoprc

# kdeconnect
cp -r ${HOME}/.config/kdeconnect/ ${BASEDIR}/.config/

# micro
cp -r ${HOME}/.config/micro ${BASEDIR}/.config/

# neofetch
cp -r ${HOME}/.config/neofetch ${BASEDIR}/.config/

# nitrogen
cp -r ${HOME}/.config/nitrogen ${BASEDIR}/.config/

# nvim
DIRECTORY=${BASEDIR}/.config/nvim/
if [ ! -d "$DIRECTORY" ]; then
  mkdir ${DIRECTORY}
fi
cp ${HOME}/.config/nvim/init.vim ${BASEDIR}/.config/nvim/init.vim

# compton
DIRECTORY=${BASEDIR}/.config/picom/
if [ ! -d "$DIRECTORY" ]; then
  mkdir ${DIRECTORY}
fi
cp ${HOME}/.config/picom/picom.conf ${BASEDIR}/.config/picom/picom.conf

# qalculate
DIRECTORY=${BASEDIR}/.config/qalculate/
if [ ! -d "$DIRECTORY" ]; then
  mkdir ${DIRECTORY}
fi
cp ${HOME}/.config/qalculate/qalc.cfg ${BASEDIR}/.config/qalculate/qalc.cfg

# qtile
DIRECTORY=${BASEDIR}/.config/qtile/
if [ ! -d "$DIRECTORY" ]; then
  mkdir ${DIRECTORY}
fi
cp ${HOME}/.config/qtile/config.py ${BASEDIR}/.config/qtile/config.py
cp ${HOME}/.config/qtile/autostart.sh ${BASEDIR}/.config/qtile/autostart.sh

# qutebrowser
cp -r ${HOME}/.config/qutebrowser/ ${BASEDIR}/.config/

# rofi
DIRECTORY=${BASEDIR}/.config/rofi/
if [ ! -d "$DIRECTORY" ]; then
  mkdir ${DIRECTORY}
fi
cp -r ${HOME}/.config/rofi/config.rasi ${BASEDIR}/.config/rofi/config.rasi

# filelight
cp ${HOME}/.config/filelightrc ${BASEDIR}/.config/filelightrc

# kate
cp ${HOME}/.config/katerc ${BASEDIR}/.config/katerc

# konsole
cp ${HOME}/.config/konsolerc ${BASEDIR}/.config/konsolerc

# zoom
cp ${HOME}/.config/zoomus.conf ${BASEDIR}/.config/zoomus.conf

# .face
cp ${HOME}/.face ${BASEDIR}/.face

# wallpaper
cp -r ${HOME}/Pictures/wallpapers ${BASEDIR}/

# bashrc
cp ${HOME}/.bashrc ${BASEDIR}/.bashrc

# gitconfig
cp ${HOME}/.gitconfig ${BASEDIR}/.gitconfig

# homepage
cp ${HOME}/home.html ${BASEDIR}/home.html

# ly
DIRECTORY=${BASEDIR}/etc/ly
if [ ! -d "$DIRECTORY" ]; then
  mkdir ${DIRECTORY}
fi
cp /etc/ly/config.ini ${BASEDIR}/etc/ly/config.ini

# screen layout
DIRECTORY=${BASEDIR}/.screenlayout/
if [ ! -d "$DIRECTORY" ]; then
  mkdir ${DIRECTORY}
fi
cp ${HOME}/.screenlayout/default.sh ${BASEDIR}/.screenlayout/default.sh


