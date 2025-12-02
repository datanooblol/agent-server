from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from package.routers.agents import router as agents_router
from package.routers.llms import router as llms_router
from package.agents import examples  # Import to register agents
from package.llms import models  # Import to register models

app = FastAPI(title="Agent Service")

app.include_router(agents_router)
app.include_router(llms_router)

# Enable CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "message": "Agent API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)