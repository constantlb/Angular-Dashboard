FROM node:14.15.2-alpine

ADD . /app
WORKDIR /app

RUN npm install -g @angular/cli@11.0.5
RUN npm install

EXPOSE 4200

CMD npm start
