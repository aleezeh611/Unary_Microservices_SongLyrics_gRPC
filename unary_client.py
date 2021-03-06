import grpc
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2
import os
class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051
        server_host = os.getenv("SERVER_HOST", "localhost")
 
        # instantiate a channel
        self.channel = grpc.insecure_channel( f"{server_host}:50051" )
        # bind t
        # he client and the server
        self.stub = pb2_grpc.UnaryStub(self.channel)

    def get_lyrics(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    client = UnaryClient()
    songname = "songlyrics/"
    songname += input("Enter song name (with _ instead of space pls) :")
    songname += ".txt"
    result = client.get_lyrics(message=songname)
    if result.received == True:
        print(result.lyrics)
    else:
        print("NO FILE FOUND")