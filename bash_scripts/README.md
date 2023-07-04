# Bash Scripts
Bash scripts make a lot easier as it is able to make several commands run, one after the other, without the user having to enter them. 
Here are some bash scripts I use including the python scripts in the [parent directory](../python-and-I) that generates ASCII value in order to encrypt the message and decodes secret messages in ascii form, repectively.

***Please, you may want to see the general instructions on [How to use scripts on your CLI](#usage) before using any of these scripts***

In this directory are the following:
### 0. [0-git_add](./0-git_add)
A script that makes it easier for you to push to git on shell without having to enter:

`git add <file_path>`

`git commit -m '<commit message>'`

`git push`

When you run this script, it prints a prompt for you to enter the file path or the file you wish to push, after which it let's you enter your commit message without the command or `-m` or quotation marks (' ', " "), and then the file(s) is/are pushed to git automatically.

Note that you can simply enter dot (".") to add everything in the current directory to pushed to git, just the same way you enter dot to `git add`, as in; `git add .`

### 1. [1-git_rm](./1-git_rm)
This script works just like **0-git_add**, described above, but rather removes from git the file that you pass to it.

### 2. [2-git_rm_dir](./2-git_rm_dir)
This script works like *1-git_rm* but recursively removes a sub-directory in the repository and all of its content

### 3. [3-git_clone](./3-git_clone)
For me, I saved all of this as `g`, so that if I did `g <the_github_ssh_link>`, the repository will be cloned. In other words, I don't have to enter `git clone`.
The script might not make enough sense to you if you don't know how to use **ssh**, the script for those who use http and PAT (personal access token) to git clone is actually, [5-clone_with_my_PAT](./5-clone_with_my_PAT).

### 4. [4-emacs_on_bash](./4-emacs_on_bash)
This script will be very useful to you if you have emacs intalled on your PC or virtual machine that has a GUI (graphical user interface). The command in the script stops emacs from popping out as a separate window with clickable buttons, and this is for those who prefer using emacs directly on the terminal. As for me, I saved the script as `e`, so that I use the command `e <file>` to open a file in emacs directly on the terminal.

### 5. [5-clone_with_my_PAT](./5-clone_with_my_PAT)
This script clones a repository with your PAT automatically added to it. All you need to do is to pass the username of the owner of the name of the repo as 2 arguments to it. For example `./5-clone_with_my_PAT tpauldike python-and-I`.

In the above example, the username is *tpauldike* and the repository is *python-and-I*. You may not want that long name for the script (like me), simply rename the script to anything short and it will still work.

It is very important for you to know that, you have to edit this particular file and add your PAT, otherwise, it will not do the work. To do that, go to this line:
```bash
PAT='[your_PAT]'
```

Replace the template with your PAT as shown below:
```bash
PAT='ghgaKihkadjiwlLkjai898&l90'
```

And you are good to go, provided you follow the general instructions on [How to use these scripts](#usage).

## <a name="usage"></a>How to use scripts on your CLI:
- Copy and paste or type the codes into a file (use any simple and short name of your choice for the file, not necessarily the name used here)
- Make the file executable with the command `chmod u+x <file_name>`
- Move the file into your bin directory to make it global, `sudo mv <file> /bin` or `sudo mv <file> /usr/bin`.
- Run your script from anywhere on your terminal by simply entering the name. *If the sudo command is not available in your OS, you might not be able to move it to `/bin`, you have to run the file by entering `./<file>` in the directory where the executable file is present.*