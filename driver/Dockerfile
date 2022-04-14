FROM baseImage
#RUN apt-get update -y
#RUN apt-get install -y wget xvfb unzip
#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
#RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
#RUN apt-get update -y
#RUN apt-get install -y google-chrome-stable
#ENV CHROMEDRIVER_VERSION 100.0.4896.60
#ENV CHROMEDRIVER_DIR /chromedriver
#RUN mkdir $CHROMEDRIVER_DIR
#RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
#RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR
#ENV PATH $CHROMEDRIVER_DIR:$PATH
#this directory not and is never used needed at the moment pulling the base image is enough