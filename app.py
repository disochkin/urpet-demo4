import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers.TaskController import TaskController

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
repo = []
app.include_router(TaskController.create_router())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
