def power(x, y):
    if y == 0:
        return 1
    elif y > 0:
        return x * power(x, y - 1)
    else:
        return 1 / power(x, -y)


def calculate_power(base, exponent):
    try:
        base = float(base)
        exponent = float(exponent)
        result = power(base, exponent)
        return str(result)
    except ValueError:
        return "Error"
    except ZeroDivisionError:
        return "Error: Division by zero"


# @app.route('/calculate_power', methods=['POST'])
""" def calculate_power_api():
    try:
        data = request.json
        x = float(data['x'])
        y = float(data['y'])
        result = power(x, y)
        return jsonify(success=True, result=result)
    except Exception as e:
        return jsonify(success=False, error=str(e))

if __name__ == '__main__':
    app.run(debug=True) """


def main():
    try:
        x = float(input("Enter the base (x): "))
        y = int(input("Enter the exponent (y): "))

        result = calculate_power(x, y)
        print(f"{x}^{y} = {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: Division by zero encountered for x = 0 with a negative exponent.")


if __name__ == "__main__":
    main()
