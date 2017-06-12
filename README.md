# LATEX GUI
## Why? 
I thought that having a little gui showing logs and compiling options 
would be more pleasant than the actual latex-vim-suite solutions for compiling. 

## Demo 
![demo](http://i.imgur.com/Rzn29eK.gif)

## Dependencies

* PyQt5
* [vim-dispatch plugin](https://github.com/tpope/vim-dispatch) (Or at least a plugin allowing multithreading in vim)

## Usage 
Write this line in your .vimrc:

```vimscript

   nnoremap <key_of_your_choice> :Start! python /path/to/the/script %:p<CR> 

```

 


