# grpc-msgs

Exploration of gRPC message limits

This is a minimalist sample to exercise limits of gRPC response messages, while
comparing repeated messages vs streaming messages.

The server receives a request containing the number of bytes per row and the
number of rows to generate.

It generates a random string for each row and adds a CRC32 check. The CRC32
is validated on the client.

The client makes the request twice: once using a repeated field
and again using streaming. It reports the time taken for each
type of request.

If the size of the message will exceed 1 Gb, only streaming is used. The
Python server errors out with a message size larger than 1 Gb.
