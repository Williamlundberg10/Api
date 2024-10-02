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

        # Validate and extract parameters from JSON body
        if 'min_value' in data and isinstance(data['min_value'], int):
            min_value = data['min_value']
        if 'max_value' in data and isinstance(data['max_value'], int):
            max_value = data['max_value']
        if 'operations' in data and isinstance(data['operations'], list):
            operations = [op for op in data['operations'] if op in ['+', '-', '*', '/']]

        # Ensure min_value is less than max_value
        if min_value >= max_value:
            return jsonify({'error': 'min_value must be less than max_value'}), 400

    # Generate two random numbers within the specified range
    num1 = random.randint(min_value, max_value)
    num2 = random.randint(min_value, max_value)

    # Choose a random operator from the specified operations
    operator = random.choice(operations)

    # Create the problem as a string and calculate the answer
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
