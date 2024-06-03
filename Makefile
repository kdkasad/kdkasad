README.md: README.md.in generate_icons.py icons.csv
	cat $< > $@
	echo '<div>' >> $@
	./generate_icons.py < icons.csv >> $@
	echo '</div>' >> $@
