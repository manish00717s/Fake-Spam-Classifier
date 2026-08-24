# GitHub Upload Instructions

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Fill in these details:
   - **Repository name**: `spam-classifier`
   - **Description**: "SMS Spam Classification using Machine Learning and NLP - 6 week project"
   - **Visibility**: Public
   - **DO NOT initialize** with README, .gitignore, or license (we already have these)
3. Click "Create repository"

## Step 2: Get Your Repository URL

After creating, you'll see something like:
```
https://github.com/YOUR_USERNAME/spam-classifier.git
```

## Step 3: Connect Local Repository to GitHub

Run this command (replace YOUR_USERNAME):

```bash
git remote add origin https://github.com/YOUR_USERNAME/spam-classifier.git
git branch -M main
git push -u origin main
```

## Step 4: Done!

Your repository is now live at:
```
https://github.com/YOUR_USERNAME/spam-classifier
```

---

## If You Get Authentication Error

If prompted for authentication:

### Option A: Personal Access Token (Recommended)
1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Select scopes: `repo` (all)
4. Copy the token
5. When prompted for password during git push, paste the token

### Option B: GitHub CLI
```bash
gh auth login
# Follow prompts
```

### Option C: SSH Key
Setup SSH keys from GitHub settings and use:
```bash
git remote set-url origin git@github.com:YOUR_USERNAME/spam-classifier.git
```

---

## Verify Upload

After push is complete:
1. Visit: https://github.com/YOUR_USERNAME/spam-classifier
2. You should see all files listed
3. Scroll down to see README.md content

---

## After Upload

Share your GitHub URL:
- On LinkedIn: "Check out my spam classifier ML project: [URL]"
- In resume/portfolio: Add link to GitHub
- On Twitter: Share the project

**Repository is now ready for the world to see! 🚀**
