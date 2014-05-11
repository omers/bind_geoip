Using BIND server to serve Geo based queries
==========

Using Bind DNS server to serve queries based on Geo IP location.
This solution is based on open source tools to provide the same functionality as F5 Global Traffic Manager.

The script should be configured to run via cron, update the GeoIP database file (From MaxMind) and build an access list file for BIND dns.

Prerequiests
=========

* Install bind
```
yum -y install bind
```

* Install Python setup tools
```
yum -y install python-setuptools
```

* Create directory named 'geoip' under /etc
```
mkdir /etc/geoip
```

* Copy the update scrip to /etc/geoip
```
cp scripts/update_acs.py /etc/geoip
```
