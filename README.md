Using BIND server to serve Geo based queries
==========

Using Bind dns server to serve queries based on Geo IP location. Same functionality as F5 Global Traffic Manager

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
