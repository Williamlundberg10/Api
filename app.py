from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/random_math_problem', methods=['GET', 'POST'])
def random_math_problem():
    # Default parameters
    min_value = 1
    max_value = 10
    operations = ['+', '-', '*', '/']

    # Check if the request is a POST request
    if request.method == 'POST':
        data = request.get_json()
        
        # Extract parameters from JSON body
        if 'min_value' in data:
            min_value = data['min_value']
        if 'max_value' in data:
            max_value = data['max_value']
        if 'operations' in data:
            operations = data['operations']

    # Generate two random numbers within the specified range
    num1 = random.randint(min_value, max_value)
    num2 = random.randint(min_value, max_value)

    # Choose a random operator from the specified operations
    operator = random.choice(operations)

    # Create the problem as a string
    if operator == '+':
        problem = f"{num1} + {num2}"
        answer = num1 + num2
    elif operator == '-':
        problem = f"{num1} - {num2}"
        answer = num1 - num2
    elif operator == '*':
        problem = f"{num1} * {num2}"
        answer = num1 * num2
    else:  # operator == '/'
        # Avoid division by 0
        if num2 == 0:
            num2 = 1
        problem = f"{num1} / {num2}"
        answer = num1 / num2

    return jsonify({
        'problem': problem,
        'answer': answer
    })

if __name__ == '__main__':
    app.run(debug=True)
