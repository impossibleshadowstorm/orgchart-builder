# Project Setup

This project consists of a **frontend** (React with Vite) and a **backend** (FastAPI).

## Setup Instructions

1. **Create `.env` files** in both the `frontend` and `backend` directories.

   - Use `.env.example` in each directory as a reference.

2. **Run using Docker**

   ```sh
   docker compose up --build
   ```

   This will start the project and serve the frontend on <http://localhost:5173>.

3. **Run without Docker**
   - Go to the backend folder and follow the instructions in backend/README.md.
   - Go to the frontend folder and follow the instructions in frontend/README.md.

For more details, refer to the README.md files in the respective folders.
