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

# Main Variables
geo_ips = {}
input_file = "GeoIPCountryWhois.csv"
output_file = "GeoIP.acl"
acl_file = open(output_file,"w")
file_url = 'http://geolite.maxmind.com/download/geoip/database/GeoIPCountryCSV.zip'


# Function definitions

def download_file():
  print "Downloading MaxMind Geo IP File"
  try:
    urllib.urlretrieve(file_url,"GeoIPCountryCSV.zip")
  except:
    print "There was an error downloading MaxMind Geo IP File"
    sys.exit(1)
  
def extract_file():
  print "Extracting GeoIP file"
  try:
    zf = zipfile.ZipFile("GeoIPCountryCSV.zip")
    zf.extract(input_file,".")
  except:
    print "Error extracting GeoIP file"
    sys.exit(1)

def main():
  print "Building GeoIP Access list file"
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
  subprocess.call("/etc/init.d/named reload", shell=True) 


# Main script

if __name__ == "__main__":
  download_file()
  extract_file()
  main()

# END
