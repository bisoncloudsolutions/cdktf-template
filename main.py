#!/usr/bin/env python
from cdktf import App
from stacks.demo import Demo
from stacks.demo import DEMO_STACK_ID

app = App()

Demo(app, DEMO_STACK_ID)

app.synth()
