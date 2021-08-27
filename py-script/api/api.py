
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.responseMessage import responseMessage
from service.service import service

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def test():
    return responseMessage().s_code(200).customMes("SW_APPLICATION_SERVICE_HOME")

@app.get("/psm/sniffer")
def psmSniffer():
    data=service().psmSniffer()
    # print(data)
    return responseMessage().s_code(200).s_data(data)

@app.get("/test")
def test():
    return "ok"
    