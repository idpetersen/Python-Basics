#!/bin/bash

# http://shell.fullstackacademy.com:56694/
mkdir /tmp/spider_result

wget -q -r "http://shell.fullstackacademy.com:56694/" -P /tmp/spider_result

grep --color=auto -r "FS{" /tmp/spider_result

rm -rf /tmp/spider_result

