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

DAY=$(printf "%02d" "$1")
SRC_FILE="./src/day${DAY}.py"

if ! [[ -f "${SRC_FILE}" ]]; then
  cp "./src/template.py" "${SRC_FILE}"
  sed -i "12s/1/${1}/" "${SRC_FILE}"
  sed -i "32s/1/${1}/" "${SRC_FILE}"
fi

touch "./input/day${DAY}.txt"
touch "./input/day${DAY}_test.txt"

echo "AOC Day${DAY} created"

if [[ $(date +%d:%H:%M) > "${1}:06:00" ]]; then
  echo "getting input"
  ./get_input.sh "$1"
fi

exit 0
