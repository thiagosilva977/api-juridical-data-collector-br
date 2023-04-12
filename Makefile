# Docker info
DOCKER_IMAGE_NAME=thiago977/thiagosilva_consulta_juridica
DOCKER_IMAGE_TAG=1.0.0

# Install project dependencies
setup:
	pip3 install -e . --upgrade --no-cache-dir
	mkdir -p pipeline
	touch make_setup

# Uninstall project dependencies
unsetup:
	pip3 uninstall -y someexternalprojectname


	rm -f make_setup

# Use this only in private projects
docker/id_rsa:
	# To access private projects
	#cp ~/.ssh/id_rsa docker/id_rsa

# Use this only in private projects
docker/id_rsa.pub:
	# To access private projects
	#cp ~/.ssh/id_rsa.pub docker/id_rsa.pub

# Build docker package
docker/package: docker/id_rsa docker/id_rsa.pub
	python3 setup.py bdist_wheel --dist-dir=docker/package
	rm -rf build

# Build docker image
docker/image: docker/package
	docker build docker -f docker/Dockerfile -t $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG)
	touch docker/image

# Push docker image
docker/push: docker/image
	docker push $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG)
	touch docker/push

# Push docker image with latest tag
docker/push-latest: docker/image
	docker tag $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG) $(DOCKER_IMAGE_NAME):latest
	docker push $(DOCKER_IMAGE_NAME):latest
	touch docker/push-latest

# Clean all
clean:
	rm -rf docker/package
	rm -rf docker/image
	rm -rf docker/push
	rm -rf docker/push-latest
	rm -rf docker/id_rsa
	rm -rf docker/id_rsa.pub

# Uninstall/install dependencies, create docker image and push.
do_all:
	make clean
	make unsetup
	sudo docker login
	python setup.py sdist
	make setup
	make docker/image
	make docker/push-latest