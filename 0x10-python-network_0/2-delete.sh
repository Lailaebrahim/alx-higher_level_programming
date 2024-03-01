#!/bin/bash
#a Bash script that takes in a URL, and send a delete request to it
curl -s -X DELETE "$1"
