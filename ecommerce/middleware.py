import time

from fastapi import Request

from logger import logger

async def ecommerce_middleware(request: Request, callnext):
    logger.info("Starting ................")
    start_time = time.time()
    response = await callnext(request)

    try:
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        logger.info(f"ended. process_time: {process_time}")
    except Exception as e:
        print('=============', str(e))
        logger.error("An error occurred while processing")

    return response
