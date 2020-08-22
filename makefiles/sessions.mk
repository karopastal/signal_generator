list-sessions:
	@ls config/signals/sessions

new-session:
	@cp config/sessions/empty_session.json config/backgrounds/sessions/${NAME}.json && \
	cp config/sessions/empty_session.json config/signals/sessions/${NAME}.json && \
	cp config/sessions/empty_session.json config/wavelets/sessions/${NAME}.json && \
	echo session ${NAME} succcessfully created

load-empty-session:
	@cp config/sessions/empty_session.json config/backgrounds/default_background.json && \
	cp config/sessions/empty_session.json config/signals/default_signal.json && \
	cp config/sessions/empty_session.json config/wavelets/default_wavelet.json && \
	echo empty session succcessfully loaded

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

delete-current-session:
	@rm config/backgrounds/sessions/${NAME}.json && \
	rm config/signals/sessions/${NAME}.json && \
	rm config/wavelets/sessions/${NAME}.json && \
	make load-empty-session && \
	echo session ${NAME} succcessfully deleted
