FROM python:3.11
WORKDIR /gpt

COPY ./gtp_api /gpt/gtp_api
COPY ./requirements.txt /gpt
COPY ./README.md /gpt

RUN pip install --no-cache-dir --upgrade -r /gpt/requirements.txt

EXPOSE 7000

CMD ["uvicorn", "gtp_api.app:app", "--host", "0.0.0.0", "--port", "7000"]
