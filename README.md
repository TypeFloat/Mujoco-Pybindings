# Mujoco_pybindings

When I use mujoco's python module, LSP can't provide the completions and hints correctly because there are no pyi files for mujoco. Pycharm is a powerful Python IDE that can automatically scan and generate module documentation from the library. I am not used to using Pycharm because it is "too powerful", so I use Pycharm to generate mujoco module documentation and manually write the pyi files for LSP correct completion and hint.

## Usage

Firstly, you should install mujoco correctly.

Secondly, head over to your installed mujoco module, and clone the repository just here. Make sure that the directory you have just cloned is named `pybindings`.

Thirdly, touch a file named `__init__.pyi`, and echo `from mujoco.pybindings import *` in it.

Lastly, enjoy the intelligent completions and hints.

## Issue

The files in the repository are what I am using, so it is incomplete. You can raise an issue and I will soon complete it.