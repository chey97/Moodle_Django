#!/bin/bash

# Function to stop the backend server
stop_backend() {
    echo "Stopping backend server..."
    kill $BACKEND_PID
}

# Trap the EXIT signal to call the cleanup function
trap stop_backend EXIT

# Start backend server
source .venv/bin/activate
cd server
python manage.py runserver 8000 &
# Capture the PID of the backend server
BACKEND_PID=$!

# Start frontend development server
cd ../frontend
npm run dev

