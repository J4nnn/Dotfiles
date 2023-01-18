call plug#begin('~/.config/nvim/plugged')

  " Autopairs
  Plug 'jiangmiao/auto-pairs'

  " Airline
  Plug 'vim-airline/vim-airline'
  Plug 'vim-airline/vim-airline-themes'

  " Autoclose tags
  Plug 'alvan/vim-closetag'

  " Icons
  Plug 'ryanoasis/vim-devicons'

  " NerdTree
  Plug 'preservim/nerdtree'

  " IntelliSense
  Plug 'neoclide/coc.nvim', {'branch': 'release'}
  Plug 'sheerun/vim-polyglot'

  " Live server
  Plug 'manzeloth/live-server'

  " Themes
  Plug 'joshdick/onedark.vim'
  Plug 'tomasiser/vim-code-dark'
  Plug 'crusoexia/vim-monokai'
  Plug 'ayu-theme/ayu-vim'
  Plug 'dracula/vim', { 'as': 'dracula' }
  Plug 'phanviet/vim-monokai-pro'
  Plug 'morhetz/gruvbox'
  Plug 'rose-pine/neovim'
  Plug 'kaicataldo/material.vim', { 'branch': 'main' }
call plug#end()
