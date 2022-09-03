FROM nimlang/nim

RUN sudo apt update; apt -y install wget xz-utils g++ python3-dev python3-pip

RUN pip install -r requirements.txt

ENTRYPOINT ["/Mythic/mythic/payload_service.sh"]
