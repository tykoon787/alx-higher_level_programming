#!/usr/bin/env bash
# Script that displays the size of the body of the response
URL=$1
curl -sI "$URL" | grep Content-Length | grep -oE '[0-9]+' | awk '{print $1}'