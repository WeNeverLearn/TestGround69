# Add this in '~/.bashrc' or .zshrc or ...
# Execute a command on opening the first terminal
# But don't execute when you open another tab/terminal

terminal_num=$(ls /dev/pts | grep -E "^[0-9]" | wc -l)
if [ "$terminal_num" -eq "1" ]
then
	# add_command_here
fi

# How this works:
# when you open a terminal,
# a new file with the name 'n'(n=0,1,2,.....) is created
# but there exists one other file in that directory: 'ptmax'
# ls /dev/pts : ls the directory
# grep -E "^[0-9]" : show items whose name starts with a number
# wc -l : count the number of lines (every line will have a different file)

