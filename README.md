# 🍽️ Django Mess Management System

A comprehensive web-based mess management application built with Django, designed to streamline hostel/mess operations with features for both administrators and users.

## 🌟 Features

### 👨‍💼 Admin Features
- **User Management** - Create, edit, delete users and manage roles
- **Payment Management** - Track payments with status (pending/partial/paid)
- **💌 Payment Reminders** - Send automated reminders to users with pending payments
- **Grocery Management** - Track grocery purchases by category and month
- **Fixed Expense Management** - Manage monthly fixed expenses (rent, salary, gas, etc.)
- **📨 Message System** - View and reply to user messages
- **🍽️ Meal Calendar** - Plan and manage daily meals (breakfast, lunch, dinner)
- **Monthly Reports** - Generate PDF reports with payment and expense summaries
- **Transparent Data** - View all financial data for accountability

### 👤 User Features
- **Personal Dashboard** - View payment status and recent messages
- **Payment Submission** - Upload payment proofs with transaction details
- **💬 Two-Way Messaging** - Send messages to admin and receive replies
- **🍽️ Meal Calendar** - View daily meal schedules for the month
- **Transparent Data View** - Access to all mess financial information
- **PDF Receipts** - Download personal payment receipts
- **Payment Notifications** - Receive payment reminders from admin

## 🆕 Recently Added Features

### ⭐ Payment Reminder System
- Automated reminder messages for pending/partial payments
- Includes payment details and UPI ID
- Messages saved in user's inbox
- Hidden from admin message section (system messages)

### ⭐ Two-Way Messaging
- Users can send messages to admin
- Admin can reply to user messages
- Users can reply back to admin responses
- Full conversation thread maintained
- Message timestamps and status tracking

### ⭐ Meal Planning Calendar
- Interactive monthly calendar view
- Admin can add/edit/delete daily meal plans
- Users can view read-only meal schedules
- Today's date highlighted
- Breakfast, lunch, dinner, and notes for each day

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd "mess management"
```

2. **Create a virtual environment**
```bash
python -m venv venv
```

3. **Activate the virtual environment**
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create admin user**
```bash
python manage.py init_admin
```
This creates an admin user with:
- Username: `admin`
- Password: `admin123`

7. **Run the development server**
```bash
python manage.py runserver
```

8. **Access the application**
- Open browser and go to `http://127.0.0.1:8000/`
- Login with admin credentials or create a new user

## 📁 Project Structure

```
mess management/
├── core/                           # Main application
│   ├── management/
│   │   └── commands/
│   │       ├── init_admin.py      # Admin initialization script
│   │       └── create_test_user.py # Test user creation
│   ├── templatetags/
│   │   └── custom_filters.py      # Template helper filters
│   ├── migrations/                # Database migrations
│   ├── models.py                  # Database models
│   ├── views.py                   # View functions
│   ├── forms.py                   # Django forms
│   ├── meal_forms.py              # Meal plan forms
│   ├── urls.py                    # URL routing
│   ├── decorators.py              # Custom decorators
│   └── admin.py                   # Admin panel config
├── templates/                     # HTML templates
│   ├── admin/                     # Admin templates
│   │   ├── dashboard.html
│   │   ├── meal_calendar.html    # NEW: Admin meal calendar
│   │   ├── meal_plan_form.html   # NEW: Meal plan form
│   │   ├── messages.html
│   │   └── ...
│   ├── user/                      # User templates
│   │   ├── dashboard.html
│   │   ├── messages_list.html    # NEW: User message list
│   │   ├── message_reply.html    # NEW: User reply form
│   │   ├── meal_calendar.html    # NEW: User meal calendar
│   │   └── ...
│   └── base.html                 # Base template
├── static/                        # Static files (CSS, JS, images)
├── media/                         # User uploaded files
├── mess_management/               # Project settings
├── manage.py                      # Django management script
└── requirements.txt               # Python dependencies
```

## 🗺️ URL Routes

### Admin Routes
```
/manage/dashboard/              - Admin Dashboard
/manage/users/                  - User Management
/manage/payments/               - Payment Management
/manage/payments/<id>/remind/   - Send Payment Reminder (NEW)
/manage/groceries/              - Grocery Management
/manage/expenses/               - Fixed Expense Management
/manage/messages/               - Message Inbox (Enhanced)
/manage/messages/<id>/reply/    - Reply to User Message (NEW)
/manage/meals/                  - Meal Calendar (NEW)
/manage/meals/create/           - Add Meal Plan (NEW)
/manage/meals/<id>/edit/        - Edit Meal Plan (NEW)
/manage/reports/monthly/        - Monthly Reports
```

