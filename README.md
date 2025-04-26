# TRON Blockchain API

This project provides an API for interacting with the TRON blockchain.
It allows querying address information and transaction history.

## Endpoints

The API provides the following endpoints:

### 1. `/address` (Implemented)

Retrieves information about a TRON address, including:
- Balance
- Bandwidth
- Energy

**Example request:**  
`POST /address`
```json
{
    "address": "TRon_address_here"
}
```

### 2. `/history` (Implemented)

Retrieves a paginated list of TRON addresses with their information, including:
- Address
- Balance
- Bandwidth
- Energy

**Example request:**  
`GET /history`
```json
{
    "limit": 10,
    "offset": 0
}
```

Where:
- `limit`: Number of records to return (must be greater than 0)
- `offset`: Number of records to skip (must be greater than or equal to 0)

**Example response:**
```json
[
  {
    "address": "TRon_address_1",
    "balance": "100.5",
    "bandwidth": 2000,
    "energy": 1500
  },
  {
    "address": "TRon_address_2",
    "balance": "250.75",
    "bandwidth": 3000,
    "energy": 2000
  }
]
```

## Environment Configuration

The application requires a `.env` file with the following variables:

```
# Database configuration
POSTGRES_USER="your_database_username"
POSTGRES_PASSWORD="your_database_password"
POSTGRES_DB="your_database_name"
DB_HOST="localhost:10145"

# TRON API configuration
TRON_GRID_API_KEY="your_tron_grid_api_key"
```

> **Note:** Replace the placeholder values with your actual configuration. Do not commit the actual values to version control as they contain sensitive information.

## Setup and Installation

### Prerequisites

- Docker and Docker Compose

### Running the Application

1. Clone the repository
2. Create a `.env` file in the `src` directory with the required configuration
3. Run the application using Docker Compose:

```bash
docker-compose up -d
```

The API will be available at `http://localhost:8000`.

## Technologies Used

- FastAPI
- SQLAlchemy
- PostgreSQL
- tronpy (TRON blockchain library)
