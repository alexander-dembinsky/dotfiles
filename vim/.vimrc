" Enable syntax highlighting
syn on

" Line numbers
set nu
set relativenumber

" Default indentation options
set expandtab
set tabstop=4
set shiftwidth=4

" Mouse support
set mouse=a

" Hidden buffers
set hidden

" Enable filetype plugin
filetype plugin on

" Wildmenu 
set wildmenu wildoptions=pum
set wildcharm=<C-z>

" Recursive search of files
set path+=**

" Key mappings

" Quickly get out of insert mode
imap jj <ESC>

" Switch between buffers
nmap <leader>b :buffer <C-z>

" Find files
nmap <leader>f :find 

" Bookmarks for working directories
let g:BookmarksFile = expand('~') .. '/.vim_bookmarks'

def SaveBookmarks(bookmarks: dict<string>)
    call writefile([json_encode(bookmarks)], g:BookmarksFile)
enddef

def GetBookmarks(): dict<string>
    if !filereadable(g:BookmarksFile)
        return {}
    endif

    return json_decode(readfile(g:BookmarksFile)[0])
enddef

def BookmarkDirectory(bookmarkName: string, directoryPath: string) 
    echom 'Bookmark name ' .. bookmarkName .. ' will point to ' .. directoryPath .. ' and stored to ' .. g:BookmarksFile
    var bookmarks = g:GetBookmarks()
    bookmarks[bookmarkName] = directoryPath
    g:SaveBookmarks(bookmarks)
enddef

def BookmarkCWD(bookmarkName: string)
    const cwd = getcwd()
    g:BookmarkDirectory(bookmarkName, cwd)
enddef

def BookmarkCD(bookmarkName: string)
    const bookmarks = g:GetBookmarks()
    if !bookmarks->has_key(bookmarkName)
       echom 'Bookmark ' .. bookmarkName .. ' does not exist'
       return
    endif
    exec 'cd ' .. bookmarks[bookmarkName]
enddef

def CompleteBookmarkList(ArgLead: string, CmdLine: string, CursorPos: number): list<string>
    return g:GetBookmarks()->keys()
enddef

command! -nargs=* -complete=dir BookmarkDir call BookmarkDirectory(<f-args>)
command! -nargs=1 BookmarkCWD call BookmarkCWD(<f-args>)>
command! -nargs=1 -complete=customlist,CompleteBookmarkList BookmarkCD call BookmarkCD(<f-args>)

nmap <leader>cd :BookmarkCD <C-z>
