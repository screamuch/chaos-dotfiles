# chaos ([ex-zeus] 2-head desktop) dotfiles

## install base system

Do what you gotta do - this is an arch-based config

## Install base system software right away

- `# pacman -S yay`
- `# pacman -S qtile alacritty copyq dunst fish gtop htop micro neofetch nitrogen picom pulsemixer libqalculate qutebrowser rofi rofi-emoji filelight xterm thunar`
- `$ yay -S ly pfetch ttf-apple-emoji noto-fonts-emoji-apple otf-code-new-roman`

## Unpack configs and set up X

1. `etc` contents (!) go in `/etc/`
2. `wallpapers` go in `$HOME/Pictures`
3. `.config`, `.screenlayout`, all other files (except `README.md` and `.git`) go in `$HOME`
4. Set up ly:
  - `# systemctl enable ly.service`
5. `$ chsh --shell /bin/fish $USER`

## Install application software

### First priority

- `$ yay -S zoom slack spotify telegram-desktop steam fiji-bin typora audacity`
- `$ yay -S ungoogled-chromium`
- `https://docs.conda.io/en/latest/miniconda.html`
- In `nvim` run `:PlugInstall`

### Not that necessary, KDE things I liked

`# pacman -S kdeconnect`
`# pacman -S kate`
`# pacman -S konsole`

