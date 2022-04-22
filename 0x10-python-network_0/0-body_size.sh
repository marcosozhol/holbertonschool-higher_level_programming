#!/usr/bin/env bash
# takes in a URL and displays the size
curl -i 0.0.0.0:5000 | grep "Content-Length"