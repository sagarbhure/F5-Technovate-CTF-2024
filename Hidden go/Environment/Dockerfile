FROM golang:1.23-alpine

WORKDIR /app

COPY . .

RUN go build -o server .

EXPOSE 9994

CMD ["./server"]
