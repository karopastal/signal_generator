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