# 🚀 Render Deployment Guide - Mess Management System

Complete guide for deploying the Django Mess Management System to Render.

## 📋 Table of Contents
- [Quick Setup](#quick-setup)
- [Build & Start Commands](#build--start-commands)
- [Environment Variables](#environment-variables)
- [Step-by-Step Deployment](#step-by-step-deployment)
- [Post-Deployment Tasks](#post-deployment-tasks)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Quick Setup

### Build Command
```bash
./build.sh
```

### Start Command
```bash
gunicorn mess_management.wsgi:application
```

---

## 🔧 Build & Start Commands

### **Build Command** (Run once during deployment)
```bash
./build.sh
```

**What it does:**
- ✅ Installs all Python dependencies from `requirements.txt`
- ✅ Collects static files (CSS, JS, images) using WhiteNoise
- ✅ Runs database migrations
- ✅ Creates admin superuser automatically
- ✅ Sets up UPI payment details
- ✅ Creates test user for testing

### **Start Command** (Runs your application)
```bash
gunicorn mess_management.wsgi:application
```

**What it does:**
- Starts the Gunicorn WSGI HTTP server
- Serves your Django application
- Handles incoming requests

---

## 🔐 Environment Variables

### **Required Environment Variables**

Set these in your Render dashboard under **Environment** tab:

| Variable | Value | Description |
|----------|-------|-------------|
| `PYTHON_VERSION` | `3.10.0` | Python version to use |
| `SECRET_KEY` | `<generate-random-key>` | Django secret key (see below) |
| `DEBUG` | `False` | **IMPORTANT:** Always False in production |
| `ALLOWED_HOSTS` | `your-app.onrender.com,localhost` | Your Render domain |
| `EMAIL_HOST_USER` | `pawantripathi802@gmail.com` | Gmail address for sending emails |
| `EMAIL_HOST_PASSWORD` | `<your-app-password>` | Gmail app password (16 chars) |

### **Optional Environment Variables**

| Variable | Default Value | Description |
|----------|---------------|-------------|
| `DATABASE_URL` | SQLite (db.sqlite3) | Database connection string |
| `DISABLE_COLLECTSTATIC` | `0` | Set to `1` to skip collectstatic |

---

## 🔑 How to Generate SECRET_KEY

### **Method 1: Python (Recommended)**
```python
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### **Method 2: Online Generator**
Visit: https://djecrety.ir/

> ⚠️ **IMPORTANT:** Never commit the SECRET_KEY to GitHub!

---

## 📧 How to Get Gmail App Password

1. **Enable 2-Step Verification:**
   - Go to: https://myaccount.google.com/security
   - Enable "2-Step Verification" if not already enabled

2. **Generate App Password:**
   - Go to: https://myaccount.google.com/apppasswords
   - Select: **Mail** + **Other** (custom name: "Mess Manager")
   - Copy the **16-character password** (remove spaces!)

3. **Set in Render:**
   - Add as `EMAIL_HOST_PASSWORD` environment variable
   - Example: `abcd efgh ijkl mnop` → `abcdefghijklmnop`

---

## 📝 Step-by-Step Deployment

### **Step 1: Create Web Service on Render**

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository: `Pawantripathi2606/mess_management_deployment`

### **Step 2: Configure Web Service**

| Field | Value |
|-------|-------|
| **Name** | `mess-management-system` (or your preferred name) |
| **Region** | `Singapore` (or closest to your users) |
| **Branch** | `main` |
| **Runtime** | `Python 3` |
| **Build Command** | `./build.sh` |
| **Start Command** | `gunicorn mess_management.wsgi:application` |

### **Step 3: Add Environment Variables**

Click **"Advanced"** and add these environment variables:

```bash
PYTHON_VERSION=3.10.0
SECRET_KEY=your-generated-secret-key-here
DEBUG=False
ALLOWED_HOSTS=mess-management-system.onrender.com,localhost
EMAIL_HOST_USER=pawantripathi802@gmail.com
EMAIL_HOST_PASSWORD=your-16-char-app-password
```

> 📝 **Note:** Replace `mess-management-system.onrender.com` with your actual Render URL

### **Step 4: Choose Plan**

- **Free Plan:** Good for testing (sleeps after 15 mins of inactivity)
- **Starter Plan ($7/mo):** Better for production use

### **Step 5: Deploy**

1. Click **"Create Web Service"**
2. Wait for deployment (2-5 minutes)
3. Monitor build logs for any errors

---

## ✅ Post-Deployment Tasks

### **1. Verify Deployment**

Visit your app URL: `https://your-app.onrender.com`

You should see the role selection page.

### **2. Test Admin Login**

1. Go to: `https://your-app.onrender.com/admin/`
2. Login with:
   - **Username:** `admin`
   - **Password:** `admin123`

> ⚠️ **SECURITY:** Change the admin password immediately!

### **3. Test User Login**

1. Go to: `https://your-app.onrender.com/accounts/login/`
2. Login with test user:
   - **Username:** `testuser`
   - **Password:** `test123`

### **4. Set Up Google OAuth (Optional)**

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create OAuth 2.0 credentials
3. Add authorized redirect URI:
   ```
   https://your-app.onrender.com/accounts/google/login/callback/
   ```
4. Add Client ID and Secret in Django admin:
   - Go to: `/admin/socialaccount/socialapp/`
   - Add Google Social Application

### **5. Change Admin Password**

```python
# SSH into Render shell (if available) or use Django admin
python manage.py changepassword admin
```

Or via Django Admin:
1. Go to `/admin/auth/user/`
2. Click on `admin` user
3. Click "Change password"

---

## 🔍 Database Persistence

### **Current Setup: SQLite**
- Database file: `db.sqlite3`
- **Limitation:** Data resets on each deployment

### **For Production: Use PostgreSQL (Recommended)**

1. **Create PostgreSQL Database on Render:**
   - Go to Dashboard → New → PostgreSQL
   - Copy the `DATABASE_URL`

2. **Update requirements.txt:**
```txt
psycopg2-binary==2.9.9
dj-database-url==2.1.0
```

3. **Update settings.py:**
```python
import dj_database_url

# Database configuration
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

4. **Add DATABASE_URL to Environment Variables:**
```
DATABASE_URL=postgresql://user:pass@host:5432/dbname
```

---

## 🎨 Static Files

Static files are handled by **WhiteNoise** - no additional configuration needed!

- CSS, JS, Images automatically served
- Compressed and cached for performance
- No need for AWS S3 or similar services

---

## 📱 Media Files (User Uploads)

### **Current Setup: Local Storage**
- Upload folder: `media/`
- **Limitation:** Files lost on redeployment

### **For Production: Use Cloud Storage**

**Option 1: Cloudinary (Recommended)**

1. Sign up at [Cloudinary](https://cloudinary.com/)
2. Install package:
```txt
django-cloudinary-storage==0.3.0
```

3. Add to settings.py:
```python
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

**Option 2: AWS S3**

See Django documentation: https://docs.djangoproject.com/en/5.0/howto/static-files/

---

## 🐛 Troubleshooting

### **Issue: Build Fails**

**Check:**
1. Are all dependencies in `requirements.txt`?
2. Is Python version correct? (`PYTHON_VERSION=3.10.0`)
3. Check build logs for specific errors

**Fix:**
```bash
# Test locally first
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

### **Issue: 500 Internal Server Error**

**Check:**
1. `DEBUG=False` is set
2. `ALLOWED_HOSTS` includes your Render domain
3. Check logs in Render dashboard

**Fix:**
- Temporarily set `DEBUG=True` to see detailed error
- Check Render logs: Dashboard → Your Service → Logs

### **Issue: Static Files Not Loading**

**Check:**
1. WhiteNoise is in `MIDDLEWARE`
2. `STATICFILES_STORAGE` is set correctly
3. `collectstatic` ran successfully

**Fix:**
```bash
# In build.sh
python manage.py collectstatic --no-input --clear
```

### **Issue: Email Not Sending**

**Check:**
1. Gmail App Password is correct (16 chars, no spaces)
2. 2-Step Verification is enabled on Gmail
3. Email environment variables are set

**Test locally:**
```python
python manage.py shell
>>> from django.core.mail import send_mail
>>> send_mail('Test', 'Body', 'from@gmail.com', ['to@gmail.com'])
```

### **Issue: Database Reset After Deployment**

**Cause:** SQLite data is ephemeral on Render

**Solution:** Migrate to PostgreSQL (see Database Persistence section)

### **Issue: Build.sh Permission Denied**

**Fix:**
```bash
# Make build.sh executable
git update-index --chmod=+x build.sh
git commit -m "Make build.sh executable"
git push
```

---

## 📊 Monitoring & Logs

### **View Live Logs**
1. Go to Render Dashboard
2. Click on your service
3. Click "Logs" tab
4. Real-time logs will appear

### **Common Log Commands**
```bash
# Filter errors only
grep "ERROR" logs.txt

# Filter specific user
grep "user_id=123" logs.txt
```

---

## 🔒 Security Best Practices

### **1. Production Checklist**

- ✅ `DEBUG=False`
- ✅ Strong `SECRET_KEY` (50+ random characters)
- ✅ `ALLOWED_HOSTS` set correctly
- ✅ HTTPS enabled (automatic on Render)
- ✅ Change default admin password
- ✅ Email passwords in environment variables (not code)

### **2. Environment Variables Security**

- ❌ Never commit `.env` files to Git
- ❌ Never hardcode passwords in code
- ✅ Use Render environment variables
- ✅ Rotate secrets regularly

### **3. Database Backups**

If using PostgreSQL:
- Render provides automatic daily backups
- Manual backup: Dashboard → Database → Backups

---

## 🚀 Performance Optimization

### **1. Enable Caching**

Add to settings.py:
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
    }
}
```

Then create cache table:
```bash
python manage.py createcachetable
```

### **2. Database Connection Pooling**

For PostgreSQL, add to requirements.txt:
```txt
psycopg2-binary==2.9.9
```

### **3. Compress Static Files**

Already configured via WhiteNoise! 🎉

---

## 📞 Support & Resources

- **Django Documentation:** https://docs.djangoproject.com/
- **Render Documentation:** https://render.com/docs
- **Django-allauth Docs:** https://django-allauth.readthedocs.io/

---

## 📝 Summary

### **Essential Commands:**

```bash
# Build Command
./build.sh

# Start Command
gunicorn mess_management.wsgi:application
```

### **Essential Environment Variables:**

```bash
PYTHON_VERSION=3.10.0
SECRET_KEY=<your-secret-key>
DEBUG=False
ALLOWED_HOSTS=<your-app>.onrender.com
EMAIL_HOST_USER=pawantripathi802@gmail.com
EMAIL_HOST_PASSWORD=<your-app-password>
```

### **Default Credentials:**

```
Admin: admin / admin123
Test User: testuser / test123
```

---

**🎉 You're all set! Deploy with confidence!**
