# How to use
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
So, Im not proud I made this in python no offense. But it works Hopefully in the near future I will move it to my up coming project called Zyfron. But who knows.

Anyways, you'll need Python, Go Figure. I use [Python 3.10.4](https://www.python.org/downloads/release/python-3104/). I would recommend downloading this version from that link because I know that it works.

Next make sure you have pip installed. It should come downloaded if you use that link.

Than copy and paste this into your terminal

Normal Pip: 
```
git clone https://github.com/Leviathenn/CBuild && cd CBuild && pip install -r requirements.txt && rm build(don'tdownloadthisversion).py
```
Or if your using Pip3: 
```
git clone https://github.com/Leviathenn/CBuild && cd CBuild && pip3 install -r requirements.txt && rm build(don'tdownloadthisversion).py
```

Now all you gotta do is when thats done, just run this command and your set!

```
py build.py
```

That will automatically install updates.

the "build(don'tdownloadthisversion)" is the source for the builder if your wondering. the reason why you don't download it is because its always updating.

# Project Structure
Okay, So CBuild uses a Very stirct but simple easy and fun(don't ask) project structure.

In your src folder, things that are going to be built(executable files) are built by name. Here is the a tree for refrence: 
```
├── build
│   ├── example.exe
│   └── subdir1.exe
├── include
├── lib
├── src
│   ├── example 
│   │   ├── example.h
│   │   └── main.cpp
│   └── subdir1
│       └── main.cpp
└── build.py
```

Basically every subdir inside of src will be compiled into an executable. So it makes it easier to compile more more source code into different executables.

The lib folder doesn't work yet. I will get it working but for now its a no. Anyways its super easy probably the best out their.

Hope you enjoy it!

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://prestonwitzel.github.io"><img src="https://avatars.githubusercontent.com/u/117534523?v=4?s=100" width="100px;" alt="PrestonW"/><br /><sub><b>PrestonW</b></sub></a><br /><a href="#infra-pwitzel" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/Leviathenn/CBuild/commits?author=pwitzel" title="Tests">⚠️</a> <a href="https://github.com/Leviathenn/CBuild/commits?author=pwitzel" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
