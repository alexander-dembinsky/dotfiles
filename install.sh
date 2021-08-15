#/usr/bin/env bash

echo -e "\nInstalling packages...\n"
sudo pacman --noconfirm --needed -S git \
       	python \
        python-setuptools \
        python-pip \
        qtile \
        dunst \
        alacritty \
        volumeicon \
        network-manager-applet \
        variety \
        jgmenu \
        picom \
        blueman \
        nitrogen \
        sxhkd \
        gvim \
        curl \
        conky

script_dir="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

echo -e "\nInstalling vim-plug...\n"
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

echo -e "\nCreating symlinks...\n"
rm -Rf $HOME/.config/qtile
ln -s "$script_dir/.config/qtile" $HOME/.config/qtile

rm -Rf $HOME/.config/alacritty
ln -s "$script_dir/.config/alacritty" $HOME/.config/alacritty

rm $HOME/.vimrc
ln -s "$script_dir/.vimrc" $HOME/.vimrc

