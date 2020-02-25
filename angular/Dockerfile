FROM node:12.13-alpine

ADD . /app
WORKDIR /app

RUN npm install
RUN npm install -g @angular/cli@7.3.9

EXPOSE 4200

CMD npm start
