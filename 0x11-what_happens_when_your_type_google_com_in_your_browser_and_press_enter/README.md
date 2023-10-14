WHAT HAPPENS WHEN YOU TYPE GOOGLE.COM IN YOUR BROWSER AND PRESS ENTER
--------------------------------------------------------------------------------------------------------------------
With a market share of 83.43%, according to statistica.com, there’s a high probability that you have used Google at some point. Google handles more than 8.5 billion searches per day. But what happens when you key in the google.com characters and hit enter?
In this article, we’ll have an in-depth analysis of what happens under the hood as well as on the web.
-----------------------------------------------------------------------------------------------------------------
DNS LOOKUP
-----------------------------------------------------------------------------------------------------------------
To connect to google.com, your browser (Chrome, Bing, etc.) must figure out which server to connect to. The server to connect to hosts the website Google.com and is identified by a unique address known as an IP address (I’ll be writing an article about IP addresses be sure to follow me). How, then, does this happen when you only type in characters as opposed to the IP address?
The answer lies in the DNS lookup. When you type in the URL, the first thing that happens is that your browser identifies the domain name to be translated to the IP address. The DNS lookup has to be lightning-fast. To achieve this, the browser searches for the IP address in its cache, the operating system cache, the local network cache at your router, the DNS server cache on your corporate network, or at your Internet Service Provider (ISP). If the IP address is not found at any of these locations, the DNS servers at your ISP perform a recursive search on all the DNS servers around the internet. If not found, the DNS servers continue the recursive search until the IP address is found.
-----------------------------------------------------------------------------------------------------------------
TCP CONNECTION
------------------------------------------------------------------------------------------------------------------
Once Google’s IP address is found, it’s time to connect to the internet. The browser achieves this by initiating a TCP connection (Follow me on X @DevWambugu for concise tech tweets). The browser sends a SYN packet to the web server - the SYN packet requests a connection between the two computers. The SYN packet contains the IP address and port number of the browser. Once the web server receives the SYN packet, it responds with a SYN-ACK packet which is then received by the browser. Once the web browser receives the SYN-ACK packet, it responds with the ACK packet to complete the connection.
-----------------------------------------------------------------------------------------------------------------
FIREWALL
-----------------------------------------------------------------------------------------------------------------
Connections to the servers are prone to malicious attacks and software. As a protective mechanism, web servers apply firewalls. Firewalls are essentially software that sets rules about what can connect to or leave a network. Through these applications, web servers are able to protect themselves from hackers.
------------------------------------------------------------------------------------------------------------------
THE WEB SERVER
------------------------------------------------------------------------------------------------------------------
A web server is software and hardware that uses protocols to respond to a client’s request, HTTPS in our case. Web servers display webpages to clients. 
Web servers can either be static or dynamic. Static web servers serve data as is, while dynamic web servers allow the updating of data before it is sent to the web browser. 
Dynamic webservers consist of application servers and the database.
-----------------------------------------------------------------------------------------------------------------
APPLICATION SERVERS
-----------------------------------------------------------------------------------------------------------------
The application server is a software system that resides between the operating system and the database. Its main purpose is to deliver dynamic content. The application server allows the client to interact with the server-side application code and deliver dynamic content search as real-time analytics and transaction results.
-----------------------------------------------------------------------------------------------------------------
DATABASE
-----------------------------------------------------------------------------------------------------------------
A database is an organized collection of structured information in a computer. There are many types of databases, such as object-oriented and relational databases, but relational databases, such as SQL, are the defacto databases for websites. Database software creates, stores, edits, and maintains records and files, allowing for their fast retrieval.
-----------------------------------------------------------------------------------------------------------------
LOAD BALANCER 
------------------------------------------------------------------------------------------------------------------
To improve the website’s (Google’s) scalability, reliability, and performance, a load balancer is applied to distribute client requests to a group of web servers. In HTTPS connections, the load balancer also encrypts and decrypts data transported via the HTTPS connection. The encryption and decryption of data are crucial as they set the web and application servers free to perform the jobs they are designed to do. This greatly improves the performance of the website. Additionally, if the connection between the web server, the application server, and the load balancer is secure, you only need to manage the SSL certificate on the load balancer. This makes it efficient.
-----------------------------------------------------------------------------------------------------------------
HTTPS REQUEST AND RESPONSE
-----------------------------------------------------------------------------------------------------------------
There are 2 types of requests. HTTP requests (covered below) and HTTPS requests. HTTPS requests are more secure since they encrypt clients' data. The data is protected from unauthorized access. Hackers may access your sensitive data if it’s not encrypted. They only need to intercept your connection and identify which port you are listening on. The establishment of a secure connection is achieved through Secure Sockets Layer (SSL) certificates, also known as digital certificates.  Google.com uses the HTTPS protocol.
To share data between the web server and browser, the following happens:
1. The browser attempts to connect to the website (Google.com)
2. The browser requests the web server to establish itself
3. As a response, the web server sends a copy of the SSL certificate to the browser.
4. The browser then inspects the SSL certificate and checks whether it can be trusted. If it can be trusted, the browser signals the web server.
5. The web server responds by sending a digitally signed acknowledgment, and a session is initiated.
6. Encrypted data is shared between the web server and the web browser.
-----------------------------------------------------------------------------------------------------------------
HTTPS RESPONSE
----------------------------------------------------------------------------------------------------------------
The web browser receives the HTTPS response in the form of HTML code that describes the structure of the requested webpage. The browser renders the page to create a visual representation of the web page. One point to note is that as the browser renders the page, it makes additional requests to get images, JavaScript, CSS, and data.
-----------------------------------------------------------------------------------------------------------------
HTTP REQUEST (CAVEAT)
-----------------------------------------------------------------------------------------------------------------
For the less secure HTTP request, the browser sends an HTTP request requesting the webpage. The HTTP request contains the following: the URL page, the HTTP method (GET, POST, etc.), and any additional headers required by the web browser. The browser responds by serving the webpage or a 404 error if the page is not found.
----------------------------------------------------------------------------------------------------------------
TCP Connection Close
------------------------------------------------------------------------------------------------------------------
Once the browser finishes rendering the webpage, it closes the TCP connection. Closing the TCP connection can be achieved in two ways. The Half-Close and the Full-Close. Like many other sites, Google follows the same protocol once the data transfer is complete. The browser sends a FIN signal to signal that it has finished sending the data. The other end receives the signal and may also launch a half-close to signal that it has finished sending data. Once the two ends acknowledge the FINS, a full close is performed, indicating that the connection is closed.

The process described in this article takes place in milliseconds, if not nanoseconds. Web infrastructure design sounds complex on paper due to the numerous protocols that are involved, but it’s a simple concept when well-researched and understood. This article is not limited to the domain google.com. It could help you identify and solve problems that may arise when surfing the web.