### User Routes
```
/user/dashboard/                - User Dashboard
/user/payment/                  - Make Payment
/user/messages/                 - View All Messages (NEW)
/user/messages/send/            - Send Message to Admin
/user/messages/<id>/reply/      - Reply to Admin (NEW)
/user/meals/                    - View Meal Calendar (NEW)
/user/receipt/                  - Download Receipt
/user/data/                     - Transparent Data View
```

## 💾 Database Models

### User Profile
- Extended user model with role (admin/user)
- Phone number and room number
- Active status tracking

### Payment
- User payment tracking
- Status: pending, partial, paid
- Transaction ID and proof image
- Month/year based grouping

### Grocery
- Item purchases with categories
- Quantity and price tracking
- Monthly grouping

### Fixed Expense
- Monthly fixed costs (rent, salary, gas, etc.)
- Calculated total expense

### Message (Enhanced)
- User-admin messaging
- Message types: user/system
- Two-way conversation support
- Admin and user replies with timestamps

### Meal Plan (NEW)
- Daily meal planning
- Breakfast, lunch, dinner fields
- Additional notes
- Date-based unique entries

## 🔐 User Roles

### Admin
- Full access to all features
- Can manage users, payments, expenses
- Can reply to messages
- Can create meal plans
- Access to reports and analytics

### User
- View personal payment status
- Submit payment proofs
- Send and receive messages
- View meal calendar
- Access transparent financial data
- Download personal receipts

## 🎨 UI/UX Features

- Clean and modern card-based design
- Responsive layouts
- Color-coded status indicators
- Interactive calendar grid
- Real-time success/error notifications
- Icon-based navigation
- Mobile-friendly interface

## 📊 Reporting

- Monthly payment summary reports
- Expense breakdowns
- Grocery spending analysis
- PDF receipt generation
- Payment status tracking

## 🔧 Management Commands

### Create Admin User
```bash
python manage.py init_admin
```

### Create Test User
```bash
python manage.py create_test_user
```

### Run Migrations
```bash
python manage.py migrate
```

### Collect Static Files
```bash
python manage.py collectstatic
```

## 🛠️ Technology Stack

- **Backend:** Django 5.0
- **Database:** SQLite (easily switchable to PostgreSQL/MySQL)
- **PDF Generation:** ReportLab
- **Frontend:** HTML5, CSS3, JavaScript
- **Authentication:** Django Auth System
- **File Uploads:** Django File Handling

## 📝 Default Credentials

**Admin Account:**
- Username: `admin`
- Password: `admin123`

**Test User Account:**
- Username: `testuser`
- Password: `test123`

> ⚠️ **Important:** Change these default passwords in production!

## 🔄 Recent Updates

### Version 2.0 (Latest)
- ✅ Added payment reminder system
- ✅ Implemented two-way messaging
- ✅ Created meal planning calendar
- ✅ Fixed all template syntax errors
- ✅ Enhanced message system with reply functionality
- ✅ Added system/user message type differentiation
- ✅ Created custom template filters
- ✅ Improved user message inbox

### Version 1.0
- Initial release with core features
- User and payment management
- Grocery and expense tracking
- Basic messaging system
- PDF reports generation

## 🐛 Bug Fixes

- Fixed template syntax errors in all templates
- Resolved AdminReplyForm import issues
- Fixed month comparison operators
- Corrected malformed template tags
- Fixed grocery and expense form templates

## 📖 Documentation

- See `walkthrough.md` for detailed feature documentation
- Check `implementation_plan.md` for technical details
- Review code comments for inline documentation

## 🤝 Contributing

This is a private project. For any suggestions or issues, please contact the administrator.

## 📄 License

This project is private and not licensed for public use.

## 👨‍💻 Author

Developed for mess management operations.

## 🙏 Acknowledgments

- Django Framework
- ReportLab for PDF generation
- Bootstrap-inspired design patterns

---

**Status:** ✅ Production Ready
**Last Updated:** February 2026
**Version:** 2.0
