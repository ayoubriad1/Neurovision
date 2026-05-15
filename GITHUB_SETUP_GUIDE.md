# 📘 Complete GitHub Setup & Upload Guide for Neurovision

This guide walks you through every step needed to create a GitHub repository and upload the Neurovision project. No prior Git experience required!

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Create GitHub Repository](#create-github-repository)
3. [Local Git Setup](#local-git-setup)
4. [First Commit & Push](#first-commit--push)
5. [Advanced Git Operations](#advanced-git-operations)
6. [Verification Checklist](#verification-checklist)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before you begin, make sure you have:

### 1. Git Installation
Check if Git is installed:
```bash
git --version
```

**If not installed:**
- **Windows:** Download from https://git-scm.com/download/win
- **macOS:** `brew install git`
- **Linux:** `sudo apt-get install git`

### 2. GitHub Account
- Go to https://github.com
- Click **Sign up** and create a free account
- Verify your email address

### 3. Git Configuration
Set your Git identity (one-time setup):
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Verify configuration:
```bash
git config --global user.name
git config --global user.email
```

---

## Create GitHub Repository

### Step 1: Create Empty Repository on GitHub

1. Log in to GitHub at https://github.com
2. Click the **+** icon (top right) → **New repository**
3. Fill in the form:

| Field | Value | Notes |
|-------|-------|-------|
| **Repository name** | `neurovision` | Use lowercase, hyphens OK |
| **Description** | Brain-target affinity visualization tool | Optional but recommended |
| **Public/Private** | Public | Makes it visible to others |
| **Initialize with README** | ❌ **UNCHECK** | We already have README.md |
| **Add .gitignore** | ❌ **UNCHECK** | We already have .gitignore |
| **.gitignore template** | Python | (Skip if unchecked) |
| **Add a license** | MIT License | Or choose manually later |

4. Click **Create repository**

✅ **Result:** Empty repository created at `https://github.com/YOUR_USERNAME/neurovision`

---

## Local Git Setup

### Step 2: Initialize Git in Your Local Folder

Navigate to the Neurovision folder and initialize Git:

```bash
# Navigate to your Neurovision folder
cd /path/to/Neurovision

# Initialize Git repository
git init
```

**Output:**
```
Initialized empty Git repository in /path/to/Neurovision/.git/
```

### Step 3: Add Remote Repository Link

Connect your local folder to the GitHub repository you created:

```bash
git remote add origin https://github.com/YOUR_USERNAME/neurovision.git
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

**Verify the connection:**
```bash
git remote -v
```

**Expected output:**
```
origin  https://github.com/YOUR_USERNAME/neurovision.git (fetch)
origin  https://github.com/YOUR_USERNAME/neurovision.git (push)
```

### Step 4: Check Git Status

Before committing, see what files Git sees:

```bash
git status
```

**Expected output:**
```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
    .gitignore
    CONTRIBUTING.md
    LICENSE
    README.md
    app.py
    brain_regions.py
    requirements.txt
    visualization.py
```

---

## First Commit & Push

### Step 5: Stage All Files

Add all files to the **staging area** (ready to commit):

```bash
git add .
```

**Verify files are staged:**
```bash
git status
```

**Expected output:**
```
On branch master

No commits yet

Changes to be committed:
  (use "rm --cached <file>..." to unstage)
    new file:   .gitignore
    new file:   CONTRIBUTING.md
    new file:   LICENSE
    new file:   README.md
    new file:   app.py
    new file:   brain_regions.py
    new file:   requirements.txt
    new file:   visualization.py
```

### Step 6: Make Your First Commit

Create a snapshot of your project:

```bash
git commit -m "Initial commit: Add Neurovision brain visualization tool"
```

**Message format:**
```
git commit -m "DESCRIPTION OF CHANGES"
```

**Good commit messages:**
- ✅ `"Initial commit: Add Neurovision brain visualization tool"`
- ✅ `"Add 3D brain surface rendering with 8 anatomical views"`
- ✅ `"Fix kcal/mol conversion formula"`

**Bad commit messages:**
- ❌ `"fix"`
- ❌ `"update"`
- ❌ `"asdf"`

**Expected output:**
```
[master (root-commit) a1b2c3d] Initial commit: Add Neurovision brain visualization tool
 8 files changed, 2847 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 CONTRIBUTING.md
 create mode 100644 LICENSE
 create mode 100644 README.md
 create mode 100644 app.py
 create mode 100644 brain_regions.py
 create mode 100644 requirements.txt
 create mode 100644 visualization.py
```

### Step 7: Push to GitHub

Upload your local commits to GitHub:

```bash
git branch -M main
git push -u origin main
```

**What this does:**
- `git branch -M main` — Renames the default branch to `main` (GitHub standard)
- `git push -u origin main` — Uploads commits to GitHub (`-u` sets it as default for future pushes)

**First-time push note:**  
GitHub may ask you to authenticate:
- **If using HTTPS:** Enter your GitHub username and a **personal access token** (see [Create PAT](#create-personal-access-token))
- **If using SSH:** Your SSH key handles authentication automatically (see [Setup SSH](#setup-ssh-optional))

**Expected output:**
```
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 8 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 2.8 KiB | 2.8 MiB/s, done.
Total 8 (delta 0), reused 0 (delta 0), pack-reused 0
 * [new branch]      main -> main
Branch 'main' is set to track remote branch 'main' from 'origin'.
```

✅ **Success!** Your project is now on GitHub.

---

## Authentication Methods

### Option A: Personal Access Token (Recommended)

**Step 1: Create a PAT on GitHub**

1. Go to GitHub Settings → [Developer settings](https://github.com/settings/tokens)
2. Click **Generate new token** → **Generate new token (classic)**
3. Configure:
   - **Token name:** `neurovision-upload`
   - **Expiration:** 90 days (or longer)
   - **Scopes:** Check `repo` (grants access to repositories)
4. Click **Generate token**
5. **⚠️ Copy the token immediately** (you won't see it again!)

**Step 2: Use Token for Git**

When Git asks for a password:
- **Username:** Your GitHub username
- **Password:** Paste the token you just created

**Store token for future use:**
```bash
# Windows
git config --global credential.helper wincred

# macOS
git config --global credential.helper osxkeychain

# Linux
git config --global credential.helper cache
```

### Option B: SSH Key (Advanced)

SSH provides secure, passwordless authentication.

**Step 1: Generate SSH Key**

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

**Step 2: Save SSH Key**
- When prompted for location, press **Enter** (saves to default location)
- When prompted for passphrase, you can press **Enter** (or set a passphrase)

**Step 3: Copy Public Key**

```bash
# Windows (PowerShell)
type $env:USERPROFILE\.ssh\id_ed25519.pub | Set-Clipboard

# macOS/Linux
cat ~/.ssh/id_ed25519.pub | pbcopy
```

**Step 4: Add Key to GitHub**

1. Go to GitHub Settings → [SSH and GPG keys](https://github.com/settings/keys)
2. Click **New SSH key**
3. **Title:** `neurovision-machine`
4. **Key:** Paste your public key (Ctrl+V)
5. Click **Add SSH key**

**Step 5: Use SSH for Git**

Update your remote URL:
```bash
git remote set-url origin git@github.com:YOUR_USERNAME/neurovision.git
```

Now future pushes won't require authentication!

---

## Advanced Git Operations

### Making Changes & Pushing Updates

After you modify files locally:

```bash
# 1. Check what changed
git status

# 2. Stage specific files (or use 'git add .' for all)
git add app.py visualization.py

# 3. Commit with descriptive message
git commit -m "Improve Gaussian blob generation for deep structures"

# 4. Push to GitHub
git push
```

### Working with Branches

For feature development without affecting the main project:

```bash
# Create a new branch
git checkout -b feature/add-export-to-nifti

# Make changes and commit normally
git add .
git commit -m "Add NIfTI export functionality"

# Push the new branch
git push -u origin feature/add-export-to-nifti

# On GitHub, create a Pull Request to merge back to main
# After review, merge the PR
```

### Viewing Commit History

```bash
# View all commits
git log

# View last 5 commits in compact format
git log --oneline -5

# View commits with visual branch graph
git log --graph --oneline --all
```

**Example output:**
```
a1b2c3d (HEAD -> main, origin/main) Initial commit: Add Neurovision brain visualization tool
```

### Undoing Mistakes

```bash
# Undo the last commit (keep changes)
git reset --soft HEAD~1

# Undo the last commit (discard changes)
git reset --hard HEAD~1

# View what was lost (reflog)
git reflog
```

---

## Verification Checklist

After pushing to GitHub, verify everything is correct:

### ✅ Checklist

- [ ] **Repository exists on GitHub**
  - Visit `https://github.com/YOUR_USERNAME/neurovision`
  - Should show your project with README displayed

- [ ] **All files are present**
  - app.py ✓
  - brain_regions.py ✓
  - visualization.py ✓
  - requirements.txt ✓
  - README.md ✓
  - LICENSE ✓
  - .gitignore ✓
  - CONTRIBUTING.md ✓

- [ ] **README displays properly**
  - Click on README.md in the GitHub repo
  - Markdown formatting should be visible (not raw code)

- [ ] **.gitignore is working**
  - No `__pycache__` folder on GitHub
  - No `.pyc` files on GitHub

- [ ] **License is correct**
  - GitHub shows "MIT License" badge
  - LICENSE file content is correct

### GitHub Repository Stats

Once verified, your GitHub repo should show:
```
XX commits (currently 1)
Files: 8
Language: Python (100%)
License: MIT
```

---

## Troubleshooting

### Common Issues & Solutions

#### ❌ "fatal: not a git repository"

**Cause:** Git not initialized in current directory

**Solution:**
```bash
git init
```

---

#### ❌ "fatal: 'origin' does not appear to be a 'git' repository"

**Cause:** Remote not set up correctly

**Solution:**
```bash
# Check current remotes
git remote -v

# Add the remote (replace YOUR_USERNAME!)
git remote add origin https://github.com/YOUR_USERNAME/neurovision.git

# Or update existing remote
git remote set-url origin https://github.com/YOUR_USERNAME/neurovision.git
```

---

#### ❌ "error: failed to push some refs to origin"

**Cause:** Remote has changes you don't have locally (or branch mismatch)

**Solution:**
```bash
# Fetch latest changes from GitHub
git fetch origin

# Pull changes into your local branch
git pull origin main

# Resolve any conflicts if necessary, then commit
git push origin main
```

---

#### ❌ "Please tell me who you are" when committing

**Cause:** Git user configuration not set

**Solution:**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

#### ❌ "fatal: Authentication failed"

**Cause:** Incorrect credentials

**Solutions:**
- **Using HTTPS:** Create a [Personal Access Token](#option-a-personal-access-token-recommended) and use that as password
- **Using SSH:** Verify SSH key is added to GitHub ([see SSH setup](#option-b-ssh-key-advanced))

---

#### ❌ Accidentally committed sensitive data

**Cause:** Private keys, API tokens, passwords committed

**Solution:** 
DO NOT use `git reset --hard` as it leaves history. Use [git filter-branch](https://git-scm.com/docs/git-filter-branch) or better yet, use [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)

---

### Getting Help

- **GitHub Docs:** https://docs.github.com/
- **Git Documentation:** https://git-scm.com/doc
- **Stack Overflow:** Tag questions with `git` and `github`

---

## Next Steps

### 1. Add Repository Topics
```
Settings → About → Topics
Add: brain-visualization, neuroscience, python, streamlit, neuroimaging
```

### 2. Enable Discussions
```
Settings → Features → Discussions (enable for community discussions)
```

### 3. Add GitHub Pages
```
Settings → Pages → Source: main branch
Adds documentation site at github.com/YOUR_USERNAME/neurovision
```

### 4. Add CI/CD (Optional)
Create `.github/workflows/test.yml` for automated testing.

### 5. Create Releases
```bash
git tag v1.0.0
git push origin v1.0.0
```
Then on GitHub, create a Release with download links.

---

## Summary of Commands

Quick reference for the entire workflow:

```bash
# Initial setup (one time)
git init
git remote add origin https://github.com/YOUR_USERNAME/neurovision.git

# First upload
git add .
git commit -m "Initial commit: Add Neurovision project"
git branch -M main
git push -u origin main

# Future updates
git add .
git commit -m "Description of changes"
git push
```

---

## Congratulations! 🎉

Your Neurovision project is now on GitHub and ready for collaboration. 

**Next:**
- Share the repository link: `https://github.com/YOUR_USERNAME/neurovision`
- Add collaborators via Settings → Collaborators
- Star your own repo! ⭐

---

**Last updated:** May 2026  
**Version:** 1.0.0
