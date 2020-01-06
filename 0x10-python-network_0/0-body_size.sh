#!/bin/bash
# Script print the size of the body response
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
