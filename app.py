from fastapi import FastAPI, Request
from Bio import SeqIO
from io import StringIO
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/convert")
async def convert(request: Request):
    raw_data = await request.body()
    handle = StringIO(raw_data.decode("utf-8"))
    output = StringIO()

    for record in SeqIO.parse(handle, "fasta"):
        record.id = record.id.split()[0]
        record.description = ""
        SeqIO.write(record, output, "fasta")

    return PlainTextResponse(output.getvalue())
