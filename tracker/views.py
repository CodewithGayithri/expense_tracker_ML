from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from collections import defaultdict

from .ml_model import predict_monthly_expense


# ---------------- HOME ----------------
def home(request):
    return render(request, 'home.html')


# ---------------- PROFILE ----------------
@login_required
def profile(request):
    return render(request, 'profile.html')


# ---------------- DASHBOARD ----------------
@login_required
def dashboard(request):
    today = date.today()

    # Current month expenses (for table + cards)
    expenses = Expense.objects.filter(
        user=request.user,
        date__month=today.month,
        date__year=today.year
    )

    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    count = expenses.count()

    # ---------------- ML PREDICTION ----------------
    all_expenses = Expense.objects.filter(user=request.user)
    monthly_prediction = predict_monthly_expense(all_expenses)

    # ---------------- CHART DATA ----------------

    # Monthly chart (bar)
    monthly_data = defaultdict(float)
    for exp in all_expenses:
        month = exp.date.strftime("%b")
        monthly_data[month] += exp.amount

    months = list(monthly_data.keys())
    monthly_totals = list(monthly_data.values())

    # Category chart (pie)
    category_data = defaultdict(float)
    for exp in all_expenses:
        category_data[exp.category] += exp.amount

    category_labels = list(category_data.keys())
    category_values = list(category_data.values())

    # ---------------- ADD EXPENSE ----------------
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()

    return render(request, 'dashboard.html', {
        'expenses': expenses,
        'form': form,

        # cards
        'total': total,
        'count': count,
        'categories_count': len(category_labels),

        # ML
        'monthly_prediction': monthly_prediction,

        # charts
        'months': months,
        'monthly_totals': monthly_totals,
        'category_labels': category_labels,
        'category_values': category_values,
    })


# ---------------- EDIT ----------------
@login_required
def edit_expense(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'edit_expense.html', {'form': form})


# ---------------- DELETE ----------------
@login_required
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)
    expense.delete()
    return redirect('dashboard')


# ---------------- SIGNUP ----------------
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

from collections import defaultdict
import pandas as pd
@login_required
def charts(request):

    # --------- LOAD CSV (PAST DATA) ----------
    try:
        df_csv = pd.read_csv('tracker/ml_data.csv')
    except:
        df_csv = pd.DataFrame(columns=['month', 'total_expense'])

    # Convert CSV to dict
    monthly_data = {}

    for _, row in df_csv.iterrows():
        monthly_data[int(row['month'])] = float(row['total_expense'])

    # --------- CURRENT USER DATA ----------
    expenses = Expense.objects.filter(user=request.user)

    today = date.today()

    current_total = expenses.filter(
        date__month=today.month,
        date__year=today.year
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    # Add current month
    monthly_data[today.month] = current_total

    # --------- SORT DATA ----------
    sorted_months = sorted(monthly_data.keys())

    month_names = {
        1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
        5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
        9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
    }

    months = [month_names[m] for m in sorted_months]
    monthly_totals = [monthly_data[m] for m in sorted_months]
    
     # --------- CATEGORY PIE ----------
    category_data = expenses.values('category').annotate(total=Sum('amount'))

    category_labels = [item['category'] for item in category_data]
    category_values = [item['total'] for item in category_data]

    return render(request, 'charts.html', {
        'months': months,
        'monthly_totals': monthly_totals,
        'category_labels': category_labels,
        'category_values': category_values
    })