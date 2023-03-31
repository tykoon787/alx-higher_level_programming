#!/bin/bash
# Sends a POST Request
curl -sX -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
