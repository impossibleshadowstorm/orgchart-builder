# Organization Chart Visualization

This project is a web application for visualizing and managing an organization's hierarchy using drag-and-drop functionality. It allows users to update an employee’s manager dynamically and sync changes with a FastAPI backend.

## Features

- **Organization Chart Visualization**: Displays employees in a structured hierarchy.
- **Drag-and-Drop Functionality**: Change an employee’s manager via drag-and-drop.
- **API Integration**: Updates the database when changes are made.
- **UI Feedback**: Loading indicators and success/error messages.

## Technologies Used

- Vite (React.js)
- `@dnd-kit/core`
- `axios`
- `react-router-dom`
- `react-toastify`
- FastAPI (Backend)
- PostgreSQL (Database)
- Docker

## Getting Started

### Running with Docker

1. Clone the repository:

   ```sh
   git clone https://github.com/impossibleshadowstorm/orgchart-builder.git
   cd orgchart-builder
   ```

2. Create `.env` files in the backend and frontend directories using `.env.example` as a reference.

3. Build and start the application:

   ```sh
   docker compose up --build
   ```

4. The application will be available at `http://localhost:5173`.

### Running without Docker

1. Clone the repository and navigate into it:

   ```sh
   git clone https://github.com/impossibleshadowstorm/orgchart-builder.git
   cd orgchart-builder
   ```

2. Create `.env` files in the backend and frontend directories using `.env.example` as a reference.

3. Install dependencies:

   ```sh
   cd backend
   yarn install
   cd ../frontend
   yarn install
   ```

4. Start the backend and frontend:

   ```sh
   cd backend
   python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
   alembic upgrade head
   uvicorn app.main:app --reload
   ```

   In another terminal:

   ```sh
   cd frontend
   yarn run dev
   ```

5. The application will be available at `http://localhost:5173`.
