local map = vim.api.nvim_set_keymap
local default_opts = {noremap = true, silent = true}

map('n', '<leader>ff', ':Telescope find_files<cr>', default_opts)
map('n', '<leader>fg', ':Telescope live_grep<cr>', default_opts)
map('n', '<leader>fb', ':Telescope buffers<cr>', default_opts)
map('n', '<leader>fh', ':Telescope help_tags<cr>', default_opts)
