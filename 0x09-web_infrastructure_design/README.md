# Web Infra
### DNS
DNS converts text-based domain names to machine-adapted ip addresses.

When DNS is converting a domain name, the browser and OS first check their caches.
If they can't, they check with the resolver.
The resolver is usually the ISP (Internet service provider).
The resolver also first checks their cache to see if the domain name is known. If it's not,
the root server is consulted.
The root name server (of which there are 13 serviced by 12 independent orgs) checks for the domain name.
If it doesn't have it, it provides the .com tld (top level domain) address which the resolver stores for future
use (instead of repetitive requests to the root name server).
the tld server provides authoritative name servers addresses of which one of them provides the ip address to
the domain name.

An A record (Address record) maps the domain name to the ip address of the computer hosting the domain.
a CNAME (Canonical name) maps one domain to another. Useful when running multiple servers (ftp, web...) 
from one ip address.
MX - a mail exchanger record (MX record) specifies the mail server responsible for accepting messages on behalf
of a domain name.

In both TCP and UDP, port numbers start at 0 and go up to 65535. The lower ranges are dedicated to common 
internet protocols such as port 25 for SMTP and port 21 for FTP. 
