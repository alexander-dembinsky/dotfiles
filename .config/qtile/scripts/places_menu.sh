#!/usr/bin/env bash

FILEMAN="thunar"

(cat <<EOF
Home,     $FILEMAN $HOME            , folder-home
Downloads,$FILEMAN $HOME/Downloads  , folder-downloads
Documents,$FILEMAN $HOME/Documents  , folder-documents
Videos,   $FILEMAN $HOME/Videos     , folder-videos
Music,    $FILEMAN $HOME/Music      , folder-music
Pictures, $FILEMAN $HOME/Pictures   , folder-pictures
Dropbox,  $FILEMAN $HOME/Dropbox    , folder-dropbox
^sep()
SSD,      $FILEMAN /mnt/SSD         , drive-harddisk
HDD,      $FILEMAN /mnt/HDD         , drive-harddisk
EOF
) | jgmenu --simple --at-pointer --config-file=$HOME/.config/qtile/scripts/jgmenurc_places
