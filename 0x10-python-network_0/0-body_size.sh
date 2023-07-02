#!/bin/bash
#takes in a URL, sends a request to that URL, and displays the size fo the
# body of the response
curl -sw "\n%{size_download}\n" "$1" | tail -1
