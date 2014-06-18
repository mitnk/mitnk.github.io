Save it as a file and service it in an http / https server. Tools like FoxyProxy can use it.

    :::javascript
    function FindProxyForURL(url, host)
    {
      // Direct connections to non-FQDN hosts
      if (isPlainHostName(host) ||
         (host == "127.0.0.1") ||
         (host == "*.xxx.com") ||
         (shExpMatch(host, "*.xxx.local")) ||
         (shExpMatch(host, "*.xxx.org")) ||
         (shExpMatch(host, "192.168.*"))) {
           return "DIRECT"
      } else {
        return "PROXY 192.168.1.12:3128"
      }
    }

