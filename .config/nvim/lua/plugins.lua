vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function()
  use 'wbthomason/packer.nvim'

  -- Colorscheme
  use 'kristijanhusak/vim-hybrid-material'
  -- Nvim tree
  use {
    'kyazdani42/nvim-tree.lua',
    requires = 'kyazdani42/nvim-web-devicons'
  }
  -- Telescope 
  use {
    'nvim-telescope/telescope.nvim',
    requires = { {'nvim-lua/plenary.nvim'} }
  }
  -- Airline
  use { 
    'vim-airline/vim-airline',
    requires = { { 'vim-airline/vim-airline-themes' } }
  }
  -- COC
  use {'neoclide/coc.nvim', branch = 'release'}
  -- TreeSitter
  use {
    'nvim-treesitter/nvim-treesitter',
    run = ':TSUpdate'
  }
  -- Fugitive
  use {
    'tpope/vim-fugitive'
  }
end)

