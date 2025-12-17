# ERP System Clone

A simplified ERP system architecture designed to be a SAP/Oracle clone, utilizing Google Cloud services and Firebase.

## Technology Stack

- **Backend**: Python (Flask)
- **Database**:
  - Google Cloud BigTable (for high throughput, scalable data)
  - Google Cloud Spanner (for relational, transactional data)
  - Google Cloud MemoryStore (Redis for caching)
- **Frontend**: Modern JavaScript (Vanilla/ES6+)
- **Hosting/Platform**: Firebase & Google Cloud Platform

## Project Structure

```
/
├── backend/
│   ├── app/
│   │   ├── api/            # API endpoints
│   │   ├── db/             # Database clients (BigTable, Spanner, MemoryStore)
│   │   ├── main.py         # Application entry point
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── public/             # Static files
│   ├── src/                # Source code
│   │   ├── api.js          # API interaction layer
│   │   ├── firebase_config.js # Firebase configuration
│   │   ├── index.js        # Frontend entry point
│   └── package.json        # Node dependencies
├── firebase.json           # Firebase configuration
└── README.md
```

## Setup

### Backend

1. Navigate to `backend/`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set environment variables for Google Cloud project.
4. Run the application: `python -m app.main`.

### Frontend

1. Navigate to `frontend/`.
2. Install dependencies: `npm install`.
3. Update `src/firebase_config.js` with your Firebase project details.

## Future Plans

The core ERP logic ("boring stuff") will be implemented later, powered by Gemini Flash.
