#!/bin/bash
#script that sends a DELETE request to the URL passed as the first argument
curl -Ls -X "DELETE" "$1"
