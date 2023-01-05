
# Taxi Meter

This is a Flask application that serves as an API for storing and retrieving data for meters and meter data. The application uses SQLAlchemy to connect to a SQLite database and store data in it.

## Run Locally

Clone the project

```bash
  git clone https://github.com/kingdragon46/Taxi-Meter.git
```

Go to the project directory

```bash
  cd Ride-Meter
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py
```


## API Reference

#### Get Meters

```http
  GET /api/meters
```

#### Create Meters

```http
  POST /api/meters
```

#### Get meter data by id

```http
  GET /api/meters/<int:id>/meter_data
```


#### Create meter data by id

```http
  POST /api/meters/<int:id>/meter_data
```

