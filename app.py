from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            peso = float(request.form['peso'])
            medida = request.form['medida']
            if medida == 'K':
                resultado = f'O peso em quilos é: {peso * 0.453592:.2f} kg'
            elif medida == 'P':
                resultado = f'O peso em libras é: {peso * 2.20462:.2f} lbs'
        except ValueError:
            resultado = 'Digite apenas números'
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
    #app.run(debug=True)
