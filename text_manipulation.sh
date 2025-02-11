#read email from a lof file

grep -E -o "[a-zA-Z0-9]+[a-zA-Z0-9]+\\[a-zA-Z]{2,}" log.txt

grep -e "error" log.txt

awk "ERROR" log.txt