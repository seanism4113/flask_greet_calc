# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def display_add_result():
    """ Add a and b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.add(a,b)
    return f"""
    <h1>The addition of {a} + {b} = {result}</h1>
    """

@app.route('/sub')
def display_subtract_result():
    """ Subtract a and b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.sub(a,b)
    return f"""
    <h1>The subtraction of {a} - {b} = {result}</h1>
    """

@app.route('/mult')
def display_multiply_result():
    """ Multiply a and b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.mult(a,b)
    return f"""
    <h1>The multiplication of {a} x {b} = {result}</h1>
    """

@app.route('/div')
def display_division_result():
    """ Divide a and b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.div(a,b)
    return f"""
    <h1>The division of {a} / {b} = {result}</h1>
    """

operators = {
        "add": operations.add,
        "sub": operations.sub,
        "mult": operations.mult,
        "div": operations.div,
        }

@app.route("/math/<operation>")
def do_math(operation):
    """Perform math function on a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operation](a, b)

    return f"""
    <h1>If you {operation} {a} and {b} you get {result}</h1>
    """