Title: ia32libs on 64-bit Debian Wheezy
Date: 2014-07-2 10:00
Category: debian
Tags: Debian, Notetoself, Unix 
Slug: ia32libs
Author: Oscar Carlsson
Lang: en
Summary: A short guide on how to get 32-bit programs working on a 64-bit debian wheezy using ia32libs.

Tried to install a VPN earlier, Forticlient SSL VPN, on my 64-bit Debian wheezy but it turned out to only exist a 32 bit version.

```bash
# My system:
$ uname -a
$ Linux lad-laptop 3.2.0-4-amd64 #1 SMP Debian 3.2.57-3+deb7u2 x86_64 GNU/Linux
```

After googling for solutions the standard reply was to install a library which would make 32-bit programs just work: `ia32-libs-gtk`.

So i tried this, with no luck:

> The following packages have unmet dependencies: <br> ia32-libs : Depends: ia32-libs-i386 but it is not installable <br> E: Unable to correct problems, you have held broken packages.

So I found a couple of guides but everyone differed in something. I will now retell what worked for me.
First I had to tell the package management, dpkg, that I wanted `i386` libraries (32bit)
```bash
$ dpkg --add-architecture i386
```

then change the lines in `/etc/apt/source.list` to look like following

```
deb [arch=amd64,i386] http://ftp.se.debian.org/debian/ wheezy main
```

And then update the system with
```bash
$ sudo apt-get update ; sudo apt-get dist-upgrade 
$ sudo apt-get install ; sudo apt-get dist-upgrade
```

and then I was able to install the ia32-lib and get Forticlient working.

```bash
$ sudo apt-get install ia32-libs-gtk && sudo apt-get install libgtk2.0-0:i386
```
Note: I have still not gotten any errors by allowing i386 libs on my system but I will update this post if anything bad happens.
