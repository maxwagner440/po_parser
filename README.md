
To Build Docker:

build:
    - docker build -t po-parser .
run:
    docker run  --it po-parser
run interactive shell:
    docker run --it po-parser sh