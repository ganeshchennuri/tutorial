# Backend Engineering 
- Special thanks to Nasser Hussein [youtube](https://www.youtube.com/c/HusseinNasser-software-engineering/)
## OSI model
- For a local n/w when a request is sent on a browser to any device like 192.168.31.12:80
- The actual process for the get request is via OSI model
- steps
    1. Application Layer (the actual representation of data)
    2. Presentation layer (encryption of data)
    3. Session Layer (identifying sessions)
    4. Transport Layer (data is divided into segments with source & destination port mapping)
    5. Network layer (each segment can have multiple data packets with source & destination ips attached)
    6. Data link layer (Data packets can be further divided into smaller frames & mac address of both source & destination is alsl attached, ARP helps mappping)
    7. Physical Layer (bunch of 1's & 0's)
    ![Image](./backend_engg_snapshots/osi_model.png "OSI MODEL")
- Wifi router - router receives radio signals & it sends the data frames to all the devices in a multicast network (can be uni or multicast) , the Network card ina device identifies & accepts or rejects the data frames
- So it is not recommended to browse http websites on public internet, as anyone might reconfigure network card to accept all the traffic
    ![Image](./backend_engg_snapshots/osi_router.png "OSI MODEL")
- One can have 7 different tcp connections with webserver with diffreent sessions

> Later https://youtu.be/dh406O2v_1c


# HTTP
## HTTP Requests & Responses
- Req have 4 contents url, method type, headers, body
- Response have status code, headers, body

## Web Server & making requests to server
- one can simply create & spin up nodejs webserver using http-server library
- npm -g install http-server & http-server . => will run http server in current dir
- Browser first sends the request, server gives back a response text/html or image or any other stuff.
the referenced urls in response page are requested afterwards to accumulate all the data.
- One can also make a http request using simple javascript using fetch API
> fetch("localhost:8080").then(a=> a.text()).then(console.log)

## How it works
- Http works in layer 7 of OSI model, called as layer7 protocol.
- HTTP opens a tcp connection & closes the tcp connection after receiving data.
- tcp handshake is done first & data is sent & recieved

### HTTP 1(1996)
- creates a new tcp connection for each request,it is slow & buffering

### HTTP 1.1(survived for almost 20yrs, HTTP2 in 2015)
- invented keep-alive header,so connection is not closed until both parties wishes to close
- Persisted TCP connection, low latency, streaming & chunked transfer(image loading part by parts)
- Pipelining (disabled by default), all req are sent & client wait for response

### HTTP/2
- Compression, Multiplexing(multiple connections are sent in one tcp request)
- Server Push (Faster)
- SPDY
- secure by default
- Protocol Negotiation during TLS(NPN/ALPN) - client negotiates type of protocol with server (http1,2,etc) done in tls handshake
- Next protocol negotiation, replaced by Application layer protocol negotiation

### HTTP/2 over QUIC (HTTP/3)
- 2018 sept adoped by internet engg task force
- replaces with TCP with QUIC (UDP with congestion control)
- all HTTP/2 features
- Still experimental

## HTTP Params & Query Strings
- Params or url params is an identifier which can be further used for other purposes userid in this case - https://localhost:3000/user/5896544
- Query strings or query params are the key value pairs - https://localhost:3000/user?userId=5896544

# Etags
- etags are assigned by server on first requests for caching
- etags are attached to each request & server identifies req with it, if data not modified old data is returned
- etag logic is created on webserver, can be hash of last modified data for a file, then it is compared with requests etag
- etags can also be used to monitor user actions, by pausing new creation of etags

# Zombie Cookies
- a cokies once deleted, can also be re created mainly used for tracking
- cookie even works in incognito mode, even it is created on normal browsing.
- can be done using multiple ways, for eg. e-tags 


# TCP AND UDP
## TCP
- TCP protocol is stateful protocol starts first with a 3-way handshake
- when Client sends http get request, SYN (sequence number for packet) is sent to the server, server acknowledges ACK & send back its SYN (sequence number would be 32bit random integer), the client then sends ACK, the 3-way handshake is done & connection is established
- Server now sends data to the get request, when client acknowledges it, the TCP connection is closed
    ![Image](./backend_engg_snapshots/tcp_handshake.png "TCP Handshake")
- creating a tcp server using nodejs
    ```js
    const net = require("net")

    const server = net.createServer(socket => {
        socket.write("Hello.")
        socket.on("data", data => {
            console.log(data.toString())
        })
    })

    server.listen(8080)
    ```
- HTTP/2 does multiplexing by combining multiple requests into streams in a single tcp connection(multiprocessing in single tcp conn)

## UDP
- UDP protocol is a stateless protocol, when a client requests some information, data is sent to the client and the server does not wait for acknowledgement.
- Connectionless, No guranteed delivery, adds CRC checksum to the packet to check it is bad or good for rejecting it.
- No congestion control (it sends data, doesn't care if there's traffic)
- No ordering of packet, no sequence numbers, no headers
- Security concerns since its conncetion less and keeps sending data whoever asks for it (lot of firewalls disables UDP for this reason)
- Pros like smaller packets(no headers), hence consumes less bandwidth and faster
- sample code
    ```js
    const dgram = require('dgram');
    const socket = dgram.createSocket('udp4');

    socket.on('message', (msg, rinfo) => {
    console.log(`server got: ${msg} from ${rinfo.address}:${rinfo.port}`);
    });

    socket.bind(8081);

    ```

## TCP Slow start
- slow start is implemented in TCP to avoid congestion
- sometimes the server is capable of handling multiple requests & but the network which is transferring the data might not be that much capable
- So TCP slow start is a mechanishm where the window of sending recieving data is minimun at start & increases gradually as we receive data & if any issues in acknowledgements or erros
client will start reducing the congestion window where it can communicate efficiently with server

## TCP fast open cnnection
- if bot client & server support fast open connection, client sends fast open connection along with syn
- server sends the fast open cookie(Cryptographic hash) along with SYN/ACK
- useful in http 1.1, not kuch useful in http/2
- next time the client sends the requests, it will send syn along with fast open cookie& get request
- server acknowledges the SYN and also send the data along with SYN
- supported by curl

- HTTP/2 we can multiplex many requests in single tcp connection, but jn HTTP 1.1 we send tcp conn for each request
- slow start is congestion control(eager loading) & lazy loading(tcp fast open)

## TCP half open connection
- so in hlaf open connection, client will not response to SYN/ACK by server
- server tries to resend & eventually closes the tcp connection
- can be used to chexk if the port is open

## SYN flood
- when a client opens a half open tcp connection, server waits for ACK & teies to resend the SYN/ACK
- so when source ip is spooofed & multiple requests are sent to server with different source ip's, the tcp networks flood & block the memory
- can also be a DDOS


# WebServers