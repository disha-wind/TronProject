# TRON Blockchain API

This project provides an API for interacting with the TRON blockchain. It allows querying address information and transaction history (under development).

## Endpoints

The API provides the following endpoints:

### 1. `/address` (Implemented)

Retrieves information about a TRON address, including:
- Balance
- Bandwidth
- Energy

**Example request:**
```json
POST /address
{
    "address": "TRon_address_here"
}
```

### 2. `/history` (Under Development)

This endpoint will allow querying transaction history for a TRON address.

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