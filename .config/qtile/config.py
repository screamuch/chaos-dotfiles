# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os, subprocess

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.dgroups import simple_key_binder
from libqtile.lazy import lazy
# from libqtile.log_utils import logger

mod = "mod4"
terminal = "alacritty"
rofi = "rofi -show run -terminal alacritty"

# colors
text_color = "000000"
background_color = "e5e5e5"
number_color = "1C9898"
diff_color = "ECECEC"
line_color = "BBBBBB"
folded_color = "808080"
comment_color = "AAAAAA"

keys = [

    # Switch between windows

    Key([mod], "j",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
    ),
    Key([mod], "k",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
    ),

    # Switch between screens

    Key([mod, "control"], 'l', lazy.to_screen(0), desc='Move focus to horizontal monitor'),
    Key([mod, "control"], 'h', lazy.to_screen(1), desc='Move focus to horizontal monitor'),

    # Manipulate window placement

    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc='Move windows down in current stack'
    ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc='Move windows up in current stack'
    ),

    # Manupulate window size

    Key([mod], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
    ),
    Key([mod], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
    ),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
    ),

    # Manipulate window state

    Key([mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
    ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
    ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
    ),


    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        # desc="Toggle between split and unsplit sides of stack"),
    Key([mod, "shift"], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "space", lazy.spawn(rofi), desc="Launch rofi"),
    Key([mod], "b", lazy.spawn('qutebrowser'), desc="Launch browser"),

    # Toggle between different layouts as defined below
    Key([mod], "p", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Screenshots
    Key([], "Print", lazy.spawn('spectacle -mc'), desc="Screenshot current monitor"),
    Key([mod, "shift"], "Print", lazy.spawn('spectacle -rc'), desc="Screenshot a region"),
    Key([mod], "Print", lazy.spawn('spectacle -ac'), desc="Screenshot active window"),
]

# groups
def init_group_names():
    return [
        ('web', {'layout': 'monadtall'}),
        ('irc', {'layout': 'monadthreecol'}),
        ('mail', {'layout': 'monadtall'}),
        ('doc', {'layout': 'monadtall'}),
        ('dev', {'layout': 'verticaltile'}),
        ('sys', {'layout': 'verticaltile'}),
        ('mus', {'layout': 'monadtall'}),
        ('nl1', {'layout': 'monadtall'}),
        ('nl2', {'layout': 'monadtall'})
    ]

def init_groups(group_names):
    return [Group(name, **kwargs) for name, kwargs in group_names]


group_names = init_group_names()
groups = init_groups(group_names)

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))


layout_theme = {"border_width": 3,
                "margin": 5,
                "border_focus": "0000ff",
                "border_normal": "dddddd"
                }



layouts = [
    layout.MonadTall(**layout_theme),
    layout.VerticalTile(**layout_theme),
    layout.MonadThreeCol(**layout_theme),
]

widget_defaults = dict(
    # font='Code New Roman',
    font='Code New Roman',
    fontsize=17,
    padding=3,
    background=background_color,
    foreground=text_color
)
# extension_defaults = widget_defaults.copy()

screens = [
    # horizontal screen (right side)
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    inactive="666666",
                    active="000000"
                ),
                widget.Sep(padding=8),
                widget.WindowName(font='SF Pro', fontsize=17),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayout(font='SF Pro', fontsize=17),
                widget.Sep(padding=8),
                widget.Systray(),
                # make this display something on mouse hover
                widget.PulseVolume(emoji=True, volume_app="pulsemixer"),
                widget.Clock(font='SF Pro', fontsize=18, padding=10,
                             format='%m/%d/%Y %a %I:%M:%S %p'
                ),
            ],
            25,
            # background="#cccccc"
        ),
    ),
    # vertical screen (left side)
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    inactive="666666",
                    active="000000"
                ),
                widget.Sep(padding=8),
                widget.WindowName(font='SF Pro', fontsize=17),
                widget.CurrentLayout(font='SF Pro', fontsize=17),
                widget.Sep(padding=8),
                widget.CPU(
                    font='SF Pro', fontsize=17,
                    format="cpu: {load_percent}%",
                    mouse_callbacks = {'Button1': lazy.spawn(terminal + ' -e gtop')},
                ),
                widget.Sep(padding=8),
                widget.Memory(
                    font='SF Pro', fontsize=17,
                    format="ram: {MemUsed:.0f}{mm} ",
                    mouse_callbacks = {'Button1': lazy.spawn(terminal + ' -e htop')},
                ),
            ],
            25,
            # background="#cccccc"
        ),
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button1", lazy.window.bring_to_front()),
]

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='confirm'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='notification'),
    Match(wm_class='dialog'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    # Match(title='Telegram'),
    # Match(title='Discord'),
    # Match(title='Zoom'),
    # Match(title='Slack'),
    Match(wm_class='copyq'),
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
