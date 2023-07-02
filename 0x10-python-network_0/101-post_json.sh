#!/bin/bash
# sends a JSON POST to a URL and displays response body
curl -H "Content-Type: application/json" -sX POST -d "@$2" "$1"
