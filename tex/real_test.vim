" Test script to verify UltiSnips expansion
e test.tex
sleep 200m
" Go to a blank line and enter insert mode
normal! GA
" Try typing // to trigger fraction snippet
call feedkeys("i$ //", 'tx')
sleep 200m
" Now try to expand with Tab
call feedkeys("\<Tab>", 'tx')
sleep 200m
" Save and show the result
w! /tmp/ultisnips_test_output.tex
qa!
