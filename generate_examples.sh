#!/bin/bash
mkdir "docs/source/classes-doc/examples/"
for file in nvd3/*Chart.py; do
   html_filename="docs/source/classes-doc/examples/"`echo $file | sed "s/.*\///" | sed "s/\.py//"`".html"
   echo $html_filename
   echo -e "..\n    _Generated with generated_examples.sh script\n\n.. raw:: html" > $html_filename

   cat $file | grep "Python example" -A1000 | grep -E "Javascript generated|Note that in case you" -m 1 -B 1000 | tail -n+2 | head -n-1 | sed "s/^[ \t]*//g" | python | sed "s/^/        /" >> $html_filename
done

