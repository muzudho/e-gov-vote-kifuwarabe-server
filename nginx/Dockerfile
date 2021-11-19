# FROM ubuntu:20.10
FROM nginx:1.18

# RUN apt-get update && apt-get install -y \
#     nginx

# 設定ファイル
COPY ./conf/app.conf /etc/nginx/conf.d/app.conf

# ドキュメント・ルート
COPY ./app/index.html /app/index.html

# フォアグラウンドでnginx実行
CMD nginx -g "daemon off;"
