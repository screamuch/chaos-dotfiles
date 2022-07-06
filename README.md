# chaos ([ex-zeus] 2-head desktop) dotfiles

## Install base system

- Do what you gotta do - this is an arch-based config
- Make swap, fat32 efi boot partitions
- `# pacstrap MOUNT_POINT base linux linux-firmware`
- Sync the clock to hardware
- Install `sudo`, `nano`, `efibootmgr`, `efibootmgr`, `dosfstools`, `mtools`, `grub`
- Uncomment enUS locale in `locale.gen` (and ru maybe), `# locale-gen`
- Make `/etc/hostname` and `/etc/hosts` with loopback
- Set root passwd
- Create users, add them to `wheel,audio,video,optical`
- `EDITOR=nano visudo` - uncomment `%wheel`
- Install grub, `grub-install`

## Install base system software right away

- enable `multilib` repo
- `# pacman -Syyu git`
- install yay (`makepkg -si`)
- `# pacman -S qtile alacritty copyq dmenu dunst fish gtop htop libinput micro neofetch nitrogen picom pulsemixer libqalculate qutebrowser rofi rofi-emoji filelight xterm thunar spectacle thunderbird`
- `$ yay -S ly pfetch ttf-apple-emoji noto-fonts-emoji-apple otf-code-new-roman ttf-hack apple-fonts github-cli rofi-calc`

## Unpack configs and set up X

1. `$ gh auth login`
2. `$ git clone https://github.com/screamuch/chaos-dotfiles`
3. `etc` contents (!) go in `/etc/`
4. `wallpapers` go in `$HOME/Pictures`
5. `.config`, `.screenlayout`, all other files (except `README.md` and `.git`) go in `$HOME`
6. Set up ly: `# systemctl enable ly.service`
7. `$ chsh --shell /bin/fish $USER`

## Install application software

### First priority

- `$ yay -S zoom slack-desktop spotify telegram-desktop steam fiji-bin typora audacity natural-scrolling-forever`
- `$ yay -S ungoogled-chromium`
- `https://docs.conda.io/en/latest/miniconda.html`
- Install vimplug for neovim
- In `nvim` run `:PlugInstall`

### Not that necessary, KDE things I liked

`# pacman -S kdeconnect`
`# pacman -S kate`
`# pacman -S konsole`

