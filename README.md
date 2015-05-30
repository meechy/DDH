# DDH
DuckDuckHack for DDG Search Engine to give Instant Answers

------

### Operating Systems

Currently, DuckPAN has been developed on, and works well with **Ubuntu**. More specifically, we regularly build, test and run DuckPAN on **Ubuntu 12.04**. We have also successfully installed and run DuckPAN on older and newer Ubuntu releases, e.g. Ubuntu 10.04, 12.10, and 13.04.

Developers have also been successful running DuckPAN on other Linux distros (e.g. Arch, Debian) and on Mac OS X 10.8 and later, but **we make no promises that it will work outside of Ubuntu**.

As well, **there have been reported issues with installing DuckPAN on Windows**, so we don't recommend you go down that path.

That being said, we are more than willing to help you debug any installation problems, so please come to us with your problems and we'll try to get your issues sorted out. If you'd like some help from our community, feel free to engage with them on the [DuckDuckGo forum](http://duck.co/).


### Perl Versions

We run our DuckPAN tests against Perl 5.16 and 5.18 using Travis (https://travis-ci.org/duckduckgo/p5-app-duckpan). We suggest you install Perl 5.16 via Perlbrew for local development. The Codio boxes come with Perlbrew and Perl 5.18 already installed.

------


## Index
- [Starting Point] (#starting-point)
- [Getting Started](#getting-started)
- [Using the Codio Project Template](#using-the-codio-project-template)

------

## Starting Point

Go to this [link](https://duck.co/duckduckhack/ddh-intro) and read up on how to setup account on Codio. Fork this to get all ZeroClickInfo repositories.

------
## Getting Started

Getting started with DuckPAN is easy! Here's a list of ways you can get DuckPAN up & running:

- **Use our Codio Project Template ([see below](#using-the-codio-project-template))**. We highly recommended this choice! It's *super* quick and easy.
- Use our DuckDuckHack development virtual machine image ([see below](#duckduckhack-development-virtual-machine))
- Use the Vagrant virtual environment ([see below](#vagrant-virtual-environment))
- Install DuckPAN locally ([see below](#installing-duckpan-locally)). Keep in mind, this **requires Linux or Mac OS X**. We suggest you install [Ubuntu](http://www.ubuntu.com/download).

After installing DuckPAN, be sure to checkout the [Using DuckPAN](#using-duckpan) section below!

------


## Using the Codio Project Template

1. Create an account on [Codio](https://codio.com/).
2. Go to https://codio.com/duckduckgo/duckduckhack and fork the project. Make sure to fork the project and the box.
    ![Codio Fork](https://raw.githubusercontent.com/duckduckgo/duckduckgo-documentation/master/duckpan/assets/codio_fork.png)
    ![Codio Fork Both](https://raw.githubusercontent.com/duckduckgo/duckduckgo-documentation/master/duckpan/assets/codio_fork_both.png)
3. Visit one of our Instant Answer repositories (such as https://github.com/duckduckgo/zeroclickinfo-spice), and follow GitHub's instructions to first [fork](https://help.github.com/articles/fork-a-repo) the repository. You can then clone the repo into your Codio machine (You need to open the Terminal for this).  
    ![Codio Terminal](https://raw.githubusercontent.com/duckduckgo/duckduckgo-documentation/master/duckpan/assets/codio_terminal.png)
4. Go into the directory (by typing in `cd zeroclickinfo-spice`) and run `duckpan server`. Click on "DuckPAN Server" to view the webpage.
    ![Codio Server](https://raw.githubusercontent.com/duckduckgo/duckduckgo-documentation/master/duckpan/assets/codio_server.png)
5. You're all set!
    ![Codio Success](https://raw.githubusercontent.com/duckduckgo/duckduckgo-documentation/master/duckpan/assets/codio_success.png)

Try typing in queries like "define hello," and see if it works for you. You might be wondering why there are no search results in the page. It's because DuckPAN isn't configured to work with search results—it's only for testing Instant Answers.

------