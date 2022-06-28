" 
" Use 'fzf' plugin to show list of bookmarks created in NERDTree.
"
" When user selects the bookmark, it will set NERDTree's root to the
" appropriate path.
"

let s:bookmarks = {}

func! s:Sink(choice) abort
  let [matched, bookmark, path; other] = matchlist(a:choice, '.\ \(.*\)\ (\(.*\))')
  exec 'cd ' . path
  exec 'NERDTreeFromBookmark ' . bookmark
endf

func! s:FormatBookmarkEntry(key, val)
  return '✎ ' . a:key . ' (' . a:val . ')'
endf

func! s:FuzzyBookmarks() abort
  if !filereadable(g:NERDTreeBookmarksFile)
    echo g:NERDTreeBookmarksFile . " is absent"
    return
  endif

  let bookmarkFileLines = readfile(g:NERDTreeBookmarksFile)
  
  for line in bookmarkFileLines
    if line == ''
      continue
    endif
    let [bookmark, path] = split(line)
    let s:bookmarks[bookmark] = path
  endfor

  let entries = values(map(s:bookmarks, function('s:FormatBookmarkEntry')))
  call fzf#run(fzf#wrap({'options': '--prompt "Bookmarks> "', 
               \'source': entries,
               \'sink': function('s:Sink'), 
               \}))
endf

command! Bookmarks call s:FuzzyBookmarks()

