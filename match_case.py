def http_error(status):
    match status:
        case 400:
            return 'Bad request'
        case 404:
            return 'Not found'
        case 418:
            return 'I\'m a teapot'
        case _:
            return 'Something is wrong with the Internet'
        

if __name__ == '__main__':
    http_error(418)
    