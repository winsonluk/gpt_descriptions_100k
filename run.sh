#!/bin/sh

while true; do
  nohup python ~/gpt_descriptions_100k/generate_descriptions.py $(($(wc -l ~/gpt_descriptions_100k/io/descriptions100k_with_summaries.txt | cut -f1 -d' ') + 1))
done &
