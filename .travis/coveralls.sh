#!/bin/sh

if [ "$TOXENV" = "cover" ]; then
    coveralls
fi
