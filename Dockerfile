FROM continuumio/miniconda3
RUN conda config --add channels conda-forge
RUN conda config --set channel_priority strict
RUN conda update --all
RUN conda create -n env anaconda jupyterhub pyspark oauthenticator
RUN conda update -n base -c defaults conda
RUN echo "source activate env" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH
COPY jupyterhub_config.py /

# docker build -t jupyterhub .
# docker run -p 8000:8000 -it --mount source=home,target=/home jupyterhub
# jupyterhub --ip 0.0.0.0 
