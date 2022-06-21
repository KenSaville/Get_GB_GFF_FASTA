FROM 812206152185.dkr.ecr.us-west-2.amazonaws.com/wf-base:fbe8-main



# Or use managed library distributions through the container OS's package
# manager.
RUN pip3 install bio --upgrade


# You can use local data to construct your workflow image.  Here we copy a
# pre-indexed reference to a path that our workflow can reference.

copy wf /root/wf


# STOP HERE:
# The following lines are needed to ensure your build environement works
# correctly with latch.
ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag
RUN  sed -i 's/latch/wf/g' flytekit.config
RUN python3 -m pip install --upgrade latch
WORKDIR /root
