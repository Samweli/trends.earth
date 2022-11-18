# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LDMP - A QGIS plugin
 This plugin supports monitoring and reporting of land degradation to the UNCCD
 and in support of the SDG Land Degradation Neutrality (LDN) target.
                              -------------------
        begin                : 2017-05-23
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Conservation International
        email                : trends.earth@conservation.org
 ***************************************************************************/
"""

import os
import sys

import numpy as np

import unittest

from LDMP.calculate_ldn import ldn_total_by_trans_merge

from LDMP.test import add_default_bands_to_map

from LDMP.calculate import (
    ldn_make_prod5,
    ldn_recode_state,
    ldn_recode_traj,
    ldn_total_by_trans,
    ldn_total_deg_f,
)


class recode_stateTests(unittest.TestCase):
    def recode_to_deg(self):
        out = recode_state(np.array((-10, -2), dtype=np.int16))
        self.assertEquals(out, np.array((-1, 1), dtype=np.int16))

    def recode_to_stable(self):
        out = recode_state(np.array((-1, 1), dtype=np.int16))
        self.assertEquals(out, np.array((0, 0), dtype=np.int16))

    def recode_to_improve(self):
        out = recode_state(np.array((2, 10), dtype=np.int16))
        self.assertEquals(out, np.array((1, 1), dtype=np.int16))


def CalculateLDNUnitSuite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(recode_stateTests, "test"))
    return suite


def run_all():
    _suite = unittest.TestSuite()
    _suite.addTest(CalculateLDNUnitSuite())
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(_suite)
