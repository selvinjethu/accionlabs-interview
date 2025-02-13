#Dockerfile for nginx 1.19

FROM nginx:1.19.0-alpine
WORKDIR /var/www/html
RUN rm -rf /etc/nginx/config.d/default.conf
#add user and group for non root user, expose 80
COPY nginx.conf /etc/nginx/conf.d/default.conf
CMD ["nginx", "-g", "demon off;"]
