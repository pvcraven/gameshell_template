Python Arcade Game Template For Gameshell
=========================================

* Install Python 3.6
* Install the Arcade library
* Clone the template
* Install
* Restart

Install Python 3.6
------------------

Gameshell runs on Debian Linux. Right now, Debian uses Python 3.5, and Arcade
requires 3.6. So to install 3.6, we need to tell Debian to look at the "testing"
set of files.

Shell over to your Gameshell, and copy/paste the following:

.. code-block:: bash

    echo "deb http://ftp.fr.debian.org/debian testing main" | sudo tee -a /etc/apt/sources.list

After you do that, run then following commands:

.. code-block:: bash

    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install -y python3.6

Install Arcade
--------------

Now that we have Python 3.6, we need to install the Arcade library. Do that with:

.. code-block:: bash

    python3.6 -m pip install arcade

Clone Game
----------

.. code-block:: bash

    cd ~/games
    git clone git@github.com:pvcraven/gameshell_template.git

Install the Game
----------------

.. code-block:: bash

    cd ~/games/gameshell_tempate
    chmod u+x install.sh
    ./install.sh