#!/usr/bin/pytho3

status = int(input("Enter http_error Code: "))

def http_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something is wrong"
    
http_error(status)
