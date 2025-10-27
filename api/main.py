from fastapi import FastAPI, UploadFile, Response

app = FastAPI()

@app.get("/heartbeat")
async def heartbeat():
    return "pumping"

@app.post("/publish")
async def publish_video(file: UploadFile):
    with open(f"../{file.filename}", 'wt', encoding="utf-8") as f:
        contents = await file.read()
        f.write(contents.decode(encoding="utf-8"))
    return {"published": file}

@app.get("/video/{file:path}")
def hls_files(file: str):
    contents = bytes()
    try:
        with open(f"./storage/{str(file)}", "rb") as f:
            contents = f.read()
    except FileNotFoundError:
        return Response({"msg": "file not found"}, media_type="application/json", status_code=404, headers={"Access-Control-Allow-Origin": "*"})

    return Response(
        contents, media_type="application/x-mpegURL",
        headers={"Access-Control-Allow-Origin": "*"}
    )

@app.get("/{file:path}")
def static_files(file: str):
    contents = bytes()
    try:
        with open(f"./app/{str(file)}", "rt") as f:
            contents = f.read()
    except Exception:
        return Response({"msg": "file not found"}, media_type="application/json", status_code=404, headers={"Access-Control-Allow-Origin": "*"})

    return Response(
        contents, headers={"Access-Control-Allow-Origin": "*"}
    )

