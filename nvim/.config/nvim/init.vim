filetype plugin on
set number
set relativenumber
syn on
set noswapfile
set mouse=a
set clipboard=unnamedplus
set hidden

set background=dark
set termguicolors
let g:airline_theme="hybrid"

colorscheme codedark

lua require "init"

source ~/.config/nvim/keymaps.vim
source ~/.config/nvim/nvim-tree.vim
source ~/.config/nvim/coc.vim
source ~/.config/nvim/telescope.vim

" Language specific remaps
au Filetype json source ~/.config/nvim/json.vim
au Filetype typescript source ~/.config/nvim/typescript.vim

