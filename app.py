import json
from flask import Flask, request, jsonify, Response, render_template
from models import db, Meter, Meter_Data

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meter_data.sqlite3'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/meters', methods=['POST', 'GET'])
def create_meter():
    try:
        if request.method == 'POST':
            data = request.get_json()
            meter = Meter()
            meter.label=data['label']
            db.session.add(meter)
            db.session.commit()
            return jsonify({'message': 'Meter created successfully!'})
        elif request.method == 'GET':
            meters = Meter.query.all()
            if not meters:
                return jsonify({'meters': "No meters present"})
            output = []
            for meter in meters:
                meter_data = {}
                meter_data['id'] = meter.id
                meter_data['label'] = meter.label
                output.append(meter_data)
            return jsonify({'message': output})
        else:
            return jsonify({'message': 'Method not allowed'})
    except Exception as e:
        print("exception: ", e)

@app.route('/api/render_meters')
def get_meters():
    meters = Meter.query.all()
    if not meters:
        return jsonify({'meters': "No meters present"})
    output = []
    for meter in meters:
        meter_data = {}
        meter_data['id'] = meter.id
        meter_data['label'] = meter.label
        output.append(meter_data)
    return render_template('meters.html', meters = output)

@app.route('/api/meters/<int:id>', methods=['GET'])
def get_meter(id):
    meter = Meter.query.get(id)
    if meter:
        output = {}
        output['id'] = meter.id
        output['label'] = meter.label
        return jsonify({'meter': output})
    return jsonify({'message': 'Meter not found'})

@app.route('/api/meters/<int:id>/meter_data', methods=['POST', 'GET'])
def create_meter_data(id):
    meter = Meter.query.get(id)
    if request.method == 'POST':
        data = request.get_json()
        if meter:
            meter_data = Meter_Data(value=data['value'], meter_id=id)
            db.session.add(meter_data)
            db.session.commit()
            return jsonify({'message': 'Meter Data created successfully!'})
    elif request.method == 'GET':
        if meter:
            meter_data = Meter_Data.query.filter_by(meter_id=id).all()
            output_data = []
            for mdata in meter_data:
                output = {}
                output['id'] = mdata.id
                output['meter_id'] = mdata.meter_id
                output['time_stamp'] = mdata.time_stamp
                output['value'] = mdata.value
                output_data.append(output)
            return jsonify({'meter_data': output_data})
    return jsonify({'message': 'Meter not found'})

@app.route('/api/meters/<int:id>/render_meter_data')
def get_meter_data(id):
    meter = Meter.query.get(id)
    if meter:
        meter_data = Meter_Data.query.filter_by(meter_id=id).all()
        output_data = []
        for mdata in meter_data:
            output = {}
            output['id'] = mdata.id
            output['meter_id'] = mdata.meter_id
            output['time_stamp'] = mdata.time_stamp
            output['value'] = mdata.value
            output_data.append(output)
        return render_template('meter_data.html', meterData = output_data)
        # return jsonify({'meterData': output_data})
    return jsonify({'message': 'Meter data not found'})

if __name__ == '__main__':
    app.run(debug=True)
