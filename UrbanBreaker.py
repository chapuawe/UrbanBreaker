import sys
from cam import cam_breaker
from optparse import OptionParser

print "\n Welcome to UrbanBreaker, this framework is for the active hacktivisters"
print " this combine the wifi, network, cell phones, cameras pentest\n\n"

parser = OptionParser()
parser.add_option("--cb", action="store", type="string", dest="cambrute")

(options, args) = parser.parse_args()

if ( len(str(options.cambrute)) >= 8):
	host, port = options.cambrute.split(":")
	cam_breaker.breaker(host, port)
else:
	print " OPTIONS:\n"
	print "   --cb camera brute force, syntax: ip:port"
	print "        example: --cb 1.1.1.1:80\n"