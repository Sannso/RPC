from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

def sub(x, y):
    print(x - y)
    return x - y

def main():
    server = SimpleJSONRPCServer(("localhost", 1008))
    server.register_function(sub)
    print("Server is running")
    server.serve_forever()

if __name__ == '__main__':
    main()