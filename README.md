Using BIND server to serve Geo based queries
==========

Using Bind dns server to serve queries based on Geo IP location. Same functionality as F5 Global Traffic Manager

Prerequiests
=========

1. Install bind
```
yum -y install bind
```

2. Install Python setup tools
```
yum -y install python-setuptools
```

3. Create directory named 'geoip' under /etc
```
mkdir /etc/geoip
```

4. Copy the update scrip to /etc/geoip
```
cp scripts/update_acs.py /etc/geoip
```
