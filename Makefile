.PHONY: test web

include makefiles/web.mk
include makefiles/models.mk
include makefiles/datasets.mk
include makefiles/sessions.mk
include makefiles/visualizations.mk

#test:
#	@python3 -m unittest discover

#purge:
#	 @read -p "Are you sure? it will delete all the output folder permanently (Yes/no): " purge; \
#	 if [ $$purge == "Yes" ]; then echo $$purge; fi

#echo-this:
#ifdef type
#	@echo $(type)
#else
#	@echo "options: echo-this type=type1, echo-this type=type2"
#endif
