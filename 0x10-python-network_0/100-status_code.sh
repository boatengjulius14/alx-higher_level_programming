#!/bin/bash
# sends request and displays status code
curl -so /dev/null -w "%{http_code}" "$1"
