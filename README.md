The inspiration behind this project was a math youtuber known as 3Blue1Brown. Math can sometimes be hard to grasp. While going through some of 3Blue1Brown's videos, having a unique visual and interpretation of a problem provided additonal insight and further understanding, which motivated me to do the same. 

The following animations made in this project were made using manim (python library), an animation engine for explanatory math videos created by Grant Sanderson or 3Blue1Brown.

**Dependancies**

Instillation (mac)
To install all required dependencies for installing Manim (namely: ffmpeg, Python, and some required Python packages), run:

`brew install py3cairo ffmpeg`

On Apple Silicon based machines (i.e., devices with the M1 chip or similar; if you are unsure which processor you have check by opening the Apple menu, select About This Mac and check the entry next to Chip), some additional dependencies are required, namely:

`brew install cmake pango scipy`

After all required dependencies are installed, simply run:

`pip3 install manim`

to install Manim.

Instillation (windows)
Manim can be installed via Chocolatey simply by running:

`choco install manimce`

Instillation (linux)
To first update your sources, and then install Cairo, Pango, and FFmpeg simply run:

`sudo apt update`

`sudo apt install libcairo2-dev libpango1.0-dev ffmpeg`

If you don’t have python3-pip installed, install it via:

`sudo apt install python3-pip`

Then, to install Manim, run:

`pip3 install manim`




