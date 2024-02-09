# syntax = docker/dockerfile:1.4
FROM node:18-alpine as react-build

RUN mkdir -p /var/www/vision-canvas-web
WORKDIR /var/www/vision-canvas-web

COPY *.json /var/www/vision-canvas-web
RUN npm i --force

COPY public/ public/
COPY src/ src/
COPY index.html .
COPY vite.config.ts .

RUN --mount=type=secret,id=VITE_REACT_APP_FIREBASE_API_KEY \
    --mount=type=secret,id=VITE_REACT_APP_FIREBASE_AUTH_DOMAIN \
    --mount=type=secret,id=VITE_REACT_APP_FIREBASE_DATABASE_URL \
    --mount=type=secret,id=VITE_REACT_APP_FIREBASE_PROJECT_ID \
    --mount=type=secret,id=VITE_REACT_APP_FIREBASE_STORAGE_BUCKET \
    --mount=type=secret,id=VITE_REACT_APP_FIREBASE_MESSAGING_SENDER_ID \
    --mount=type=secret,id=VITE_REACT_APP_FIREBASE_APP_ID \
    --mount=type=secret,id=VITE_REACT_APP_API_URL \
<<EOF
echo VITE_REACT_APP_FIREBASE_API_KEY=$(cat /run/secrets/VITE_REACT_APP_FIREBASE_API_KEY) >> .env
echo VITE_REACT_APP_FIREBASE_AUTH_DOMAIN=$(cat /run/secrets/VITE_REACT_APP_FIREBASE_AUTH_DOMAIN) >> .env
echo VITE_REACT_APP_FIREBASE_DATABASE_URL=$(cat /run/secrets/VITE_REACT_APP_FIREBASE_DATABASE_URL) >> .env
echo VITE_REACT_APP_FIREBASE_PROJECT_ID=$(cat /run/secrets/VITE_REACT_APP_FIREBASE_PROJECT_ID) >> .env
echo VITE_REACT_APP_FIREBASE_STORAGE_BUCKET=$(cat /run/secrets/VITE_REACT_APP_FIREBASE_STORAGE_BUCKET) >> .env
echo VITE_REACT_APP_FIREBASE_MESSAGING_SENDER_ID=$(cat /run/secrets/VITE_REACT_APP_FIREBASE_MESSAGING_SENDER_ID) >> .env
echo VITE_REACT_APP_FIREBASE_APP_ID=$(cat /run/secrets/VITE_REACT_APP_FIREBASE_APP_ID) >> .env
echo VITE_REACT_APP_API_URL=$(cat /run/secrets/VITE_REACT_APP_API_URL) >> .env
EOF

EXPOSE 5173

ENTRYPOINT ["npm", "run", "dev"]
