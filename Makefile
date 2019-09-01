.PHONY: test web

web:
	@python3 web/app.py

build-fronend:
	npm run build --prefix web/static/vue-material-dashboard-master

serve-dev-frontend:
	npm run dev --prefix web/static/vue-material-dashboard-master

test:
	@python3 -m unittest discover

purge:
	 @read -p "Are you sure? it will delete all the output folder permanently (Yes/no): " purge; \
	 if [ $$purge == "Yes" ]; then echo $$purge; fi

plot-background:
	@python3 ./src/default_background.py $(BG_ID)

plot-signal:
	@python3 ./src/default_signal.py $(SIGNAL_ID)

plot-clean:
	@python3 ./src/default_clean.py $(SIGNAL_ID) $(BG_ID)

plot-fluctuations:
	@python3 ./src/default_fluctuations.py $(SIGNAL_ID) $(BG_ID)

plot-cwt-clean:
	@python3 ./src/default_cwt_clean.py $(SIGNAL_ID) $(BG_ID) $(WAVELET_ID)

plot-cwt-fluctuations:
	@python3 ./src/default_cwt_fluctuations.py $(SIGNAL_ID) $(BG_ID) $(WAVELET_ID)

echo-this:
ifdef type
	@echo $(type)
else
	@echo "options: echo-this type=type1, echo-this type=type2"
endif
