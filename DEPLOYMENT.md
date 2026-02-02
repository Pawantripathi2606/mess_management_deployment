# 🚀 Free Deployment Guide - Django Mess Management System

## 🎯 Best Free Hosting Options for Django

Here are the **top 5 FREE platforms** to deploy your Django application, ranked by ease of use:

---

## 🥇 Option 1: PythonAnywhere (RECOMMENDED for Beginners)

**Why:** Easiest for Django, free tier is generous, excellent documentation.

**Free Tier:**
- ✅ 512MB storage
- ✅ 1 web app
- ✅ Custom domain support
- ✅ Always-on (doesn't sleep)
- ⚠️ Limited to PythonAnywhere subdomain on free tier

**Steps to Deploy:**

### 1. Sign Up
- Go to: https://www.pythonanywhere.com/
- Create free "Beginner" account

### 2. Upload Your Code
```bash
# Option A: Using Git (recommended)
git init
git add .
git commit -m "Initial commit"
git push to GitHub

# Then on PythonAnywhere console:
git clone https://github.com/YOUR_USERNAME/mess-management.git
```

### 3. Set Up Virtual Environment
```bash
cd mess-management
mkvirtualenv --python=/usr/bin/python3.10 messenv
pip install -r requirements.txt
```

### 4. Configure Web App
- Go to "Web" tab
- Click "Add a new web app"
- Choose "Manual configuration"
- Python version: 3.10
- Set source code: `/home/YOUR_USERNAME/mess-management`
- Set virtualenv: `/home/YOUR_USERNAME/.virtualenvs/messenv`

### 5. Edit WSGI Configuration
```python
import sys
import os

path = '/home/YOUR_USERNAME/mess-management'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mess_management.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 6. Configure Static Files
- In Web tab → Static files section:
  - URL: `/static/`
  - Directory: `/home/YOUR_USERNAME/mess-management/static/`

### 7. Run Migrations
```bash
cd mess-management
python manage.py migrate
python manage.py init_admin
python manage.py collectstatic
```

**Your site will be at:** `YOUR_USERNAME.pythonanywhere.com`

---

## 🥈 Option 2: Render (Modern & Easy)

**Why:** Modern platform, automatic deployments from Git, PostgreSQL included.

**Free Tier:**
- ✅ 750 hours/month
- ✅ Free PostgreSQL database
- ✅ Auto-deploy from GitHub
- ⚠️ Spins down after 15 min inactivity
- ⚠️ Slow cold starts

**Steps to Deploy:**

### 1. Create Required Files

**`build.sh`** (create in project root):
```bash
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py init_admin
```

**`render.yaml`** (create in project root):
```yaml
services:
  - type: web
    name: mess-management
    env: python
    buildCommand: "./build.sh"
    startCommand: "gunicorn mess_management.wsgi:application"
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
      - key: SECRET_KEY
        generateValue: true
      - key: DEBUG
        value: False
```

### 2. Update `requirements.txt`
Add these lines:
```
gunicorn==21.2.0
psycopg2-binary==2.9.9
whitenoise==6.6.0
```

### 3. Update `settings.py`
```python
# Add to MIDDLEWARE (near top)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    ...
]

# Update ALLOWED_HOSTS
ALLOWED_HOSTS = ['*']  # For initial setup

# Update STATIC settings
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### 4. Deploy
- Push code to GitHub
- Go to https://render.com/
- Click "New +" → "Web Service"
- Connect your GitHub repo
- Render will auto-deploy!

**Your site will be at:** `mess-management.onrender.com`

---

## 🥉 Option 3: Railway (Developer Friendly)

**Why:** Very easy setup, generous free tier, PostgreSQL included.

**Free Tier:**
- ✅ $5 credit/month (500 hours)
- ✅ Free PostgreSQL
- ✅ Auto-deploy from Git
- ⚠️ Credit runs out if overused

**Steps to Deploy:**

### 1. Install Railway CLI (Optional)
```bash
npm install -g @railway/cli
railway login
```

### 2. Create Files

**`Procfile`**:
```
web: gunicorn mess_management.wsgi
```

**`runtime.txt`**:
```
python-3.11.0
```

### 3. Update requirements.txt
```
gunicorn==21.2.0
dj-database-url==2.1.0
psycopg2-binary==2.9.9
```

