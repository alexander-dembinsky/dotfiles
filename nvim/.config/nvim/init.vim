syntax on
set number
set relativenumber
set expandtab
set tabstop=4
set shiftwidth=4
set mouse=a
set hidden
set wildcharm=<C-z>
let path = expand('~/.config/nvim')

imap jj <esc>
" Format all document
nmap <leader>F mmgg0vG$<leader>f'm

" List buffers
nmap <leader>b :buffer <C-z>

" Navigate between buffers
nmap ]b :bn<cr>
nmap [b :bp<cr>

call plug#begin()

" NERDTree
Plug 'ryanoasis/vim-devicons'
Plug 'preservim/nerdtree'

" Color Schemes
Plug 'rafi/awesome-vim-colorschemes'

" Git
Plug 'tpope/vim-fugitive'

" Comment out
Plug 'tpope/vim-commentary'

" FZF
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'

" Bookmarks
Plug 'alexander-dembinsky/bookmarks'

" CoC
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'SirVer/ultisnips'

" Tests
Plug 'vim-test/vim-test'

" Airline
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" Floaterm
Plug 'voldikss/vim-floaterm'

call plug#end()

set background=dark
colorscheme gruvbox

" Tree
nnoremap <C-n> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>
nnoremap <leader>n :NERDTreeFocus<CR>

" Fuzzy
nnoremap <silent> <expr> <leader><leader> (expand('%') =~ 'NERD_tree' ? "\<c-w>\<c-w>" : '').":FZF\<cr>"
nnoremap <leader>fl :BLines<CR>
nnoremap <leader>' :Bookmarks<CR>

" CoC
exec 'source' . path . '/coc.vim'
exec 'source' . path . '/java.vim'

" Tests
let test#strategy = 'floaterm'

nmap <silent> <leader>tn :TestNearest<CR>
nmap <silent> <leader>tf :TestFile<CR>
nmap <silent> <leader>ts :TestSuite<CR>
nmap <silent> <leader>tl :TestLast<CR>
nmap <silent> <leader>tv :TestVisit<CR>

" Airline
let g:airline#extensions#tabline#formatter = 'unique_tail'

" Floaterm
let g:floaterm_keymap_new    = '<F12>'
let g:floaterm_keymap_prev   = '[t'
let g:floaterm_keymap_next   = ']t'
let g:floaterm_keymap_first  = '{T'
let g:floaterm_keymap_last   = '}T'
let g:floaterm_keymap_hide   = ''
let g:floaterm_keymap_show   = ''
let g:floaterm_keymap_kill   = '<C-x>'
let g:floaterm_keymap_toggle = '<C-t>'

