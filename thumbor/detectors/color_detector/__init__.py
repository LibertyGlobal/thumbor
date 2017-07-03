#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com thumbor@googlegroups.com


from thumbor.detectors import BaseDetector
from colorthief import ColorThief

class Detector(BaseDetector):

    def detect(self, callback):
        self.context.request.prevent_result_storage = True
        try:
            color_thief = ColorThief(self.context.request.image_url)
            self.context.request.dominant_color = color_thief.get_color(quality=1)
            self.context.request.palette = color_thief.get_palette(color_count=5)
        finally:
            callback([])



