from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

def sum(x, y):
    print(x + y)
    return x + y

def main():
    server = SimpleJSONRPCServer(("localhost", 1007))
    server.register_function(sum)
    print("Server is running")
    server.serve_forever()

if __name__ == '__main__':
    main()