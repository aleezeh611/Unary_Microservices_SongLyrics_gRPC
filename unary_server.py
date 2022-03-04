import grpc
from concurrent import futures
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2
from pathlib import Path

def read_text_file(file_path):
    checkfile = Path(file_path)
    if checkfile.is_file():
        with open(file_path, 'r') as f:
            temp =f.read()
            return temp 
    return -1

class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass 

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        message = request.message
        song_data = read_text_file(message)
        if song_data == -1:
            result = {'lyrics':"none", 'received': False}
        
        else:
            print("FILE NAME RECEIVED : " + message)
            result = {'lyrics': song_data, 'received': True}

        return pb2.MessageResponse(**result) 



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

    