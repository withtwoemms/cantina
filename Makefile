TEST_FILE := test_app.py


all: 
	@echo "FLASK APP -->" ${FLASK_APP}
	@echo "FLASK ENV -->" ${FLASK_APP_ENV}

test: 
	$(eval export FLASK_APP_ENV=test)
	@echo "CURRENT_ENV -->" ${FLASK_APP_ENV}
	python $(TEST_FILE)

dev:
	$(eval export FLASK_APP_ENV=dev)
	@echo "CURRENT_ENV -->" ${FLASK_APP_ENV}
	python ${FLASK_APP}

.PHONY: all test
