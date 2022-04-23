#!/bin/bash
# Sends a GET request to a given URL and display the response status code.
curl -sI -w '%{response_code}' "$1" -o /dev/null
