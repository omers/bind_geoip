#!/usr/bin/env python
#
# Author: Omer Segev
# Date: 05/11/2014
# Purpose: Download GeoIPCountryCSV file and build BIND dns access list file
#


import sys
import netaddr
import csv
import urllib
import zipfile
import subprocess
import datetime

# Main Variables
geo_ips = {}
input_file = "GeoIPCountryWhois.csv"
output_file = "GeoIP.acl"
acl_file = open(output_file,"w")
file_url = 'http://geolite.maxmind.com/download/geoip/database/GeoIPCountryCSV.zip'


# Function definitions

def download_file():
  print "%s - Downloading MaxMind Geo IP File" % datetime.datetime.now()
  try:
    urllib.urlretrieve(file_url,"GeoIPCountryCSV.zip")
  except:
    print "%s - There was an error downloading MaxMind Geo IP File" % datetime.datetime.now()
    sys.exit(1)
  
def extract_file():
  print "%s - Extracting GeoIP file" % datetime.datetime.now()
  try:
    zf = zipfile.ZipFile("GeoIPCountryCSV.zip")
    zf.extract(input_file,".")
  except:
    print "%s - Error extracting GeoIP file" % datetime.datetime.now()
    sys.exit(1)

def main():
  print "%s - Building GeoIP Access list file" % datetime.datetime.now()
  with open(input_file,"rb") as f:
    data = csv.reader(f)
    for line in data:
      start_ip = line[0]
      end_ip = line[1]
      longtitude = line[2]
      latitude = line[3]
      country_code = line[4]
      country = line[5]
      cidr = netaddr.iprange_to_cidrs(start_ip,end_ip)
      geo_ips.setdefault(country_code,[]).append(cidr)
  for k,v in geo_ips.iteritems():
    nets = []
    for item in v:
      ip = str(item[0])
      nets.append(ip)
    acl_file.write("acl \"%s\" { %s ; } ; \n" % (k,'; '.join(nets)))
  acl_file.close()
  print "%s - GeoIP Access file created" % datetime.datetime.now()
  try:
    subprocess.call("/etc/init.d/named reload", shell=True)
  except:
    print "%s - Error reloading BIND configuraion" % datetime.datetime.now()


# Main script

if __name__ == "__main__":
  download_file()
  extract_file()
  main()

# END
