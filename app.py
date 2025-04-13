from flask import Flask, jsonify, request
    
app = Flask(__name__)
@app.route('/')
def home():
    return 'Hi!'

@app.route('/api/v1.0/predict')
def predict():
    num_one = request.args.get('num_one')
    num_two = request.args.get('num_two')
    if num_one and num_two:
        if float(num_one) + float(num_two) > 5.8:
            prediction = 1
        else:
            prediction = 0
    else:
        prediction = 0
    return jsonify({'prediction' : prediction, 'features' : [num_one, num_two]})

if __name__ == '__main__':
    app.run(debug=True, port=5002)
