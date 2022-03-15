from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

def mul(x, y):
    print(x * y)
    return x * y

def main():
    server = SimpleJSONRPCServer(("localhost", 1009))
    server.register_function(mul)
    print("Server is running")
    server.serve_forever()

if __name__ == '__main__':
    main()