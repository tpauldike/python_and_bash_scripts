# <a name="top"></a>Personal Bash Scripts
Bash scripts make a lot easier as it is able to make several commands run, one after the other, without the user having to enter them. 
Here are some bash scripts I use including the python scripts in the [parent directory](../python-and-I) that generates ASCII value in order to encrypt the message and decodes secret messages in ascii form, repectively.

***Please, you may want to see the general instructions, at the bottom of the README, on [How to use scripts on your CLI](#usage) before using any of these scripts***

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

### 3. [3-ssh_git_clone](./3-ssh_git_clone)
For me, I saved all of this as `g`, so that if I did either `g <repo>` or `g <ssh_link>`, the repository will be cloned. In other words, I don't have to enter `git clone <ssh_link>`. Entering *g* is sure faster than entering *git clone* but please choose a name that you can easily remember.
The script might not make enough sense to you if you don't know how to use **ssh**, the script for those who use http and PAT (personal access token) to git clone is actually, [5-clone_with_my_PAT](./5-clone_with_my_PAT).

Please beware that you need to replace the word *codetrybe* with your GitHub username, you'll find it in a few lines of [the code](./3-ssh_git_clone), as show below.
```bash
SSH_URL="^git@github\.com:codetrybe/[[:alnum:]_-]+\.git$"
```

```bash
elif [[ $1 =~ $REPO ]]; then
        git clone git@github.com:codetrybe/$1.git
```

### 4. [4-emacs_on_bash](./4-emacs_on_bash)
This script will be very useful to you if you have emacs intalled on your PC or virtual machine that has a GUI (graphical user interface). The command in the script stops emacs from popping out as a separate window with clickable buttons, and this is for those who prefer using emacs directly on the terminal. As for me, I saved the script as `e`, so that I use the command `e <file>` to open a file in emacs directly on the terminal.

### 5. [5-clone_with_my_PAT](./5-clone_with_my_PAT)
This script clones a repository with your PAT automatically added to it. All you need to do is to pass the username of the owner of the name of the repo as 2 arguments to it. For example `./5-clone_with_my_PAT tpauldike python_and_bash_scripts`.

In the above example, the username is *tpauldike* and the repository is *python_and_bash_scripts*. You may not want that long name for the script (like me), simply rename the script to anything short and it will still work.

It is very important for you to know that, you have to edit this particular file and add your PAT, otherwise, it will not do the work. To do that, go to this line:
```bash
PAT='[YOUR_PERSONAL-ACCESS-TOKEN]'
```

Replace the template with your PAT enclosed within single quotes, as illustrated below:
```bash
PAT='ghgaKihkadjiwlLkjai898&l90'
```

One more thing; replace the word *codetrybe* with your GitHub username, you find a line like this in [the script](./5-clone_with_my_PAT):
```bash
USER="codetrybe"
```

And you are good to go, provided you follow the general instructions on [How to use these scripts](#usage).

## <a name="usage"></a>How to use scripts on your CLI:
- Copy and paste or type the codes into a file (use any simple and short name of your choice for the file, not necessarily the name used here)
- Make the file executable with the command `chmod u+x <file_name>`
- Move the file into your bin directory to make it global, `sudo mv <file> /bin` or `sudo mv <file> /usr/bin`.
> *Please be very careful here, you could ruin your system if you make a mistake in this particular step*.
- Run your script from anywhere on your terminal by simply entering the name. *If the sudo command is not available in your OS, you might not be able to move it to `/bin`, you have to run the file by entering `./<file>` in the directory where the executable file is present.*

###### If you find anything confusing or difficult, please contact the author.
##### Author: [Topman Paul-Dike](./https://github.com/tpauldike) - [Twitter](https://twitter.com/tpauldike)
###### [scroll to the top](#top)
