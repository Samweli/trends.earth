#!/usr/bin/env bash

QGIS_IMAGE=qgis/qgis

QGIS_IMAGE_V_3_26=latest
QGIS_IMAGE_V_3_20=release-3_20

QGIS_VERSION_TAGS=($QGIS_IMAGE_V_3_26)

export IMAGE=$QGIS_IMAGE

for TAG in "${QGIS_VERSION_TAGS[@]}"
do
    echo "Running tests for QGIS $TAG"
    export QGIS_VERSION_TAG=$TAG
    export WITH_PYTHON_PEP=false
    export ON_TRAVIS=false
    export MUTE_LOGS=true

    docker-compose up -d

    sleep 10
#
#    docker-compose exec -T qgis-testing-environment sh -c "apt-get update"
#     docker-compose exec -T qgis-testing-environment sh -c "apt-get install -y python3-opencv"
#     docker-compose exec -T qgis-testing-environment sh -c "pip uninstall opencv-python"
#     docker-compose exec -T qgis-testing-environment sh -c "pip install opencv-python-headless"

    docker-compose exec -T qgis-testing-environment qgis_testrunner.sh LDMP.test.testplugin
    docker-compose down

done
