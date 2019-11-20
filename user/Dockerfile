FROM alpine:3.10

RUN apk update && apk add --no-cache alpine-sdk python3 vim

# Include user code

# Get current docker's id, maybe we should use ENV instead of RUN
# Will test later
RUN export CONTAINER_ID=$(head -1 /proc/self/cgroup|cut -d/ -f3)