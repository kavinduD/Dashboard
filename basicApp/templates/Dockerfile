# syntax=docker/dockerfile:1
   
FROM node:18-alpine
WORKDIR /templates
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 4000