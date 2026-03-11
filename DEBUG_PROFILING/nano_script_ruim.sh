#!/bin/sh

# Usar o asterisco direto no for é mais seguro que o ls
for f in *.m3u
do
  # Aspas duplas em "$f" e no padrão de busca
  grep -qi "hq.*mp3" "$f" \
    && echo "Playlist $f contains a HQ file in mp3 format"
done