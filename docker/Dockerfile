ARG SOURCE=ghcr.io/neuralmagic/cuda-python3.8
ARG PACKAGE_NAME="sparseml-nightly[onnxruntime,torchvision,transformers,yolov5,ultralytics]"

FROM ghcr.io/neuralmagic/sparseml-nightly:latest

RUN pip install --no-cache-dir $PACKAGE_NAME

HEALTHCHECK CMD python3.8 -c 'import sparseml'
RUN pip list | grep sparseml
CMD bash