########
AMI Kiln
########

**This is an ongoing Python port of the proof of concept library: `kiln-php https://github.com/samkeen/kiln-php`**

*******
Summary
*******

This is a Packer based AMI building system. Its goal is to simplify and help organize the creation of AMIs.

************
Install/Test
************

Still alpha, getting Python package distribution worked out::

    $ mkdir ~/Projects/amiorganizer/config/

    # this will be automated in the future, but for now use
    # https://github.com/samkeen/ami-organizer/blob/master/config/config.dist.yml as template
    $ vi ~/Projects/amiorganizer/config/config.yml

    $ amiorganizer --configPath ~/Projects/amiorganizer/config/


