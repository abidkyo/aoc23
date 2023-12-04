#!/usr/bin/env bash

# set flag to exit when error
set -eo pipefail

# help function
show_help() {
  cat <<EOF
Usage: get_input.sh DAY

EOF
  exit 1
}

[[ -z $1 ]] && show_help

YEAR="2023"
DAY=$(printf "%d" "$1")
FILENAME=$(printf "%02d" "$1")

curl --silent "https://adventofcode.com/${YEAR}/day/${DAY}/input" \
  --cookie "session=${AOC_SESSION}" \
  -A 'abidkyo @ github.com/abidkyo' \
  -o "./input/day${FILENAME}.txt"

exit 0
