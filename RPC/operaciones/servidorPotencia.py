from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

def pow(x, y):
    print(x ** y)
    return x ** y

def main():
    server = SimpleJSONRPCServer(("localhost", 1011))
    server.register_function(pow)
    print("Server is running")
    server.serve_forever()

if __name__ == '__main__':
    main()