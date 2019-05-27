# Python Example


## To Build

It is highly recommended to setup a virtual environment first.

Install grpc and the grpc-tools package
```
pip install grpcio
pip install grpcio-tools
```

then generate the Python code

```
python -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. route_guide.proto
```

## Start the server

```
python route_guide_server.py
```

## Start the client.

The client takes the following command lines arguments:

```
-b  Number of bytes per row
-n  Number of rows
-m  Maximum message size
-p  pagesize. Simulate paging with a given pagesize
```

The client will display a status update for every 1,000 streaming rows received.

Example: generate 50 rows of 1024 bytes

```
python route_guide_client.py -b 1024 -n 50
```

Example: generate 10000 rows of 1 kb using 10,400,000 message size
```
python route_guide_client.py -b 1024 -n 10000 -m 10400000
```

Example: generate 2 rows of 100 Mb using a 500 Mb message size
```
python route_guide_client.py -n 2 -b 134217728 -m 536870912
```

Example: generate 10001 rows of 1 kb using a page size of 100
```
python route_guide_client.py -b 1024 -n 10001 -p 100 -m 10401040
```
## Credits

This is based on the gRPC
[route guide](https://grpc.io/docs/tutorials/basic/python/) example.
