from datetime import datetime, timedelta
from models import storage
from models.expense import Expense

def get_expense_by_date(user_id, filter, start_date=None, end_date=None ):
    """gets expense using using date
    args:
    filter(week, today, custom)
    start_date: The start date of query if using custom
    end_date: The end date of query if using custom
    """
    
    base_query = storage.get_user_expenses(user_id)
    if filter == "today":
        start_of_today = datetime.combine(today, datetime.min.time())
        query = base_query.filter(Expense.created_at >= start_of_today)
    
    elif filter == "week":
        week_start = today - timedelta(days=today.weekday())
        start_of_week = datetime.combine(week_start, datetime.min.time())
        query = base_query.filter(Expense.created_at >= start_of_week)
    elif filter == "custom":
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            query = base_query.filter(Expense.created_at.between(start_date, end_date))
        except ValueError:
            raise ValueError("Invalid start or end date format")
      else:
        return []
      return [expense.to_dict() for expense in query.all()]


def get_expense_by_category(user_id, category, filter, start_date=None, end_date=None ):
    """gets expense using using category
    args:
    category: category of the expenses 
    filter(week, today, custom)
    start_date: The start date of query if using custom
    end_date: The end date of query if using custom
    """
    date_filtered_expenses = get_expense_by_date(user_id, filter, start_date, end_date)
    category_filtered_expenses = [for expense in date_filtered_expenses if expense['category'] == category]

def total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total

"""
up next
* total functions for date and category ✓
^ pagination
* testing
* email
* hints
* frontened
"""