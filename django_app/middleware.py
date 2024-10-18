import logging

logger = logging.getLogger(__name__)

class LogRequestMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code executed for each request before the view is called.
        logger.info(f"Request Method: {request.method}, Path: {request.path}")

        response = self.get_response(request)

        # Code executed for each response after the view is called.
        return response
