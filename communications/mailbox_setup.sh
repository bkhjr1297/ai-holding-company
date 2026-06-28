#!/bin/bash
set -e
apt-get update -qq
apt-get install -y -qq postfix curl
postconf -e "myhostname = $(hostname)"
postconf -e "inet_interfaces = loopback-only"
postconf -e "inet_protocols = ipv4"
service postfix restart
echo 'LocalPostfixReady'
