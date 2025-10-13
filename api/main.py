from fastapi import FastAPI, File, UploadFile
from typing import Union

app = FastAPI()

@app.get("/")
async def heartbeat():
    return "pumping"


@app.post("/publish")
async def publish_video(file: UploadFile):
    with open(f"../{file.filename}", 'wt', encoding="utf-8") as f:
        contents = await file.read()
        f.write(contents.decode(encoding="utf-8"))
    return {"published": file}


@app.get("/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
