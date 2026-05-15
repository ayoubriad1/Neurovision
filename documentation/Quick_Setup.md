# ⚡ Neurovision: Quick Start Guide

Get your Neurovision project on GitHub in **5 minutes**!

---

## Step 1: Create GitHub Repository (2 minutes)

1. Go to https://github.com/new
2. Repository name: `neurovision`
3. Description: `Brain-target affinity visualization tool`
4. Choose **Public** (unless you want private)
5. **UNCHECK** "Initialize this repository with a README"
6. Click **Create repository**

✅ **Copy your repository URL:**
```
https://github.com/YOUR_USERNAME/neurovision
```

---

## Step 2: Setup Git Locally (2 minutes)

Open your terminal/command prompt in the Neurovision folder:

```bash
# Configure Git (first time only)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Initialize Git in this folder
git init

# Connect to GitHub (replace YOUR_USERNAME!)
git remote add origin https://github.com/YOUR_USERNAME/neurovision.git

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Add Neurovision brain visualization tool"

# Push to GitHub (rename branch to main)
git branch -M main
git push -u origin main
```

**GitHub will ask for login:**
- Username: Your GitHub username
- Password: Use a [Personal Access Token](GITHUB_SETUP_GUIDE.md#option-a-personal-access-token-recommended) instead of your password

---

## Step 3: Verify on GitHub (1 minute)

1. Visit `https://github.com/YOUR_USERNAME/neurovision`
2. You should see:
   - All your files listed
   - README.md displayed at the bottom
   - Green "✓ main" branch indicator

✅ **Done!** Your project is live on GitHub.

---

## Next Steps

- **Share the link:** Post `https://github.com/YOUR_USERNAME/neurovision` online
- **Make changes:** Edit files locally, then run:
  ```bash
  git add .
  git commit -m "Your change description"
  git push
  ```
- **Read full guide:** See [GITHUB_SETUP_GUIDE.md](GITHUB_SETUP_GUIDE.md) for detailed explanations

---

## Troubleshooting

### "Authentication failed"
Use a **Personal Access Token** instead of your GitHub password. See [GITHUB_SETUP_GUIDE.md](GITHUB_SETUP_GUIDE.md#option-a-personal-access-token-recommended)

### "Please tell me who you are"
Run:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### "fatal: not a git repository"
You're in the wrong folder. Make sure you're in the Neurovision folder:
```bash
cd path/to/Neurovision
git init
```

---

**More help?** Read [GITHUB_SETUP_GUIDE.md](GITHUB_SETUP_GUIDE.md) — it has everything explained in detail with troubleshooting.
