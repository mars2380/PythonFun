#!/usr/bin/env bash

function checkpasswd {
  local pwned sha siteout
  read -p 'Try me: ' -s pwned
  sha=$(echo -n "$pwned" | sha1sum | awk '{ print $1 }')
  siteout=$(curl -s https://api.pwnedpasswords.com/range/${sha:0:5})
  if ! grep -i "${sha: -((${#sha}-5))}" <<<"$siteout"
    then echo 'OK'
  fi
}

checkpasswd