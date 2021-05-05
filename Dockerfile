FROM python:3.9

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV PYTHONPATH /app
WORKDIR /app

RUN ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo Asia/Shanghai > /etc/timezone \
    && echo 'deb https://mirrors.tencent.com/debian buster main contrib non-free \
    deb https://mirrors.tencent.com/debian buster-updates main contrib non-free \
    deb https://mirrors.tencent.com/debian buster-backports main contrib non-free \
    deb https://mirrors.tencent.com/debian buster-proposed-updates main contrib non-free \
    deb-src https://mirrors.tencent.com/debian buster main contrib non-free \
    deb-src https://mirrors.tencent.com/debian buster-updates main contrib non-free \
    deb-src https://mirrors.tencent.com/debian buster-backports main contrib non-free \
    deb-src https://mirrors.tencent.com/debian buster-proposed-updates main contrib non-free**' > /etc/apt/sources.list

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY src /app
EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload"]