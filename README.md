# ecmm409-quadruped

[![python 3.9.2](https://img.shields.io/badge/python-3.9.2-blue.svg)](https://www.python.org/downloads/release/python-392/)

Training and evolution of a virtual two-legged robot.

For the Virtual Creatures Competition 2022 (https://virtualcreatures.github.io/).

## Demo

![Screenshot of an optimised child walker, which is the output of the evolutionary algorithm](media/thumbnail.png)

https://www.youtube.com/watch?v=7wZyJ0yNZHA

## Purpose

This project implements a 3D computer simulation of a two-legged walker, built using pybullet and pyrosim. 

The demonstration is followed by a showcase of the genetic algorithm optimising the walker over 6 generations. For each generation, the fitness score of each member is measured in a dynamic simulation. The fittest members of the population are selected, and children are produced based on each pair. Children have a small chance to mutate, in order to escape local maxima. 

The end goal is a child that can travel as far as possible in the fixed time that the simulation runs for, which is 2160 frames.

## Installation

> Make sure you're running Python 3.9 with `pip3` installed.

Set up and activate a virtual environment:

```bash
$ python -m venv '.env'
```

To activate:

```bash
$ source .env/bin/activate          # Linux
$ source .env/Scripts/activate      # Windows
```

Install the required `pip` packages to your environment:

```bash
$ pip install -r requirements.txt
```

Install `pybullet` (`bullet3`) manually, as the `pip` distribution is [buggy](https://github.com/bulletphysics/bullet3/issues/1864):

```bash
$ git clone https://github.com/$ bulletphysics/bullet3
$ cd bullet3
$ python setup.py build
$ python setup.py install
```

## Usage

All files should be run from the root directory (i.e. `ecmm409-quadruped/`).

To run the full evolutionary simulation:

```bash
$ python quadruped/evolution.py
```

To generate an example creature for the manual simulation:

```bash
$ python quadruped/generation.py
```

To run the manual simulation with the generated creature:

```bash
$ python quadruped/simulation.py
```
