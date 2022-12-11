from fastapi import FastAPI

from routes import routes
from core.db import database


app = FastAPI()

app.include_router(routes)


@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    await database.disconnect()


# Вызывается при каждом запросе
# Передаем в request экземпляр сессии, по окончанию запроса его закрываем
# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response(
#         "Internal server error",
#         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#     )

#     try:
#         request.state.db = await SessionLocal()
#         response: StreamingResponse = await call_next(request)

#     finally:
#         request.state.db.close()

#     return response
