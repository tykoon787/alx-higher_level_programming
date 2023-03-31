#!/bin/bash
# Displays HTTP Methods
curl -Is "$1" | grep -i Allow | cut -d ' ' -f2-
