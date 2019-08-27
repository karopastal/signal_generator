.PHONY: test

test:
	@python3 -m unittest discover

purge:
	 @read -p "Are you sure? it will delete all the output folder permanently (Yes/no): " purge; \
	 if [ $$purge == "Yes" ]; then echo $$purge; fi

plot-background:
	@python3 ./src/default_background.py

plot-signal:
	@python3 ./src/default_signal.py

plot-clean:
	@python3 ./src/default_clean.py

plot-fluctuations:
	@python3 ./src/default_fluctuations.py

plot-cwt-clean:
	@python3 ./src/default_cwt_clean.py

plot-cwt-fluctuations:
	@python3 ./src/default_cwt_fluctuations.py

echo-this:
ifdef type
	@echo $(type)
else
	@echo "options: echo-this type=type1, echo-this type=type2"
endif
