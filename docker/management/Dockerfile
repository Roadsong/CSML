FROM alpine:3.10

RUN apk update && apk add --no-cache alpine-sdk python3 vim moreutils

RUN cd / \
    && mkdir results

# Include management code