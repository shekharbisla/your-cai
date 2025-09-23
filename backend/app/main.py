# backend/app/main.py
"""
Your-CAi Backend Entrypoint
---------------------------
This is the main FastAPI application that powers the CAi system.
Phase 1: Only health & root endpoints (MVP).
Later: Routers for invoice, chat, audit, advisory etc.
"""

from fastapi import FastAPI

# Create FastAPI app with metadata
app = FastAPI(
    title="Your CAi Backend",
    description="AI-powered Chartered Accountant (MVP)",
    version="0.1.0",
    contact={
        "name": "Your CAi Team",
        "email": "support@yourcai.ai",
    },
)

# Root endpoint (basic check)
@app.get("/")
def read_root():
    return {"message": "Welcome to Your CAi backend! 🚀", "phase": "MVP Phase 1"}

# Later we'll include routers here, e.g.:
# from .routes import router
# app.include_router(router, prefix="/api")
