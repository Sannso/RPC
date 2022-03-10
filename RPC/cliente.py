from jsonrpclib import Server

def main():
    conn = Server('http://localhost:1006')
    print('suma: ', conn.add(5,3))
    print('resta: ', conn.substract(5,3))
    print('multiplicacion: ', conn.mul(5,3))
    print('division: ', conn.div(5,3))

if __name__ == '__main__':
    main()