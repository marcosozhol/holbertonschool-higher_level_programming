#!/usr/bin/env bash
# takes in a URL and displays the size
curl -i $"1" | grep "Content-Length" | awk '{print $2}'