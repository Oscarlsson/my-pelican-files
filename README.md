my-pelican-files
================

Files to generate the content of oscarlsson.github.io

Assumes pelican-themes and pelican-plugins is located in ..


Setup
================
To get pelican, themes and plugins if you want to make changes or generate your own blog.


```
cd <devfolder>
git clone git@github.com:getpelican/pelican.git
cd pelican
sudo python setup.py install
sudo pip install markdown
```

```
git clone git@github.com:Oscarlsson/pelican-themes.git
git clone git@github.com:getpelican/pelican-plugins.git
sudo pip install webassets cssmin 
```

```
git clone git@github.com:Oscarlsson/my-pelican-files.git
cd my-pelican-files 
```

Starting local server: ```make devserver```

stopping it : ```./develop_server.sh stop``` 

As we are hosting the blog on github-pages we have another repository for that
```git clone git@github.com:Oscarlsson/Oscarlsson.github.io.git output```

Changes made in my-pelican-files will be written to output. When we are sattisfied with
what is in output we push it to the github.io-repository

