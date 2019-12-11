.PHONY: test web

web:
	@python3 web/app.py

build-web:
	npm run build --prefix web/static/vue-material-dashboard-master && \
	cp -r docs/gallery web/static/vue-material-dashboard-master/dist

serve-dev-frontend:
	npm run dev --prefix web/static/vue-material-dashboard-master

test:
	@python3 -m unittest discover

list-sessions:
	@ls src/signals/sessions

save-session:
	@cp src/backgrounds/default_background.json src/backgrounds/sessions/${NAME}.json && \
	cp src/signals/default_signal.json src/signals/sessions/${NAME}.json && \
	cp src/wavelets/default_wavelet.json src/wavelets/sessions/${NAME}.json && \
	echo session ${NAME} succcessfully saved

load-session:
	@mv src/backgrounds/sessions/${NAME}.json src/backgrounds/default_background.json && \
	mv src/signals/sessions/${NAME}.json src/signals/default_signal.json  && \
	mv src/wavelets/sessions/${NAME}.json src/wavelets/default_wavelet.json && \
	make save-session NAME=${NAME} && \
	echo session ${NAME} succcessfully loaded

delete-session:
	@rm src/backgrounds/sessions/${NAME}.json && \
	rm src/signals/sessions/${NAME}.json && \
	rm src/wavelets/sessions/${NAME}.json && \
	echo session ${NAME} succcessfully deleted

purge:
	 @read -p "Are you sure? it will delete all the output folder permanently (Yes/no): " purge; \
	 if [ $$purge == "Yes" ]; then echo $$purge; fi

classifier-toy-dataset:
	@make load-session NAME=classifier_toy_dataset && \
	python3 -m src.analysis.datasets_factory.classifier_toy_dataset

visualise:
	@python3 -m src.visuals.${NAME}

classifier-fully-connected-model:
	@python3 -m src.analysis.models.classifier_fully_connected_model

classifier-convolutional-model:
	@python3 -m src.analysis.models.classifier_convolutional_model

plot-background:
	@python3 -m src.default_background $(BG_ID)

plot-signal:
	@python3 -m src.default_signal $(SIGNAL_ID)

plot-clean:
	@python3 -m src.default_clean $(SIGNAL_ID) $(BG_ID)

plot-fluctuations:
	@python3 -m src.default_fluctuations $(SIGNAL_ID) $(BG_ID)

plot-cwt-clean:
	@python3 -m src.default_cwt_clean $(SIGNAL_ID) $(BG_ID) $(WAVELET_ID)

plot-cwt-fluctuations:
	@python3 -m src.default_cwt_fluctuations $(SIGNAL_ID) $(BG_ID) $(WAVELET_ID)

echo-this:
ifdef type
	@echo $(type)
else
	@echo "options: echo-this type=type1, echo-this type=type2"
endif
