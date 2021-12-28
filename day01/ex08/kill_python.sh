#!/bin/bash

kill -9 $(ps | grep -E ".+\.py | awk '{if ($3 > 300) {print $2}}')
