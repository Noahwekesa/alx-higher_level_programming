#!/bin/bash
# Bash script that takes in a url, sends a request to that URL

if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

url=$1

Rsize=$(curl -sI $url | grep -i content-length | awk '{print $2}')
echo "$Rsize"
