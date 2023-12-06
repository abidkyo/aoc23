#!/usr/bin/env bash

# set flag to exit when error
set -eo pipefail

# help function
show_help() {
  cat <<EOF
Usage: create.sh DAY

EOF
  exit 1
}

[[ -z $1 ]] && show_help

DAY=${1}
FILENAME=$(printf "%02d" "${DAY}")
SRC_FILE="./src/day${FILENAME}.py"

if ! [[ -f "${SRC_FILE}" ]]; then
  cp "./src/template.py" "${SRC_FILE}"
  sed -i "12s/1/${DAY}/" "${SRC_FILE}"
  sed -i "32s/1/${DAY}/" "${SRC_FILE}"
  sed -i "33s/1/${DAY}/" "${SRC_FILE}"
fi

touch "./input/day${FILENAME}.txt"
touch "./input/day${FILENAME}_test.txt"

echo "AOC Day ${DAY} created"

if [[ $(date +%d:%H:%M) > "${DAY}:06:00" ]]; then
  echo "getting input"
  ./get_input.sh "${DAY}"
  google-chrome --new-window "https://adventofcode.com/${YEAR}/day/${DAY}"
fi

exit 0
