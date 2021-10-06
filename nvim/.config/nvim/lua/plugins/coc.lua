local map = vim.api.nvim_set_keymap
local default_opts = {noremap = true, silent = true}

map('n', '<leader>cd', ':CocDiagnostics<CR>', default_opts)
map('n', '<leader>cc', ':CocCommand<CR>', default_opts)
map('n', '<leader>ca', ':CocAction<CR>', default_opts)