### 4. Update settings.py
```python
import dj_database_url

# Database
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}
```

### 5. Deploy
- Go to https://railway.app/
- Click "Start a New Project"
- Choose "Deploy from GitHub repo"
- Select your repo
- Railway auto-detects Django!

**Your site will be at:** Generated Railway URL

---

## 🏅 Option 4: Vercel (with Serverless)

**Why:** Great for static + serverless, unlimited free tier.

**Free Tier:**
- ✅ Unlimited deployments
- ✅ 100 GB bandwidth/month
- ⚠️ Requires serverless setup
- ⚠️ More complex for Django

*(Best for experienced developers)*

---

## 🏅 Option 5: Heroku (Classic Choice)

**Why:** Most popular, extensive documentation.

**Free Tier:**
- ⚠️ **No longer has a free tier** (as of Nov 2022)
- Now requires paid Eco plan ($5/month)

---

## 📊 Comparison Table

| Platform | Setup Difficulty | Free Tier | Database | Sleeps? | Best For |
|----------|-----------------|-----------|----------|---------|----------|
| **PythonAnywhere** | ⭐ Easy | Good | SQLite | No | Beginners |
| **Render** | ⭐⭐ Medium | Good | PostgreSQL | Yes | General use |
| **Railway** | ⭐⭐ Medium | Very Good | PostgreSQL | No* | Developers |
| Vercel | ⭐⭐⭐ Hard | Excellent | External | No | Advanced |
| Heroku | ⭐⭐ Medium | ❌ Paid | PostgreSQL | No | Production |

*Railway sleeps based on credit usage

---

## 🎯 My Recommendation for You

**Use PythonAnywhere** because:
1. ✅ Easiest to deploy Django
2. ✅ No sleep/downtime
3. ✅ Works with SQLite (no database migration needed)
4. ✅ Free subdomain
5. ✅ Great for learning

---

## 🚀 Quick Start with PythonAnywhere

**5-Minute Deployment:**

1. **Sign up:** https://www.pythonanywhere.com/registration/register/beginner/
2. **Open Bash console**
3. **Run these commands:**
```bash
git clone https://github.com/YOUR_REPO/mess-management.git
cd mess-management
mkvirtualenv --python=/usr/bin/python3.10 messenv
pip install -r requirements.txt
python manage.py migrate
python manage.py init_admin
python manage.py collectstatic
```

4. **Set up Web App:**
   - Web tab → Add new web app
   - Manual configuration → Python 3.10
   - Configure WSGI file (copy from above)

5. **Reload and visit your site!**

---

## 🔒 Production Settings Checklist

Before deploying, update `settings.py`:

```python
# SECURITY SETTINGS
DEBUG = False  # IMPORTANT!
SECRET_KEY = 'your-production-secret-key'  # Change this!
ALLOWED_HOSTS = ['your-domain.com', 'subdomain.pythonanywhere.com']

# CSRF & SECURITY
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True  # If using HTTPS
```

---

## 📝 Deployment Files Needed

Save these in your project:

### For Render: `build.sh`
```bash
#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

### For Railway/Heroku: `Procfile`
```
web: gunicorn mess_management.wsgi
```

### Update `requirements.txt`
Add for production:
```
gunicorn==21.2.0
whitenoise==6.6.0
```

---

## 🎉 Next Steps After Deployment

1. ✅ Test all features on live site
2. ✅ Create initial admin account
3. ✅ Add some test data
4. ✅ Share the URL with users!

---

## 💡 Pro Tips

1. **Use Git:** Always push to GitHub first, then deploy
2. **Environment Variables:** Use platform's env vars for SECRET_KEY
3. **Database Backups:** Download SQLite file regularly on PythonAnywhere
4. **Monitor Usage:** Check platform dashboard to avoid hitting limits
5. **Custom Domain:** Most platforms allow custom domains (even on free tier)

---

## 🆘 Need Help?

**PythonAnywhere Help:** https://help.pythonanywhere.com/  
**Render Docs:** https://render.com/docs  
**Railway Docs:** https://docs.railway.app/  

---

**My #1 Recommendation: Start with PythonAnywhere!**

It's the easiest and most reliable for Django beginners. You can always migrate to other platforms later.
