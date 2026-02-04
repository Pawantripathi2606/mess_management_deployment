# Google OAuth Quick Start Guide

## ⚡ Instant Setup (3 Commands)

```bash
# 1. Run the automated setup script
python setup_google_oauth.py

# 2. Start the development server
python manage.py runserver

# 3. Test the login
# Visit: http://127.0.0.1:8000/accounts/login/
```

## 🔑 Your OAuth Credentials

**⚠️ Security Notice:** OAuth credentials should NEVER be hardcoded in your repository.

**Setup your credentials:**

1. **Get your Google OAuth credentials** from [Google Cloud Console](https://console.cloud.google.com/apis/credentials)

2. **Add to `.env` file** (create one if it doesn't exist):
   ```bash
   GOOGLE_CLIENT_ID=your-actual-client-id.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=your-actual-client-secret
   ```

3. **Make sure `.env` is in `.gitignore`** (it should already be there)

**For reference, see `.env.example` for the template.**

## ⚠️ IMPORTANT: Google Cloud Console

**Add this redirect URI to your Google Cloud Console:**

```
http://127.0.0.1:8000/accounts/google/login/callback/
```

**Steps:**
1. Go to: https://console.cloud.google.com/
2. Navigate to: **APIs & Services** → **Credentials**
3. Click your **OAuth 2.0 Client ID**
4. Under **Authorized redirect URIs**, click **+ ADD URI**
5. Paste: `http://127.0.0.1:8000/accounts/google/login/callback/`
6. Click **SAVE**

## 📱 Test Your Setup

1. **Visit login page:**
   ```
   http://127.0.0.1:8000/accounts/login/
   ```

2. **Click "Continue with Google"**

3. **Expected behavior:**
   - Redirects to Google login
   - Choose your Google account
   - Grant permissions
   - Redirects back to your app
   - You're logged in!

## 🎨 What You Got

✅ Modern login page with Google OAuth button  
✅ Modern signup page with Google OAuth button  
✅ Bootstrap 5 styling with premium design  
✅ Fully responsive for mobile/tablet/desktop  
✅ Email/password login as fallback  
✅ Automated admin configuration

## 📁 Files Modified/Created

**Modified:**
- `mess_management/settings.py` - Added allauth configuration
- `mess_management/urls.py` - Added allauth URLs

**Created:**
- `templates/account/login.html` - Modern login page
- `templates/account/signup.html` - Modern signup page
- `setup_google_oauth.py` - Automated setup script

## 🔧 Manual Admin Setup (Alternative)

If you prefer manual setup instead of the script:

1. **Login to admin:** http://127.0.0.1:8000/admin/
2. **Configure Site:**
   - Go to **Sites** → **example.com**
   - Domain: `127.0.0.1:8000`
   - Name: `Mess Management System`
3. **Add Social App:**
   - Go to **Social applications** → **Add**
   - Provider: `Google`
   - Name: `Google OAuth`
   - Client ID: (paste from above)
   - Secret: (paste from above)
   - Sites: Select `127.0.0.1:8000`

## 🐛 Quick Troubleshooting

**Issue:** `redirect_uri_mismatch`  
**Fix:** Add the redirect URI to Google Cloud Console (see above)

**Issue:** `SocialApp matching query does not exist`  
**Fix:** Run `python setup_google_oauth.py`

**Issue:** Login page doesn't show Google button  
**Fix:** Clear browser cache, hard refresh (Ctrl+Shift+R)

## 📚 Full Documentation

See [`walkthrough.md`](file:///C:/Users/Lenovo/.gemini/antigravity/brain/27932d21-42d6-4bc1-9099-dafc28285c75/walkthrough.md) for complete details.
