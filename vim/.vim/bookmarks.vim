vim9script 

g:BookmarksFile = expand('~/.vim_bookmarks')

def PrintError(msg: string)
   echohl ErrorMsg
   echo msg
   echohl None
enddef

def EchoBookmarkDoesNotExists(bookmarkName: string) 
    PrintError('Bookmark "' .. bookmarkName .. '" does not exist')
enddef

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
    var bookmarks = GetBookmarks()
    const targetPath = expand(directoryPath)

    if !isdirectory(targetPath)
        PrintError('"' .. targetPath .. '" is not a valid directory')
        return
    else
        bookmarks[bookmarkName] = targetPath
        SaveBookmarks(bookmarks)
    endif
enddef

def BookmarkCWD(bookmarkName: string)
    const cwd = getcwd()
    BookmarkDirectory(bookmarkName, cwd)
enddef

def BookmarkCD(bookmarkName: string)
    const bookmarks = GetBookmarks()
    if !bookmarks->has_key(bookmarkName)
       EchoBookmarkDoesNotExists(bookmarkName)
       return
    endif
    exec 'cd ' .. bookmarks[bookmarkName]
enddef

def BookmarkDelete(bookmarkName: string)
    final bookmarks = GetBookmarks()
    if !bookmarks->has_key(bookmarkName)
       EchoBookmarkDoesNotExists(bookmarkName)
       return
    endif
    
    bookmarks->remove(bookmarkName)
    SaveBookmarks(bookmarks)
    echom 'Bookmark "' .. bookmarkName .. '" has been deleted'
enddef

def CompleteBookmarkList(ArgLead: string, CmdLine: string, CursorPos: number): list<string>
    return GetBookmarks()->keys()
enddef

command! -nargs=* -complete=dir BookmarkDir call BookmarkDirectory(<f-args>)
command! -nargs=1 BookmarkCWD call BookmarkCWD(<f-args>)
command! -nargs=1 -complete=customlist,CompleteBookmarkList BookmarkCD call BookmarkCD(<f-args>)
command! -nargs=1 -complete=customlist,CompleteBookmarkList BookmarkDelete call BookmarkDelete(<f-args>)

