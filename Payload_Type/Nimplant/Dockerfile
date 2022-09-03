FROM itsafeaturemythic/python38_payload:0.1.1

RUN apt update; apt -y install wget xz-utils g++ python3-dev python3-pip git
RUN pip install -r requirements.txt

RUN curl https://nim-lang.org/choosenim/init.sh -sSf
RUN sh init.sh -y && rm init.sh


ENTRYPOINT ["/Mythic/mythic/payload_service.sh"]
