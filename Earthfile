VERSION 0.7
FROM python:3.10-slim

WORKDIR /code

deps:
    COPY requirements.txt ./
    RUN pip install -r requirements.txt
    COPY . .

test:
    FROM +deps
    RUN python -m pytest -v

build:
	BUILD +test
    FROM +deps
    # Remove dev dependencies if needed
    EXPOSE 8000
    ENTRYPOINT ["python"]
    CMD ["notes_app.py"]
    SAVE IMAGE notes-app:latest