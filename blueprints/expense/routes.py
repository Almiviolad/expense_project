from blueprints import expense
from blueprints.expense import expense_bp
from flask import request, jsonify
import models
from models import storage
from models.expense import Expense
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from blueprints.expense.utils import get_expense_by_date

@expense_bp.route('', methods={'POST'})
@jwt_required()
def add_expense(user_id):
    #adds new expense
    # gets the user id of the logged in user
    user_id = get_jwt_identity()

    # gets the expesne data from the request
    data = request.get_json()
    if not data or not 'amount' in data or not  'category' in data:
        return jsonify({'error': 'Mising required expenses fields'}), 400
    
    amount = data['amount']
    category = data['category']
    description = data['description']
    
    try:
        newExpense = Expense(user_id=user_id, amount=amount, category=category, description=description)
        storage.add(newExpense)
        storage.save()
    except Exception as err:
        return jsonify({'error': str(err)}), 400
    return jsonify({'message': 'Expense added succssfully'}), 201

# get expense by date to date, show expens diagram, delete expense, update, 
@expense_bp.route('', methods={'GET'})
@jwt_required()
def get_expenses():
    user_id = get_jwt_identity()
    data = request.get_json()
    if not data or not 'filter_type' in data:
        return jsonify({'error': 'Mising required expenses filter fields'}), 400
    
    filter = data['filter_type']
    if filter is 'custom':
        if not 'start_date' in data or not 'end_date' in data:
            return jsonify({'error': 'Mising required expenses filter fields (start or end date)'}), 400
        else:
            start_date = data['start_date']
            end_date = data['end_date']
            try:
                resonse = get_expense_by_date(user_id, filter, start_date, end_date)
                return jsonify(response), 200
            except Exception as err:
                return jsonify({'error': str(err)}), 400
            
    try:
        response = get_expense_by_date(user_id, filter)
        return jsonify(response), 200
    except Exception as err:
                return jsonify({'error': str(err)}), 400
    
@expense_bp.route("/<int:expense_id>", methods=["DELETE"])
@jwt_required()
def delete_expense(expense_id):
    """Delete an expense"""
    user_id = get_jwt_identity()
    expense = storage.get_expense(expense_id)
    if not expense:
        return jsonify({"error": "Expense not found"}), 404
    storage.delete(expense)
    storage.save()
    return jsonify({"message": f"Expense {expense.id} deleted  successfully"}), 200

@expense_bp.route("/<int:expense_id>", methods=["PUT"])
@jwt_required()
def update_expense(expense_id):
    """Update an expense"""
    user_id = get_jwt_identity()
    expense = storage.get_expense(expense_id)
    if not expense:
        return jsonify({"error": "Expense not found"}), 404

    data = request.get_json()
    if "amount" in data:
        expense.amount = data["amount"]
    if "category" in data:
        expense.category = data["category"]
    if "description" in data:
        expense.description = data["description"]

    storage.save()
    return jsonify({"message": "Expense updated successfully"}), 200
