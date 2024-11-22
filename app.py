from flask import Flask, request, jsonify, render_template
from power.power_function import calculate_power  # Import your power logic
from abx.abx import calculate_abx
from logarithmic.logarithmic import calculate_logbx
from stats.mad.mad import mad
from stats.stddev.__init__ import population_standard_deviation
from geo.arccos.arccos import arccos
from geo.arccos.arccos import rad_to_deg
from math import pi

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate_power', methods=['POST'])
def power_api():
    try:
        # Parse the incoming JSON request
        data = request.json
        x = float(data['x'])
        y = float(data['y'])

        # Compute the result
        result = calculate_power(x, y)
        return jsonify(success=True, result=result)
    except Exception as e:
        return jsonify(success=False, error=str(e))


@app.route('/calculate_abx', methods=['POST'])
def abx_api():
    try:
        # Parse the incoming JSON request
        data = request.json
        a = float(data['a'])
        b = float(data['b'])
        x = float(data['x'])

        result = calculate_abx(a,b,x)
        return jsonify(success=True, result=result)
    except Exception as e:
        return jsonify(success=False, error=str(e))


@app.route('/calculate_logbx', methods=['POST'])
def logbx_api():
    try:
        # Parse the incoming JSON request
        data = request.json
        b = float(data['b'])
        x = float(data['x'])

        result = calculate_logbx(b,x)
        return jsonify(success=True, result=result)
    except Exception as e:
        return jsonify(success=False, error=str(e))


@app.route('/calculate_mad', methods=['POST'])
def mad_api():
    try:
        data = request.json.get('data', [])
        if not data:
            return jsonify(success=False, error="No data provided.")
      
        # Calculate MAD
        result = mad(data)
        return jsonify(success=True, result=result)
    except Exception as e:
        return jsonify(success=False, error=str(e))


@app.route('/calculate_std', methods=['POST'])
def standard_deviation_api():
    try:
        # Parse the incoming JSON request
        data = request.json
        numbers = data['numbers']  # List of numbers from user input

        # Validate input: check if numbers are a list of integers/floats
        if not isinstance(numbers, list) or not all(isinstance(i, (int, float)) for i in numbers):
            raise ValueError("Input must be a list of numbers.")

        result = population_standard_deviation(numbers)  # Use the appropriate function for calculation

        return jsonify(success=True, result=result)  # Return result as JSON

    except Exception as e:
        return jsonify(success=False, error=str(e))


@app.route('/calculate_arccos', methods=['POST'])
def arccos_api():
    try:
        # Parse the input
        data = request.json
        x = float(data['x'])  # input for arccos
        unit = data['unit']  # Either "radian" or "degree"

        # Validate the input
        if x<-1 or x>1:
            raise ValueError("Input must be between -1 and 1 for arccos(x)")

        # Calculate the arccos
        result = arccos(x)

        # Convert the degrees if requested
        if unit == 'degree':
            result = rad_to_deg(result)

        return jsonify(success=True, result=result)

    except Exception as e:
        return jsonify(success=False, error=str(e))


if __name__ == '__main__':
    app.run(debug=True)
