
export PATH=$PATH:/home/dan/bin
export EDITOR=emacs
alias ls="ls -lv --group-directories-first"

# Set up the prompt

autoload -Uz promptinit
promptinit
prompt adam2

# Use emacs keybindings even if our EDITOR is set to vi
bindkey -e

# Keep 1000 lines of history within the shell and save it to ~/.zsh_history:
HISTSIZE=1000
SAVEHIST=1000
HISTFILE=~/.zsh_history

# Use modern completion system
autoload -Uz compinit
compinit

zstyle ':completion:*' auto-description 'specify: %d'
zstyle ':completion:*' completer _expand _complete _correct _approximate
zstyle ':completion:*' format 'Completing %d'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' menu select=2
eval "$(dircolors -b)"
zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' list-colors ''
zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' matcher-list '' 'm:{a-z}={A-Z}' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=* l:|=*'
zstyle ':completion:*' menu select=long
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle ':completion:*' use-compctl false
zstyle ':completion:*' verbose true

zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'
zstyle ':completion:*:kill:*' command 'ps -u $USER -o pid,%cpu,tty,cputime,cmd'


# Lisp config.
export CL_SOURCE_REGISTRY="/home/dan/PROJECTS/lisp/asdf-systems:/usr/share/common-lisp/systems"

# Fix broken memcpy() vs memmove() on flash and others.
#export LD_PRELOAD=/usr/lib/libc/memcpy-preload_32bit.so
#export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libc/memcpy-preload.so

# Run ruby gems.
export PATH=$PATH:/home/dan/.gem/ruby/1.9.1/bin

# Configure ccache to write to the drive with plenty of extra space.
export USE_CCACHE=1
export CCACHE_DIR=/home/dan/.ccache


