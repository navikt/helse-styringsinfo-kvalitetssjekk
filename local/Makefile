.PHONY: $(shell sed -n -e '/^$$/ { n ; /^[^ .\#][^ ]*:/ { s/:.*$$// ; p ; } ; }' $(MAKEFILE_LIST))

this_dir := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

help:
	 @echo "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\\x1b[36m\1\\x1b[m:\2/' | column -c2 -t -s :)"

python-bootstrap: # Setter opp miljø - antar at man har Homebrew
	brew install jq
	brew install poetry
	poetry install

run-soda-scan: python-bootstrap ## Kjører sjekker
	gcloud --format=json auth list | jq --exit-status '.[] | select(.status == "ACTIVE")' || gcloud auth login
	# gcloud config set project tbd-dev-7ff9
	poetry run python ./soda-scan.py
