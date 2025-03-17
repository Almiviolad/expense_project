from datetime import datetime, timedelta
from models import storage
from models.expense import Expense

def get_expense_by_date(user_id, filter_type, start_date=None, end_date=None, category=None):
    """Gets expense using date.
    
    Args:
        user_id: The user's ID.
        filter_type: Filter type ('week', 'today', 'custom').
        start_date: The start date (if using 'custom' filter).
        end_date: The end date (if using 'custom' filter).
    
    Returns:
        List of expenses in dictionary format.
    """

    today = datetime.today().date()
    base_query = storage.get_user_expenses(user_id)

    if filter_type == "today":
        start_of_today = datetime.combine(today, datetime.min.time())
        query = base_query.filter(Expense.created_at >= start_of_today)

    elif filter_type == "week":
        week_start = today - timedelta(days=today.weekday())
        start_of_week = datetime.combine(week_start, datetime.min.time())
        query = base_query.filter(Expense.created_at >= start_of_week)

    elif filter_type == "custom":
        try:
            start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
            end_datetime = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=1)  # Include the whole day
            query = base_query.filter(Expense.created_at.between(start_datetime, end_datetime))
        except ValueError:
            raise ValueError("Invalid start or end date format")
    else:
        return []
    if category:
      query = query.filter(Expense.category == category)
    expenses = [expense.to_dict() for expense in query.all()]
    total = sum(expense['amount'] for expense in expenses)
    
    
    return {"expenses": expenses, "total": total}