#!/usr/bin/env bash
# takes in a URL and displays the size
curl -sI $"1" | grep "Content-Length" | awk '{print $2}'