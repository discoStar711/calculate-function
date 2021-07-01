from flask import Flask, render_template, request
import random
from calculate_function import calculate

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/o-nas', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/api/calculate', methods=['POST'])
def calculate_function():
    function_formula = request.args.get('function')
    return calculate(function_formula)

def rownanie_kwadrat():
    a = random.randint(-10,10)
    b = random.randint(-10,10)
    c = random.randint(-10,10)
    odp = r""
    wzor = r"Przykład: " + str(a) + r"x^2"
    while a==0:
        a = random.randint(0,10)
    if a == 1:
        wzor = r"Przykład: x^2"
    else:
        r"Przykład: $" + str(a) + r"x^2"
    if b<0:
        wzor += str(b) + r"x"
    elif b>0:
        if b == 1:
            wzor += r"+" + r"x"
        else:
            wzor += r"+" + str(b) + r"x"
    else:
        wzor = wzor
    if c<0:
        wzor += str(c) + r" = 0"
    elif c>0:
         wzor += r"+" + str(c) + r" = 0"
    else:
        wzor += r" = 0"
    delta = b^2 - 4*a*c
    if delta < 0:
        odp += r"Brak miejsc zerowych funkcji"
    elif delta == 0:
        x0= (-b)/(2*a)
        odp += r"x_1 =" + str(x0)
    else:
        x1 = r"\frac{" + str(-b) + r"\sqrt(" + str(delta) + r")" + "}{" + str(2*a) + "}"
        x2 = r"\frac{" + str(-b) + r"-\sqrt(" + str(delta) + r")" + "}{" + str(2*a) + "}"
        odp += x1 + x2
    return wzor, odp

@app.route('/test')
def test():
    (dzialanie1, odp1) = rownanie_kwadrat()
    (dzialanie2, odp2) = rownanie_kwadrat()
    (dzialanie3, odp3) = rownanie_kwadrat()
    (dzialanie4, odp4) = rownanie_kwadrat()
    (dzialanie5, odp5) = rownanie_kwadrat()
    return render_template("test.html", dzialanie1=dzialanie1, odp1=odp1, dzialanie2=dzialanie2, odp2=odp2, dzialanie3=dzialanie3, odp3=odp3, dzialanie4=dzialanie4, odp4=odp4, dzialanie5=dzialanie5, odp5=odp5)

if __name__ == '__main__':
    app.run()
