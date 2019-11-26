GitHub CLI

# Config User / Mail
git config --global user.email "antoine.ratat@gmail.com"
git config --global user.name "Antoine"
git remote add origin https://github.com/antoineratat/test_repo.git
git push -u origin master


Basic CLI

git init # Creates a new Git repository
git status # Inspects the contents of the working directory and staging area
git add # Adds files from the working directory to the staging area
git diff # Shows the difference between the working directory and the staging area
git commit -m "comments" # Permanently stores file changes from the staging area in the repository
git log # Shows a list of all previous commits


BackTrack CLI

git show HEAD # Display everything the git log command displays for the HEAD commit, plus all the file changes that were committed.
git checkout HEAD filename # Restore the file in your working directory to look exactly as it did when you last made a commit.
git reset HEAD filename # This command resets the file in the staging area to be the same as the HEAD commit.
git reset commit_SHA # This command works by using the first 7 characters of the SHA of a previous commit


Branch CLI

git branch # Lists all a Git project’s branches.
git branch branch_name # Creates a new branch.
git checkout branch_name # Used to switch from one branch to another.
git merge branch_name # Used to join file changes from one branch to another.
git branch -d branch_name # Deletes the branch specified.


TeamWork CLI

git clone # Creates a local copy of a remote.
git remote -v # Lists a Git project’s remotes.
git fetch # Fetches work from the remote into the local copy.
git merge origin/master # Merges origin/master into your local branch.
git push origin <branch_name> # Pushes a local branch to the origin remote.
