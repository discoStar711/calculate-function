from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

def rownanie_kwadrat():
    a = random.randint(-10,10)
    b = random.randint(-10,10)
    c = random.randint(-10,10)
    odp = r"<p>"
    wzor = r"<p> Przykład: $" + str(a) + r"x(^2)"
    while a==0:
        a = random.randint(0,10)
    if a == 1:
        wzor = r"<p> Przykład: $ x(^2)"
    else:
        r"<p> Przykład: $" + str(a) + r"x(^2)"
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
        wzor += str(c) + r" = 0 $ </p>"
    elif c>0:
         wzor += r"+" + str(c) + r" = 0 $ </p>"
    else:
        wzor += r" = 0 $ </p>"
    delta = b^2 - 4*a*c
    if delta < 0:
        odp += r"Brak miejsc zerowych funkcji </p>"
    elif delta == 0:
        x0= (-b)/(2*a)
        odp += r"$ x_1 =" + str(x0) + r"$ </p>"
    else: 
        x1 = r"$ \frac{" + str(-b) + r"\sqrt(delta)" + "}{" + str(2*a) + "} $ </p>"
        x2 = r"$ \frac{" + str(-b) + r"-\sqrt(delta)" + "}{" + str(2*a) + "} $ </p>"
        odp += x1 + x2
    return wzor, odp

@app.route('/test')
def test():
    (dzialanie1, odp1) = rownanie_kwadrat
    return render_template("test.html", dzialanie1=dzialanie1, odp1=odp1)

if __name__ == '__main__':
    app.run()
