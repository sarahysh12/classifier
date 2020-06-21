FROM node

WORKDIR /client

COPY package.json /client/

RUN npm install

COPY /src/ /client/src/
COPY /public/ /client/public/

EXPOSE 3000
CMD ["npm","start"]

