#!/usr/bin/env bash
# Local preview of score-docs (Jekyll + just-the-docs).
# NOT committed (see .git/info/exclude). Serves at http://localhost:4000
# using _local_config.yml so baseurl is empty (clean local URLs).
#
# Usage:  ./preview.sh        # build + serve, Ctrl-C to stop
#
# Uses the system ruby + bundler (gems vendored under ./vendor/bundle).
# Only the first run is slow (bundle install).
set -e
cd "$(dirname "$0")"
# system ruby installs the bundler executable under the user gem dir
export PATH="$(ruby -e 'print Gem.user_dir')/bin:$PATH"
bundle config set --local path 'vendor/bundle' >/dev/null
bundle install
exec bundle exec jekyll serve \
  --config _config.yml,_local_config.yml \
  -H 127.0.0.1 --livereload --incremental
