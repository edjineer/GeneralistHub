# Intro to Web Technology

https://www.youtube.com/@GoogleDevelopers/videos
https://www.youtube.com/@learncodeacademy

TODO: Find 485 notes

## Theoretical Knowledge of Front End Languages

## Protocols

## How the internet Works

ISP does Server Side lookup  
Browswer parses HTML  
Request contains: Headers, and Post Body
Response has Headers and Response Body
LAMP = Linux, Apache for Web Server, MySQL for DB, and PHP for backend language
HTTP Port = 80
Apache

* One server can host multiple websites

Web Application Server

* GEt info from DB and from Filesystem's template

Scaling

* Run on multiple machines with own IP addresses
* Load Balancer
  * DNS points to Load Balancer
  * HAshing algorithm
  * Scaling your website
  * Deployment for all servers for same code


[Web Dev Josean Martinez](https://www.youtube.com/watch?v=ZTLY-7fKy4E)

* Clients and servers
* IP Address, DNS Lookup, domain name to ip address
* HTTP protocol and HTTPS domain
  * Sends HTML back
  * When references to files or style, additional request

[Acedemind: How the Web Works](https://www.youtube.com/watch?v=hJHvdBlSxug)

* Great Diagram highlighting DNS resolution of URL to IP Address
* HTTPS is just encrypted HTTP Protocol, end to end requests and responses.

### Follow Andrew Tutorial Series

What is HTTP How the Internet Works #1 [FollowAndrew](https://www.youtube.com/watch?v=wW2A5SZ3GkI)

* Fiber Optic cables, and travel at speed of light
* HTTP is a protocol for how 2 comps talk to each other
  * Client requests to the server, server responds
  * Server responds with status code
    * 100 = Info
    * 200s are Successes
    * 300= Redirections
    * 400 = Client errors
    * 500 = Server Error
  * Request = Start Line, Headers, and Body
    * Start line = Method, Target, and HTTP Version being used
    * Headers will detail the browser and version there
    * Headers sent by the browser
  * HTTP 1 is Stateless

What is an IP Address How do Domains Work [FA](https://www.youtube.com/watch?v=0QI6I6APomE)

* Domain Names:
  * TLD = Top level domain. Like .com, .net
  * CCLD = Country Code TLD = .uk, .cn
  * GTLDs = Generic TLDs. .dev, .club. Invented bc ran out of .coms
* DNS Servers = Domain Name Servers
  * Maps human readable to an ip address
* Network locations with Hierarchical Addressing
  * 12.34  = Specific organization, narrow down to computer address
  * **traceroute** in terminal
* Registrars = give domain names
  * [WHOIS Database](https://whois.domaintools.com/)
  * Any registration makes private info public, prevented by Privacy Protection
  * ICANN = governing authority for domain names
  * Domain Name Registrar Auctions

What are Internet Cookies and Cache [FA](https://www.youtube.com/watch?v=QYXAxXjaKws)

* Cache
  * Client Machines store cache
  * Temporary storage, files stored on Client Machine
  * Web Browser managest the cache. clears it out
* Cookies
  * Server machine stores the cookie
  * Enables Auto Logins
  * Since HTTP is stateless, Cookies allow continuity to uniquely identify the user
  * Cookies used to track you
  * EU law to let them know if a site uses cookies
* Browser Tools
  * Lots of cookies stored on the site
  * Storage Section of web tools
  * Cookies have values, store lang and currency, etc

### Misc Questions

HTTP version differences

* Head of Line Blocking = **LOOK UP**
* HTTP2 - 2015
  * Transport Protocol: Based on TCP, reliable ordered data delivery
  * Multiplexing: packet loss in one stream delays others
  * Still uses TLS Handshake
* HTTP3 - 2022
  * Transport Protocol based on QUIC: dQuick UDP internet Connections, minimize latency, lost packets are handled independently. 
  * Multiplexing: packet loss in one doesnt hit others
  * Updating to 3 requires updated server and client infrastructure to support QUIC
  * Supported by 25% of top million websites

URI vs URL

REST vs HTTP

TLS Handshake deatils

CDNs



## Data Transfer

## Asynchronous

## Latest at Google

## Google I/O 2011, Life in App Engine Production

[Michael Handler] (https://www.youtube.com/watch?v=rgQm1KEIIuc) 2011

SRE = Site Reliability Engineer

* Google has to be fast and available
* Invisible by Design
* App engine and reliability
* Crisis Response: how can we prevent this from happening again
* Google products are designed for in-place updates
* Data Store
  * Master Slave for replication, catchup period after
    * Swap which data center is the master in order to account for outages
    * Power Outage
    * Everything prevents writes, error gets rippled back upwards to the client's browser
  * High Replication Data Centers
    * Robust about planned and unplanned outages
  * Really fun to hear about
* Trust but verify
  * Every piece of HW has tried to corrupt data
  * No bad people, but lots of bad HW
* Become agile: move quickly
* Expect the Unexpected
  * Gremlins pop uout of the systems, make sure you get out the gremlins cousin
  * You have to have distributed systems: cant be behind the same power, geography, etc
  * There is a ceiling to reliability
* Build Off Switches into the system. Efficiencies come at a large scale
* Excitement in troubleshooting
* Transparency
  * Communication is key: if there's an issue, they need to know about it

Alan Green: Monitoring API

Other Google Videos

* https://www.youtube.com/watch?v=_8cH-QPVXsw


## Google Cloud Console 
https://cloud.google.com/functions/docs/console-quickstart

https://cloud.google.com/docs/get-started