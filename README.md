# 💸 Expense Tracker with ML Prediction

## 📌 Overview

This project is a full-stack web application that helps users **track, analyze, and predict their expenses**.
It combines **Django backend, data visualization, and Machine Learning** to provide meaningful financial insights.

---

## 🚀 Features

* 🔐 User Authentication (Login/Signup)
* ➕ Add, Edit, Delete Expenses (CRUD)
* 👤 User-specific data (each user sees only their expenses)
* 📊 Dashboard with summary (Total, Entries, Categories)
* 📈 Charts:

  * Monthly Expense Trend (Bar Chart)
  * Category-wise Distribution (Pie Chart)
* 🤖 ML Prediction:

  * Predicts **next month’s expense**
  * Uses **historical + real-time data**

---

## 🧠 Machine Learning

* Model Used: **Random Forest Regressor**
* Input Features:

  * Month-wise expense data
* Data Source:

  * Historical data (CSV)
  * Current user expenses (Database)

### 📊 Prediction Logic

The model:

1. Reads past expense data
2. Combines with current month data
3. Learns spending pattern
4. Predicts next month’s expense

---

## 🏗️ Tech Stack

* **Frontend:** HTML, CSS, Chart.js
* **Backend:** Django (Python)
* **Database:** SQLite / MySQL
* **ML:** Scikit-learn (Random Forest)
* **Data Handling:** Pandas

---

## 📂 Project Structure

```
expense_tracker/
│
├── tracker/
│   ├── models.py
│   ├── views.py
│   ├── ml_model.py
│   ├── ml_data.csv
│   └── templates/
│
├── expense_tracker/
│   ├── settings.py
│   └── urls.py
│
└── manage.py
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/CodewithGayithri/expense_tracker_ML.git
cd expense_tracker_ML
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the server

```
python manage.py runserver
```

### 5. Open in browser

```
http://127.0.0.1:8000/
```

---

## 📸 Screenshots

* Dashboard
* Charts Page
* Profile Page

*(Add screenshots here for better presentation)*

---

## 🚧 Challenges Faced

* Handling user authentication and session management
* Fixing chart data rendering issues
* Integrating ML with real-time data
* Managing date-based filtering for predictions
* UI alignment and responsive design

---

## 🔮 Future Enhancements

* 📱 Mobile-friendly UI
* 🔔 Expense alerts & notifications
* 📅 Yearly & weekly predictions
* 🤖 Advanced ML models (LSTM, ARIMA)
* 💡 Smart spending suggestions

---

## 👩‍💻 Author

**Gayithri N**
Final Year ISE Student

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
