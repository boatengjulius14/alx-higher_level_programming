#!/bin/bash
# request to a URL and respond with message containing "You got me!"
curl -sLH "Origin: HolbertonSchool" -d "user_id=98" -X PUT 0.0.0.0:5000/catch_me
