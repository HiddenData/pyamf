# -*- encoding: utf8 -*-
#
# Copyright (c) 2007 The PyAMF Project. All rights reserved.
# 
# Thijs Triemstra
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

"""
Twisted Remoting server example.

@author: Thijs Triemstra
"""

from twisted.web import http

from pyamf import remoting, gateway
from pyamf.gateway.twistedmatrix import TwistedGateway 


def echo(data):
    return data

class MyHttp(http.HTTPChannel):
    """
    """

class MyHttpFactory(http.HTTPFactory):
    protocol = MyHttp
    
if __name__ == '__main__':
    services = {
        'echo': echo
    }

    gw = TwistedGateway(services)
    
    server = MyHttpFactory()
    server.protocol.requestFactory = gw
    
    port = 8000
    print "Started PyAMF Remoting Gateway for Twisted on port", port

    from twisted.internet import reactor
    reactor.listenTCP(port, server)
    reactor.run()
    