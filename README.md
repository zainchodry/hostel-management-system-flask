# 🏨 Hostel Management System - Flask

A simple Hostel Room Booking system built with **Flask**, **SQLite**, and **Flask-Mail**. Admins can manage room availability, set rent, and receive booking requests directly to email.

---

## 🚀 Features

- Admin can:
  - Add rooms with rent, status, and contact details
  - View all rooms and their availability
- Users can:
  - View available hostel rooms
  - Submit booking interest
  - Automatically notify admin via email

---

## 🛠 Technologies Used

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- Flask-Mail
- SQLite3 (for local development)

---

## 🔧 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/hostel-management-system-flask.git
cd hostel-management-system-flask


#2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate


#3. Install dependencies
pip install -r requirements.txt


#5. Run the app
python app.py


