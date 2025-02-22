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

## API Documentation

A Postman collection containing all the API endpoints is available in the root directory of the project:

```txt
File Name: OrgChart-Builder.postman_collection.json
```

How to Use:

- Open Postman.
- Click on Import and select the OrgChart-Builder.postman_collection.json file.
- Once imported, you can explore and test all the API endpoints.

## AI Collaboration & Time Log

### AI Tools Used

During this project, I used multiple AI tools to assist with various tasks:

- ChatGPT: Assisted in structuring the project, generating base code, and debugging issues.
- Grok AI: Used for quick syntax validation and performance optimizations.
- Lovable AI: Helped in planning API structures and best practices.
- DeepSeek AI: Used for advanced debugging suggestions.
- Tabnine AI: Provided code autocompletion within the editor.

### Total Time Spent

```txt
Around 2 hours (Complete frontend & backend setup, API integration, and drag-and-drop functionality).
```

Remaining TODOs

```txt
- Fine-tune UI components for better responsiveness and visual appealing.
- Implement better error handling and logging.
- Implement Authentication for secure endpoints like updating managers.
- Write unit tests for API endpoints.
- Add Fixtures.
```

Priority was given to ensuring the core functionality (drag-and-drop + API integration) worked seamlessly within the given time frame.
