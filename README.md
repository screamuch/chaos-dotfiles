# chaos ([ex-zeus] 2-head desktop) dotfiles

## Install base system

- Do what you gotta do - this is an arch-based config
- Make swap and fat32 efi boot partitions
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

- `# pacman -S networkmanager git yay`
- `# pacman -S qtile alacritty copyq dmenu dunst fish gtop htop libinput micro neofetch nitrogen picom pulsemixer libqalculate qutebrowser rofi rofi-emoji filelight xterm thunar`
- `$ yay -S ly pfetch ttf-apple-emoji noto-fonts-emoji-apple otf-code-new-roman`
- `$ systemctl enable NetworkManager`

## Unpack configs and set up X

1. `etc` contents (!) go in `/etc/`
2. `wallpapers` go in `$HOME/Pictures`
3. `.config`, `.screenlayout`, all other files (except `README.md` and `.git`) go in `$HOME`
4. Set up ly: `# systemctl enable ly.service`
5. `$ chsh --shell /bin/fish $USER`

## Install application software

### First priority

- `$ yay -S zoom slack spotify telegram-desktop steam fiji-bin typora audacity natural-scrolling-forever`
- `$ yay -S ungoogled-chromium`
- `https://docs.conda.io/en/latest/miniconda.html`
- In `nvim` run `:PlugInstall`

### Not that necessary, KDE things I liked

`# pacman -S kdeconnect`
`# pacman -S kate`
`# pacman -S konsole`

