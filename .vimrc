filetype plugin on

""" Common Properties 
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
set hlsearch " Highlight search results
set clipboard=unnamed " Clipboard Copy/Paste
set guifont=JetBrainsMono\ Nerd\ Font\ Mono\ 13 
set guioptions-=T

set path+=** " Recursive file search
set wildmenu

""" Plugins 
call plug#begin('~/.vim/plugged')

" FZF Fuzzy finder plugin
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'

nnoremap <silent> <C-p> :call FZFOpen(':Files')<CR>

" Color schemes ---
Plug 'morhetz/gruvbox' " Gruvbox Color Scheme
Plug 'wadackel/vim-dogrun'

" Git integration 
Plug 'tpope/vim-fugitive'
map <leader>gs :G<CR>
map <leader>gj :diffget //3<CR>
map <leader>gf :diffget //2<CR>

" Vim Airline
Plug 'vim-airline/vim-airline'


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
    nnoremap <F1> :LspCodeAction<CR>

    "let g:lsp_format_sync_timeout = 1000
    "autocmd! BufWritePre *.rs,*.go,*.ts,*.py call execute('LspDocumentFormatSync')
    
    " refer to doc to add more commands
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
"colorscheme gruvbox
"set background=dark
"
colorscheme dogrun

""" Vim cursor support for Windows Terminal application
if &term =~ '^xterm'
  " normal mode
  let &t_EI .= "\<Esc>[0 q"
  " insert mode
  let &t_SI .= "\<Esc>[6 q"
endif

""" Key bindings
" List of windows
nnoremap <F5> :W<cr>

" Resizing splits
nmap <C-w><Right> :vert res +3<cr><C-w>
nmap <C-w><Left> :vert res -3<cr><C-w>

nmap <C-w><Up> :res +3<cr><C-w>
nmap <C-w><Down> :res -3<cr><C-w>

" Autocomplete
inoremap <expr> <Tab>   pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"
inoremap <expr> <cr>    pumvisible() ? asyncomplete#close_popup() : "\<cr>"

" Unit testing
nmap <silent> t<C-n> :TestNearest<CR>
nmap <silent> t<C-f> :TestFile<CR>
nmap <silent> t<C-s> :TestSuite<CR>
nmap <silent> t<C-l> :TestLast<CR>
nmap <silent> t<C-g> :TestVisit<CR>

" Jest
let test#javascript#jest#executable = 'npx jest --runTestsByPath'

" Grep Project
function! Grep()
    let pattern = input('Enter pattern: ')
    let path = input('Enter path: ', './**/*')
    set wildignore=*/node_modules/*
    exec "vimgrep /" . pattern . "/ " . path . " | :copen"
endfunction

nnoremap <F4> :call Grep()<CR>


