#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 23:27:11 2018

@author: jie
"""
import plotly
plotly.tools.set_credentials_file(username='josjsjen', api_key='mZCF44s0DRmbruynfCMJ')

import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x=[1, 2, 3, 4],
        y=[2, 1, 3, 4],
        error_y=dict(
            type='data',
            symmetric=False,
            array=[0.1, 0.2, 0.1, 0.1],
            arrayminus=[0.2, 0.4, 1, 0.2]
        )
    )
]

py.iplot(data, filename='error-bar-asymmetric-array')