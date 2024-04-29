# Git Guide: Pushing a Project to a Repository

This guide will walk you through the steps to push a local project to a remote Git repository.

## Step 1: Navigate to Your Project Directory

Open a terminal and navigate to your project directory using the `cd` command:

```bash
cd path/to/your/project
```

## Step 2: Initialize a Git Repository
Initialize a new Git repository in your project directory:
```bash
git init
```

## Step 3: Add Your Files
Add all the files in your project to the Git repository:
```bash
git add .
```

## Step 4: Commit Your Changes
Commit the changes with a message:
```bash
git commit -m "Your commit message"
```

## Step 5: Link Your Local Repository to the Remote Repository
Link your local repository to the remote repository:
```bash
git remote add origin your-repository-url
```
Replace your-repository-url with the URL of your remote repository.

## Step 6: Push Your Local Repository to the Remote Repository
Finally, push your local repository to the remote repository:
```bash
git push -u origin master
```

If you're asked for a username and password, enter your GitHub username and password.

Congratulations! You've now pushed your project to a remote Git repository.
