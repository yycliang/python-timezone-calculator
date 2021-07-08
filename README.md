# Python Project Template

This is a template repository. That means you can make a copy of it using the "Use This Template" button, and you'll get a prompt to create your own repository based on this one. THEN you can clone it down.

## Committing

To commit your code you need to run three steps:

Step 1 - Select which files (`.` means "all").
```bash
git add .
```

Step 2 - Name the commit. 
```bash
git commit -m "description of changes"
```

Step 3 - Send the changes to GitHub.
```bash
git push
```


## Troubleshooting

If it's your first push ever, you may need to do some things to configure your environment. The most common is this:

```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

Be sure to replace the email and name with your email and your name.

If it's your first push on a specific project, you may need to specify which branch to push to.

```bash
git push --set-upstream origin master
```

At any time, you can see how things are going by typing `git status`.
