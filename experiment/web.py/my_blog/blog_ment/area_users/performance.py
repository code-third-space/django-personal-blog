import time
import logging

logger = logging.getLogger(__name__)

def performance_logger_middleware(get_response):
    def middleware(request):
        startTime = time.time()
        response = get_response(request)
        duration = time.time() - startTime
        response["x-Page-Duration-ms"] = int(duration * 1000)
        logger.info("%s %s %s", duration, request.path, request.GET.dict())
        return response
    
    return middleware