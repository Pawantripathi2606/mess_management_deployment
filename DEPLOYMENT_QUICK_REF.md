# 🚀 QUICK DEPLOYMENT REFERENCE

## Render Configuration

### Build Command
```bash
./build.sh
```

### Start Command
```bash
gunicorn mess_management.wsgi:application
```

---

## Environment Variables (Copy & Paste)

```plaintext
PYTHON_VERSION=3.10.0
SECRET_KEY=<GENERATE_NEW_SECRET_KEY>
DEBUG=False
ALLOWED_HOSTS=<your-app-name>.onrender.com,localhost
EMAIL_HOST_USER=pawantripathi802@gmail.com
EMAIL_HOST_PASSWORD=<YOUR_GMAIL_APP_PASSWORD>
```

---

## Generate SECRET_KEY

**Run this command:**
```python
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Or visit: https://djecrety.ir/

---

## Get Gmail App Password

1. Go to: https://myaccount.google.com/apppasswords
2. Create app password for "Mail"
3. Copy 16-character password (remove spaces)
4. Add to `EMAIL_HOST_PASSWORD`

---

## Default Login Credentials

### Admin
- URL: `/admin/`
- Username: `admin`
- Password: `admin123`

### Test User
- URL: `/accounts/login/`
- Username: `testuser`
- Password: `test123`

---

## Post-Deployment

1. ✅ Visit your app URL
2. ✅ Test admin login
3. ✅ **CHANGE ADMIN PASSWORD**
4. ✅ Test user registration
5. ✅ Test password reset email

---

## Common Issues & Fixes

### Build Fails
```bash
# Check Python version
PYTHON_VERSION=3.10.0

# Make build.sh executable
git update-index --chmod=+x build.sh
```

### Static Files Not Loading
- Check WhiteNoise is in MIDDLEWARE
- Verify collectstatic ran successfully

### Email Not Working
- Verify Gmail App Password (16 chars)
- Enable 2-Step Verification first
- Check environment variable name

### Database Resets
- Migrate to PostgreSQL for persistence
- See RENDER_DEPLOYMENT.md for instructions

---

## Need Help?
See full guide: `RENDER_DEPLOYMENT.md`
