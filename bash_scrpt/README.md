# Bash Scripts
Bash scripts make a lot easier as it is able to make several commands run, one after the other, without the user having to enter them. 
Here are some bash scripts I use including the python scripts in the [parent directory](../python-and-I) that generates ASCII value in order to encrypt the message and decodes secret messages in ascii form, repectively.

In this directory are the following:
### [0-git_add](./0-git_add)
A script that makes it easier for you to push to git on shell without having to enter:

`git add <file_path>`

`git commit -m '<commit message>'`

`git push`

When you run this script, it prints a prompt for you to enter the file path or the file you wish to push, after which it let's you enter your commit message without the command or `-m` or quotation marks (' ', " "), and then the file(s) is/are pushed to git automatically.

### [1-git_rm](./1-git_rm)
This script works just like *0-git_add*, described above, but rather removes from git the file that you pass to it.

## How to use scripts on your CLI:
- Copy and paste or type the codes into a file (use any simple and short name of your choice for the file)
- Make the file executable with the command `chmod u+x <file_name>`
- Move the file into your bin directory to make it global, `mv <file> /bin` or `mv <file> /usr/bin`. You may use the `sudo` command if these do not work.
- Run your script from anywhere on your terminal by simply entering the name
