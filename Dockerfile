FROM erdembey/epicuserbot:latest
RUN git clone https://github.com/FaridDadashzade/NeonUserBot-Old /root/NeonUserBot-Old
WORKDIR /root/NeonUserBot-Old/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
