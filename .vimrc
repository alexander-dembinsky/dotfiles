filetype plugin on

""" Common Properties 
set nocompatible
set hidden 
set nu " Line numbers
set relativenumber " Relative line numbers
syn on " Enable syntax highlighting
set nowrap " Do not wrap text
set shiftwidth=2 " One tab == four spaces.
set tabstop=2 " One tab == four spaces.
set noswapfile " Diable swap files
set list
set listchars=tab:<-> " Highlight tabs and spaces
set expandtab " Use spaces instead of tabs
set nohlsearch " Do not highlight search results
set noeb vb t_vb= " Disable beeping

set path+=** " Recursive file search
set wildmenu
set wildignore=**/node_modules/**,**/.git/**,**/__pycache__/**

set suffixesadd+=.ts " Suffixes for 'gf' command

""" Plugins 
call plug#begin('~/.vim/plugged')

" Fuzzy finder
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'

" Color schemes ---
Plug 'morhetz/gruvbox' " Gruvbox Color Scheme
Plug 'wadackel/vim-dogrun'
Plug 'kristijanhusak/vim-hybrid-material'
 
" Git integration 
Plug 'tpope/vim-fugitive'
Plug 'airblade/vim-gitgutter'
map <leader>gs :G<CR>
map <leader>gj :diffget //3<CR>
map <leader>gf :diffget //2<CR>

" Snippets
Plug 'SirVer/ultisnips'
let g:UltiSnipsSnippetDirectories=[$HOME.'/.vim/UltiSnips']

" Editing
Plug 'tpope/vim-commentary'
Plug 'tpope/vim-surround'

" Vim Airline
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" NERDTree
Plug 'preservim/nerdtree'

" Language server protocols
Plug 'prabirshrestha/vim-lsp'
Plug 'mattn/vim-lsp-settings'
Plug 'prabirshrestha/asyncomplete.vim'
Plug 'prabirshrestha/asyncomplete-lsp.vim'

function! s:on_lsp_buffer_enabled() abort
    setlocal omnifunc=lsp#complete
    setlocal signcolumn=yes

    if exists('+tagfunc') | setlocal tagfunc=lsp#tagfunc | endif
    nmap <buffer> gd <plug>(lsp-definition)
    nmap <buffer> gs <plug>(lsp-document-symbol-search)
    nmap <buffer> gS <plug>(lsp-workspace-symbol-search)
    nmap <buffer> gr <plug>(lsp-references)
    nmap <buffer> gi <plug>(lsp-implementation)
    " nmap <buffer> gt <plug>(lsp-type-definition)
    nmap <buffer> <leader>rn <plug>(lsp-rename)
    nmap <buffer> [g <plug>(lsp-previous-diagnostic)
    nmap <buffer> ]g <plug>(lsp-next-diagnostic)
    nmap <buffer> K <plug>(lsp-hover)
    inoremap <buffer> <expr><c-f> lsp#scroll(+4)
    inoremap <buffer> <expr><c-d> lsp#scroll(-4)

    nnoremap <F3> :LspDocumentDiagnostic<CR>

    nnoremap <leader>fd :LspDocumentFormat<CR>
    nnoremap <leader>ca :LspCodeAction<CR>
endfunction

augroup lsp_install
    au!
    " call s:on_lsp_buffer_enabled only for languages that has the server registered.
    autocmd User lsp_buffer_enabled call s:on_lsp_buffer_enabled()
augroup END

" Unit Testing
Plug 'vim-test/vim-test'

call plug#end()

""" Current color scheme
set background=dark
colorscheme hybrid_material
let g:airline_theme = "hybrid"
""" Vim cursor support for Windows Terminal application
if &term =~ '^xterm'
  " normal mode
  let &t_EI .= "\<Esc>[0 q"
  " insert mode
  let &t_SI .= "\<Esc>[6 q"
endif

""" Key bindings

" Disable arrows
noremap <Left> <Nop>
noremap <Right> <Nop>
noremap <Up> <Nop>
noremap <Down> <Nop>
" Diable backspace and Del key in insert mode
inoremap <BS> <Nop>
inoremap <Del> <Nop>

" Clear highlighting
nnoremap <silent> <C-l> :<C-u>nohl<cr><C-l>

" FZF
nmap <leader>ff :Files<cr>
nmap <leader>fl :Lines<cr>
nmap <leader>fb :Buffers<cr>
nmap <leader>fm :Marks<cr>
nmap <leader>fc :Commits<cr>
nmap <leader>fw :Windows<cr>

" Switch between buffers
nmap [b :bp<cr>
nmap ]b :bn<cr>

" Switch between quickfix entries
nmap [c :cprev<cr>
nmap ]c :cnext<cr>
nmap <leader>co :copen<cr>
nmap <leader>cc :cclose<cr>

" Switch between location entries
nmap [l :lprev<cr>
nmap ]l :lnext<cr>
nmap <leader>lo :lopen<cr>
nmap <leader>lc :lclose<cr>

" Autocomplete
inoremap <expr> <Tab>   pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"
inoremap <expr> <cr>    pumvisible() ? asyncomplete#close_popup() : "\<cr>"

" Unit testing
nmap <leader>tn :TestNearest<CR>
nmap <leader>tf :TestFile<CR>
nmap <leader>ts :TestSuite<CR>
nmap <leader>tl :TestLast<CR>
nmap <leader>tv :TestVisit<CR>

" Jest
let test#javascript#jest#executable = 'npx jest --runTestsByPath'

" New line in insert mode
imap <leader>o <C-O>o
imap <leader>O <C-O>O

" NERDTree
nnoremap <F7> :NERDTreeToggle<cr>
nnoremap <leader><Tab> :NERDTreeFocus<cr>
nnoremap <leader>nf :NERDTreeFind<cr>
