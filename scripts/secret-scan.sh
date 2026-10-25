#!/usr/bin/env bash
# Fail the build if obvious secrets are committed to the repository.
set -euo pipefail

patterns='(AKIA[0-9A-Z]{16}|-----BEGIN (RSA|OPENSSH|EC|DSA|PGP|PRIVATE) KEY-----|xox[baprs]-[0-9A-Za-z-]{10,}|ghp_[0-9A-Za-z]{36}|github_pat_[0-9A-Za-z_]{20,}|sk_live_[0-9A-Za-z]{20,}|AIza[0-9A-Za-z_\-]{35})'

if grep -RInaE "$patterns" \
    --exclude-dir=.git \
    --exclude-dir=node_modules \
    . ; then
  echo "::error::Potential secret detected - aborting deploy."
  exit 1
fi

echo "Secret scan clean."
