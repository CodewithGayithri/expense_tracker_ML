import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from django.db.models import Sum
from datetime import date


def predict_monthly_expense(expenses):
    """
    Hybrid ML:
    Uses CSV (past data) + DB (current user data)
    """

    # ---------------- LOAD CSV ----------------
    try:
        df = pd.read_csv('tracker/ml_data.csv')
    except:
        df = pd.DataFrame(columns=['month', 'total_expense'])

    # ---------------- CURRENT DATA ----------------
    expenses = list(expenses)

    if len(expenses) == 0:
        return None

    today = date.today()
    current_month = today.month

    current_total = sum([float(e.amount) for e in expenses])

    # ---------------- ADD CURRENT MONTH ----------------
    df.loc[len(df)] = [current_month, current_total]

    # ---------------- NEED MIN DATA ----------------
    if len(df) < 3:
        return None

    # ---------------- TRAIN MODEL ----------------
    X = df[['month']]
    y = df['total_expense']

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    # ---------------- PREDICT NEXT MONTH ----------------
    next_month = current_month + 1 if current_month < 12 else 1

    prediction = model.predict([[next_month]])

    return round(prediction[0], 2)