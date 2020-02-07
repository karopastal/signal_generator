list-sessions:
	@ls src/signals/sessions

save-session:
	@cp config/backgrounds/default_background.json config/backgrounds/sessions/${NAME}.json && \
	cp config/signals/default_signal.json config/signals/sessions/${NAME}.json && \
	cp config/wavelets/default_wavelet.json config/wavelets/sessions/${NAME}.json && \
	echo session ${NAME} succcessfully saved

load-session:
	@mv config/backgrounds/sessions/${NAME}.json config/backgrounds/default_background.json && \
	mv config/signals/sessions/${NAME}.json config/signals/default_signal.json  && \
	mv config/wavelets/sessions/${NAME}.json config/wavelets/default_wavelet.json && \
	make save-session NAME=${NAME} && \
	echo session ${NAME} succcessfully loaded

delete-session:
	@rm config/backgrounds/sessions/${NAME}.json && \
	rm config/signals/sessions/${NAME}.json && \
	rm config/wavelets/sessions/${NAME}.json && \
	echo session ${NAME} succcessfully deleted