# Running TrueAlly backend locally

To run TrueAlly backend locally, please follow the below steps:

Install the dependencies from requirements.txt
### `pip install -r requirements.txt`

and then run

### `flask run`

to start the development server locally.
The server will be accesible at [http://localhost:5000](http://localhost:5000).

### APIs -
#### Get Insurance by policy id - `/api/insurance/policy/<policy_id>` `GET`
#### Get Insurance by customer id - `/api/insurance/customer/<customer_id>` `GET`
#### Update Insurance with policy id - `/api/insurance/policy/<policy_id>` `PUT`
#### Get monthly insurance sales data - `/api/insurance/graph_data` `GET`
