#!/bin/sh
# .sh ファイルの改行コードは LF にしてください。

cd /app
uwsgi uwsgi.ini
# ↓ こう書くとエラー。
# uwsgi /app/uwsgi.ini
