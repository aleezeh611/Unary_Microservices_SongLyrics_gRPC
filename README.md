# Unary_Microservices_SongLyrics_gRPC
💻How to run:
1. python -m grpc_tools.protoc --proto_path=. ./unary.proto --python_out=. --grpc_python_out=.  *(To make stubs from the .proto file)*
2. python3 unary_server.py
3. python3 unary_client.py 

✋Help taken from: https://www.velotio.com/engineering-blog/grpc-implementation-using-python
