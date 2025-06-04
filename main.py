import os

import requests
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from exceptions import *
from utils import get_latlng_by_digipin

app = FastAPI()


@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        media_type="application/json",
        content={"success": False, "response": exc.message},
    )


@app.get("/reverse/")
def missing_digipin():
    raise InvalidDigiPinException


@app.get("/reverse/{digipin}")
def root(digipin: str) -> JSONResponse:

    if digipin is None:
        raise InvalidDigiPinException

    langitude, latitude = get_latlng_by_digipin(digipin)

    session = requests.Session()

    url = f"{os.environ.get('NOMINATIM_BASE_URL')}/reverse"

    headers = {"User-Agent": os.environ.get("USER_AGENT")}

    params = {"lat": latitude, "lon": langitude, "zoom": 18, "format": "jsonv2"}

    try:
        data = session.get(url, params=params, headers=headers, timeout=2)
        data.raise_for_status()
        response = data.json()
    except requests.exceptions.RequestException as err:
        raise NominatimException()
    except Exception as e:
        raise AppException(f"Unexpected error: {str(e)}")

    response["digipin"] = digipin

    return JSONResponse(
        status_code=200,
        media_type="application/json",
        content={
            "success": True,
            "response": response,
        },
    )
