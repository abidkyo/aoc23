#!/usr/bin/env bash

# set flag to exit when error
set -eo pipefail

# help function
show_help() {
  cat <<EOF
Usage: run.sh DAYSTART [DAYEND]

EOF
  exit 1
}

EXEC=python3

# option parsing
while getopts "p" opt; do
  case $opt in
  p)
    EXEC=pypy3
    echo "using pypy"
    ;;

  *)
    show_help
    ;;
  esac
done
shift $((OPTIND - 1))

[[ -z $1 ]] && show_help

range=$(seq "$1" "$1")

if [[ -n $2 ]]; then
  range=$(seq "$1" "$2")
fi

for i in $range; do
  day=$(printf "%02d" "$i")
  echo -n "day${day}: "
  ${EXEC} "./src/day${day}.py"
done

exit 0
