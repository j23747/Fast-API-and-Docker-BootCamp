FROM python:3.6
COPY . . 
COPY ./requirements.txt ./requirements.txt
EXPOSE 8000:8000
RUN pip3 install -r requirements.txt
CMD ["python3", "server.py"]




# # FROM python:3.6
# # COPY . 
# # COPY ./requirements.txt ./requirements.txt
# # WORKDIR .

# # EXPOSE 8000:8000
# # RUN pip install -r requirements.txt
# # CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--reload"]
