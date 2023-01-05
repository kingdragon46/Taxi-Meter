
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

#### Get/Post Meters
This route allows you to create a new meter by sending a POST request with a JSON body containing a label field. It also allows you to retrieve a list of all meters by sending a GET request.

```http
  /api/meters
```


#### Get meter data by id
This route allows you to retrieve a single meter by sending a GET request and specifying the id of the meter in the URL.

```http
  GET /api/meters/<int:id>/meter_data
```


#### Retrieve/Create meter data by id
This route allows you to create new meter data for a specific meter by sending a POST request with a JSON body containing a value field and specifying the id of the meter in the URL. It also allows you to retrieve all meter data for a specific meter by sending a GET request and specifying the id of the meter in the URL.

```http
  /api/meters/<int:id>/meter_data
```

