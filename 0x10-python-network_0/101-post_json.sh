#!/bin/bash
#Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -s -H "Content-Type: application/json" --upload-file "$2" "$1"
