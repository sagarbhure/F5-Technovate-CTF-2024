FROM node:12-buster-slim

WORKDIR /app
COPY package.json .

ENV NODE_ENV production
ENV PORT 9998
RUN npm install

COPY . .

EXPOSE 9998

CMD ["node", "/app/server.js"]
