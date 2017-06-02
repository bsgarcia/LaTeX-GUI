# VIM LATEX GUI
## Why? 
I thought that having a little gui showing logs and compiler options could be nice. 

## Demo 
![demo](http://i.imgur.com/Rzn29eK.gif)

## Dependencies

* PyQt5
* vim-do plugin

## Usage 

Write this line in your .vimrc:

```vimscript

   nnoremap <key_of_your_choice> :DoQuietly python /path/to/the/script %:p<CR> 

```

 


