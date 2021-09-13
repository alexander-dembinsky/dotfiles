local map = vim.api.nvim_set_keymap
local default_opts = {noremap = true, silent = true}

map('n', '<leader>ff', ':Telescope find_files<cr>', default_opts)
map('n', '<leader>fg', ':Telescope live_grep<cr>', default_opts)
map('n', '<leader>fb', ':Telescope buffers<cr>', default_opts)
map('n', '<leader>fh', ':Telescope help_tags<cr>', default_opts)

-- Search dotfiles
map('n', '<leader>fd', ':lua require("telescope.builtin").git_files({cwd = "~/dotfiles"})<CR>', default_opts)

-- Lsp

map('n', '<leader>gd', ':Telescope lsp_definitions<CR>', default_opts)
map('n', '<leader>gr', ':Telescope lsp_references<CR>', default_opts)
map('n', '<leader>gi', ':Telescope lsp_implementations<CR>', default_opts)
map('n', '<leader>gi', ':Telescope lsp_implementations<CR>', default_opts)
map('n', '<leader>ge', ':Telescope lsp_document_diagnostics<CR>', default_opts)
