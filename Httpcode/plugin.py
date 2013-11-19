###
# Copyright (c) 2013, Jesus Roncero
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Httpcode')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x

httpcodes = {
    '100' : "100 Continue: The client SHOULD continue with its request",
    '101' : "101 Switching Protocols. The server understands and is " 
            "willing to comply with the client's request, via the "
            "Upgrade message header field, for a change in the application "
            " protocol being used on this connection",
    '200' : "200 OK. The request has succeded",
    '201' : "201 Created. The request has been fulfilled and resulted "
            "in a new resouce being created",
    '202' : "202 Accepted.",
    '203' : "203 Non-Authoritative Information",
    '204' : "204 No Content",
    '205' : "205 Reset Content",
    '206' : "206 Partial Content",
    '300' : "300 Multiple Choices",
    '301' : "301 Moved Permanently",
    '302' : "302 Found",
    '303' : "303 See Other",
    '304' : "304 Not Modified",
    '305' : "305 Use Proxy",
    '306' : "306 Unused. Reserved use.",
    '307' : "307 Temporary Redirect.",
    '400' : "400 Bad Request.",
    '401' : "401 Unauthorized.",
    '402' : "402 Payment Required.",
    '403' : "403 Forbidden",
    '404' : "404 Not Found",
    '405' : "405 Method Not Allowed",
    '406' : "406 Not Acceptable",
    '407' : "407 Proxy Authentication Required",
    '408' : "408 Request Timeout",
    '409' : "409 Conflict",
    '410' : "410 Gone",
    '411' : "411 Length Required",
    '412' : "412 Precondition Failed",
    '413' : "413 Request Entity Too Large",
    '414' : "414 Request-URI Too Lond",
    '415' : "415 Unsupported Media Type",
    '416' : "416 Request Range Not Satisfiable",
    '417' : "417 Expectation Failed",
    '500' : "500 Internal Error",
    '501' : "501 Not Implemented",
    '502' : "502 Bad Gateway",
    '503' : "503 Service Unavailable",
    '504' : "504 Gateway Timeout",
    '505' : "505 HTTP Version Not Supported",
    '666' : "666 Devil Packet Found."} # little easter egg.

class Httpcode(callbacks.Plugin):
    """Add the help for "@plugin help Httpcode" here
    This should describe *how* to use this plugin."""
    
    def __init__(self, irc):
    	self.__parent = super(Httpcode, self)
    	self.__parent.__init__(irc)
    	self.rng = random.Random()
    	self.rng.seed()

        # Stuff for Supybot
        self.__parent.die()

    def httpcode(self, irc, msg, args):
        """Returns the definition of an HTTP code"""
        channel = msg.args[0]
        irc.reply('you asked me: %s' % len(args) )

    def httpcode(self, irc, msg, args, code):
        """<http code>
        
        Get the description for HTTP code <http code>
        """
        if code < 1:
            irc.error('you wish!')
            return
        elif code > 600:
            irc.error('Not so fast there...')
            return
        if httpcodes.has_key(str(code)):
            irc.reply(httpcodes[str(code)])
        else:
            irc.error("I don't know anything about HTTP code %s" % code)
    httpcode = wrap(httpcode, ['int'])

Class = Httpcode


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
