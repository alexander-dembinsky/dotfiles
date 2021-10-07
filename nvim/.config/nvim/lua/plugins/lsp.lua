local map = vim.api.nvim_set_keymap
local default_opts = {noremap = true, silent = true}


require"lspconfig".tsserver.setup {}
require"lspconfig".rust_analyzer.setup {}
require"lspconfig".pyright.setup {}

