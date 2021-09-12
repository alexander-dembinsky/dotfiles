
local map = vim.api.nvim_set_keymap
local default_opts = {noremap = true, silent = true}

map('n', '<C-n>', ':NvimTreeToggle<CR>', default_opts)       -- open/close
map('n', '<leader>r', ':NvimTreeRefresh<CR>', default_opts)  -- refresh
map('n', '<leader>n', ':NvimTreeFindFile<CR>', default_opts) -- search file

map('n', '<C-l>', ':<C-u>nohl<cr><C-l>', default_opts)


map('n', '<leader>ff', ':Telescope find_files<cr>', default_opts)
map('n', '<leader>fg', ':Telescope live_grep<cr>', default_opts)
map('n', '<leader>fb', ':Telescope buffers<cr>', default_opts)
map('n', '<leader>fh', ':Telescope help_tags<cr>', default_opts)
