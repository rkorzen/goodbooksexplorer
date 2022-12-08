def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("request", request)
        response = get_response(request)
        print("response", response)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware