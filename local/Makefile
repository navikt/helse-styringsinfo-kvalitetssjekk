.PHONY: $(shell sed -n -e '/^$$/ { n ; /^[^ .\#][^ ]*:/ { s/:.*$$// ; p ; } ; }' $(MAKEFILE_LIST))

this_dir := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

help:
	 @echo "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\\x1b[36m\1\\x1b[m:\2/' | column -c2 -t -s :)"

python-bootstrap: # Setter opp miljø - antar at man har Homebrew
	@jq --version || brew install jq
	@poetry --version || brew install poetry
	poetry update

run-soda-scan: python-bootstrap ## Kjører sjekker
	@gcloud --format=json auth list | jq --exit-status '.[] | select(.status == "ACTIVE")' || gcloud auth application-default login
	poetry run python ./soda-scan.py
