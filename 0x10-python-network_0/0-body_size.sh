#!/bin/bash
#takes in a URL, sends a request to that URL, and displays the size fo the
# body of the response
curl -s -o /dev/null -w "%{size_download}" "$1"
