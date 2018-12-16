#!/usr/bin/env bash
# see README.md for use


# argument
if [ $1 ]; then
  case $1 in

    # start flask app
    start)
      python3 app.py
      ;;

    # run all tests under test/
    test)
      printf "Running all tests...\n\n"
      pytest "test"
      ;;

  esac


# no argument
else
  printf "no argument given\n\n"
fi
