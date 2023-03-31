#!/bin/bash
# Script that displays the size of the body of the response
curl -sI "$1" | grep Content-Length | grep -oE '[0-9]+' | awk '{print $1}'