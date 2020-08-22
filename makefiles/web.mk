web:
	@python3 web/app.py

build-web:
	npm run build --prefix web/static/vue-material-dashboard-master && \
	cp -r docs/gallery web/static/vue-material-dashboard-master/dist

serve-dev-frontend:
	npm install --prefix  web/static/vue-material-dashboard-master && \
	npm run dev --prefix web/static/vue-material-dashboard-master