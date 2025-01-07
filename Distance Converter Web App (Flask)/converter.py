from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def converter():
    '''Web app that converts kilometers to miles and vice-versa.'''

    if request.method == 'POST':
        direction = request.form['direction']
        distance = float(request.form['distance'])

        if direction == 'Kilometers to miles':
            units = 'kilometers'
            o_units = 'miles'
            conversion = 0.621371192
        elif direction == 'Miles to kilometers':
            units = 'miles'
            o_units = 'kilometers'
            conversion = 1.609344

        result = distance * conversion

    return render_template('converter.html', result=result, distance=distance, units=units, o_units=o_units)


if __name__ == '__main__':
    app.run(debug=True)
