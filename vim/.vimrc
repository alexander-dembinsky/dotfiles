vim9script

# Enable syntax highlighting
syn on

# Line numbers
set nu
set relativenumber

# Default indentation options
set expandtab
set tabstop=4
set shiftwidth=4
set autoindent

# Mouse support
set mouse=a

# Hidden buffers
set hidden

# Enable filetype plugin
filetype plugin on

# Wildmenu 
set wildmenu wildoptions=pum
set wildcharm=<C-z>

# Recursive search of files
set path+=**

# Key mappings

# Quickly get out of insert mode
imap jj <ESC>

# Switch between buffers
nmap <leader>b :buffer <C-z>

# Find files
nmap <leader>f :find 

# Bookmarks for working directories
import expand("~/.vim/bookmarks.vim")

nmap <leader>cd :BookmarkCD <C-z>

# Colorscheme
colorscheme desert

# Plugins
call plug#begin()

# Git
Plug 'tpope/vim-fugitive'

call plug#end()
