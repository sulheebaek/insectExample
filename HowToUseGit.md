# How to use git commands
## Installation
```
$ sudo apt install git 
```

## Initializing local git repository
```
$ git init
```

## Downloading source code from the remote git repository to the local 
```
$ git clone https://github.com/sulheebaek/aal
$ git config --global user.email "youremail@yourdomain"
$ git config --global user.name "Your name"
```

After cloning the remote repository to your local repository, you would modify some code and want to update your code changes to the remote. In that case, please check your code availability -- whether it works or not -- before pushing you changes.

## Checkout a specific commit
To checkout a specific commited version, you need to know the exact identifer, and checkout the version to your local repository.
```
$ git log --reverse

commit 7e67c3b8d7d548f8b142635a97b93ed9e12ba2bd
Author: Sulhee Baek <mongsun2@gmail.com>
Date:   Wed Jan 30 21:57:12 2019 +0900

    removed home.css, base.css, home.html, base.html since they were just for test.

commit 335ba6c7129dd7fb88e861d22286a6da11de5f3d
Author: SeRyoung Park <parksr2004@naver.com>
Date:   Fri Feb 1 12:46:45 2019 +0900

    visualize update

commit cb88d1a68936813f05ec5c46ef010ef0bc16a538
Author: Linh-An <linhan90@gmail.com>
Date:   Tue Feb 5 22:27:01 2019 -0800

    Update preprocessing app

    Screenshot in demo folder
```
```
$ git checkout 7e67c3b8d7d548f8b142635a97b93ed9e12ba2bd
```

## Checking code changes
```
$ git status
```

## Adding(Applying) all the changes
```
$ git add -A
```

## Committing
```
$ git commit -m "Contents to be added by this commit"
```

## Pushing
```
$ git push -u origin master
```
Here, _origin_ is username and _master_ is branch name.

## Pull: updating your local repository to be same with the remote repository
```
$ git pull
```

## How to resolve git aborting.
Use git stash to store your changes and retrieve them after pulling from remote.
```
$ git stash
$ git pull
$ git status
$ git add modified_file1
$ git add modified_file2
$ git stash pop
$ git commit -m "commit message"
$ git push -u origin master
```

## Browsing up to date code changes
Open web-browser and access to our git url.
https://github.com/sulheebaek/aal
