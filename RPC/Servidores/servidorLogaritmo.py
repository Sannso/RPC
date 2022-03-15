from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from math import log

def logarithm(x, y):
    print(log(x, y))
    return log(x, y)

def main():
    server = SimpleJSONRPCServer(("localhost", 1012))
    server.register_function(logarithm)
    print("Server is running")
    server.serve_forever()

if __name__ == '__main__':
    main()