
# NovaPi-OS
![NovaPi OS intro image](https://cdn.discordapp.com/attachments/1024281373726474353/1161678073087930480/image.png?ex=65392c03&is=6526b703&hm=3d1d2c8893a687726d033e38b2cc40dc64587ac35b4551fa06eb7fd6fa86ebba&)

A custom NovaPi shell where you can customize your ideal MakeX Challenge robot!

## Features!
* Not yet. This project is under rapid developement!

## Requirements
* A NovaPi. [If you dont have one. You can get it here!](https://aliexpress.com/item/1005004418087757.html)
* An mbuild Bluetooth module and a USB bluetooth transceiver
* A Computer or laptop
* Micro USB Cable
* Python 3 installed on your computer
* PuTTY installed on your computer
## A nice to haves
* Raspberry pi ( For headless control )
* [mblock programming software](https://www.mblock.cc/en/)
## Steps
* Plug your NovaPi into your computer
* Identify which USB port your computer recognises
	*  On Windows, it should identify itself as **COM** port
	* On MacOS, it should identify itself with **/dev/ttyUSB**
	* Sadly we are having a hard time to get everything working on Linux
* Launch PuTTY
	* Change **Connection type** to **Serial**
	* Put **Serial line** to your identified device ( From step 2! )
	* Change **Speed** to 115200
	* Open right away!
* You will see a crazy boot screen on a serial terminal, give it time.
* Once you greet with a **>** text. The program is yours to explore!
	* If you dont know how to use this software, Run **help** for all list of commands
	* For MakeX Challenge contestants, To try out our software. Run **setup** to setup this software that will work best with your current robot setup
