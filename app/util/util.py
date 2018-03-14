'''
Uility functions
'''

def send_401_error():
    response = {
        'status': 401,
        'message': "401 UNAUTHORIZED"
    }
    response.status_code=401
    return response

def send_401_error(message):
    response = {
        'status': 401,
        'message': message
    }
    response.status_code=401
    return response

def send_404_error(message):
    response = {
        'status': 404,
        'message': message
    }
    response.status_code=404
    return response

def send_404_error():
    response = {
        'status': 404,
        'message': "Resource not found"
    }
    response.status_code=404
    return response

def send_400_error():
    response = {
        'status': 400,
        'message': "Bad Request"
    }
    response.status_code=400
    return response

def send_400_error(message):
    response = {
        'status': 400,
        'message': message
    }
    response.status_code=400
    return response

def send_500_error():
    response = {
        'status': 500,
        'message': "Please try later"
    }
    response.status_code=500
    return response

def send_error(status_code, message):
    response = {
        'status': status_code,
        'message': message
    }
    response.status_code=500
    return response