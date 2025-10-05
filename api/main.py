from fastapi import FastAPI, responses
from typing import Union

app = FastAPI()

@app.get("/")
async def heartbeat():
    return "pumping"

@app.get("/{video}/{res}")
def get_video(video: str, res: str, q: Union[str, None] = None):
    return responses.FileResponse(f"./storage/{video}/{res}/{video}_{res}.mp4")
