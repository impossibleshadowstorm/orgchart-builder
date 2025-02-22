FROM node:22.12.0

WORKDIR /app

# Copy package.json and yarn.lock first for better caching
COPY package.json yarn.lock /app/

# Install dependencies
RUN yarn install

# Copy the rest of the app files
COPY . /app/

EXPOSE 5173

CMD ["yarn", "dev", "--host"]
