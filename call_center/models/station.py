# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Station(models.Model):
	_name='call_center.station'

	name=fields.Char()
	calls=fields.One2many(comodel_name='call_center.calls',inverse_name='station')