# ubuntu という明言は無いが何か使えるので……。
# FROM python:3.10.0a2-slim
FROM python:3.9-slim

# 連絡先
LABEL maintainer="muzudho1@gmail.com"

# Dockerfile ではまず root ユーザーで全体をざっくり環境構築して、必要なら後付けでユーザー設定してください。

# .pid ファイルを置くところ。
WORKDIR /usr/local/var/run

# ログ・ファイルを置くところ。
WORKDIR /usr/local/var/log

RUN apt-get update && apt-get install -y \
    # `gcc` - なぜか flaskパッケージが C コンパイラーを欲しがるんだぜ☆（＾～＾）
    gcc \
    uwsgi

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install uwsgi flask

ENV FLASK_APP /app/webapp.py

# ドキュメント・ルート
COPY ./app /app
RUN chmod 755 /app

# 起動スクリプト
COPY ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod 755 /usr/local/bin/docker-entrypoint.sh

# ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
