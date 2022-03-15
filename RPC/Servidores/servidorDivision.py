from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

def div(x, y):
    print(x / y)
    return x / y

def main():
    server = SimpleJSONRPCServer(("localhost", 1010))
    server.register_function(div)
    print("Server is running")
    server.serve_forever()

if __name__ == '__main__':
    main()