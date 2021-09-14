
local map = vim.api.nvim_set_keymap
local default_opts = {noremap = true, silent = true}


map('n', '<C-l>', ':<C-u>nohl<cr><C-l>', default_opts)



